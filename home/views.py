from django.shortcuts import render, redirect
from .models import View, NewsArticle
from django.contrib.auth.decorators import login_required
from django.db.models import Count

@login_required(login_url='signin')
def home(request):
    articles = NewsArticle.objects.annotate(view_count=Count('view')).order_by('publication_date')
    most_viewed_article = NewsArticle.objects.annotate(num_views=Count('view')).order_by('-num_views').first()
    most_article_view_count = View.objects.filter(article=most_viewed_article).count()

    
    return render(request, 'home.html', {'articles' : articles, 'most_viewed_article':most_viewed_article, 'most_article_view_count':most_article_view_count})

@login_required(login_url='signin')
def article_detail(request, article_id):
    article = NewsArticle.objects.get(id=article_id)
    most_viewed_article = NewsArticle.objects.annotate(num_views=Count('view')).order_by('-num_views').first()
    view = View.objects.filter(article=article, user=request.user)
    most_article_view_count = View.objects.filter(article=most_viewed_article).count()
    if not view:
        view = View.objects.create(article=article, user=request.user)
        view.save()
    view_count = View.objects.filter(article=article).count()
    return render(request, 'article_detail.html', {'article':article, 'view_count':view_count, 'most_viewed_article':most_viewed_article, 'most_article_view_count':most_article_view_count})
