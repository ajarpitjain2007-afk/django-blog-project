from django.urls import path
from .import views
from django.contrib.auth.views import LoginView , LogoutView
# from django.contrib.auth import views as auth_views
urlpatterns = [
    path('register/',views.register,name='register'),
    
    path('profile/',views.Profile,name='profile'),
    path('login/',LoginView.as_view(template_name='users/login.html',next_page='blog-home'),name = 'login'),
    path('logout/',LogoutView.as_view(template_name='users/logout.html',http_method_names=['get', 'post']),name = 'logout'),
    
]

