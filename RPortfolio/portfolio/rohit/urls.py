from django.contrib import admin
from django.urls import path,include
from rohit import views

urlpatterns = [
    path('',views.index,name='index'),
    path('signup',views.handleSignup, name="handleSignup"),
    path('login',views.handleLogin, name="handleLogin"),
    
]
