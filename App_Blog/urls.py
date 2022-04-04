from django.urls import path
from . import views
app_name = 'App_Blog'

urlpatterns = [
    path('', views.BlogList.as_view(), name='blog_list'),
    path('write/', views.CreateBlog.as_view(), name='create_blog'),
    path('detail/<int:blog_id>/', views.blog_details,name='blog_details'),

    path('liked/<int:blog_id>/',views.liked, name='liked_post'),
    path('unliked/<int:blog_id>/',views.unliked, name='unliked_post'),

    path('my-blogs/', views.MyBlog.as_view(), name='my_blogs'),
    path('edit/<int:pk>/', views.UpdateBlog.as_view(), name='edit_blog'),
]