from . import views
from django.urls import path

urlpatterns = [
    path('singin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
]