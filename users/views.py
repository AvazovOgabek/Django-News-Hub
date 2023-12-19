from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages


def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid Credentials')
            return render(request, 'signin.html')
    return render(request, 'signin.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm-password')
        if password == confirm_password:
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Email is taken')
                return redirect('signup')
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username is taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, password=password)
                return redirect('signin')
                
    return render(request, 'signup.html')


