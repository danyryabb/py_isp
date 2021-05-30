from django.urls import re_path, path
from . import views
from article.views import (
	create_blog_view,
	detail_blog_view,
	edit_blog_view,
)

app_name = 'article'

urlpatterns = [
    # re_path(r'^<slug>/', views.detail_blog_view, name="detail"),
    path('create/', create_blog_view, name="create"),
    path('<slug>/', detail_blog_view, name="detail"),
    # re_path(r'^create/', views.create_blog_view, name='create'),
    # re_path(r'^like/$', views.like_post, name='like_post')
    # re_path(r'^<slug>/edit/', views.detail_blog_view, name="edit"),
    path('<slug>/edit/', edit_blog_view, name="edit"),

]
