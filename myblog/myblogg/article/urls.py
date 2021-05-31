from django.urls import re_path, path
from article.views import (
	create_blog_view,
	detail_blog_view,
	edit_blog_view,
    like_post,
)

app_name = 'article'

urlpatterns = [
    path('create/', create_blog_view, name="create"),
    path('<slug>/', detail_blog_view, name="detail"),
    path('<slug>/edit/', edit_blog_view, name="edit"),
    path('like/', like_post, name='like_post')
]
