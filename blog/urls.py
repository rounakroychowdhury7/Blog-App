from django.urls import path
from . import views
from.views import (all_posts,
                   post_detail,
                   post_create,
                   post_delete,
                   post_update,
                   posts_user,
                )
from users import views as user_views

urlpatterns = [
   
    path('', all_posts.as_view(), name='blog-home'),
    path('post/<int:pk>/', post_detail.as_view(), name='post-detail'),
    path('post/<str:username>', posts_user.as_view(), name='post-user'),
    path('post/new/', post_create.as_view(), name='post-create'),
    path('post/<int:pk>/update/', post_update.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', post_delete.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'),
    path('register/', user_views.register, name='blog-register'),
    
]
