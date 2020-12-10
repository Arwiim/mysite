from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    # post views
    #path('login/', views.user_login, name='login'), the view ho we create
    path('login/', auth_views.LoginView.as_view(), name='login'), #django views
    path('logout/', auth_views.LogoutView.as_view(), name='logout'), #django logout view
    path('', views.dashboard, name='dashboard')
]