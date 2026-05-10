from django.urls import path 
from . import views

from .views import PostListView , PostDetailView , PostCreateView , PostUpdateView ,  PostDeleteView
# from users.views import register , profile
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView , LogoutView



urlpatterns = [
     
     path('',PostListView.as_view(),name='blog-home'),
     path('blog/<int:pk>/',PostDetailView.as_view(),name='blog-detail'),
     path('blog/create',PostCreateView.as_view(),name='blog-create'),
     path('blog/<int:pk>/update',PostUpdateView.as_view(),name='blog-update'),
     path('blog/<int:pk>/delete',PostDeleteView.as_view(),name='blog-delete'),
     path("about/", views.about, name='blog-about'),
     path("post/<int:pk>/like", views.BlogLikes, name='blog-like'),
     path("post/<int:pk>/comment", views.add_comment, name='blog-comment'),
    
]
