from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.posts, name='posts'),
    path('post/insert/', views.post_insert, name='insert_post'),
    path('post/edit/', views.post_edit, name='edit_post')
]
