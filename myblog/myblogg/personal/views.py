import asyncio
import time

from asgiref.sync import sync_to_async
from django.http import HttpResponse
from django.shortcuts import render
from operator import attrgetter
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
from article.models import BlogPost

BLOG_POSTS_PER_PAGE = 5


def home_screen_view(request, *args, **kwargs):
    context = {}
    # Search
    query = ""
    if request.GET:
        query = request.GET.get('q', '')
        context['query'] = str(query)
    blog_posts = sorted((get_blog_queryset(query)), key=attrgetter('date_updated'), reverse=True)
    # Pagination
    page = request.GET.get('page', 1)
    blog_posts_paginator = Paginator(blog_posts, BLOG_POSTS_PER_PAGE)
    try:
        blog_posts = blog_posts_paginator.page(page)
    except PageNotAnInteger:
        blog_posts = blog_posts_paginator.page(BLOG_POSTS_PER_PAGE)
    except EmptyPage:
        blog_posts = blog_posts_paginator.page(blog_posts_paginator.num_pages)
    context['blog_posts'] = blog_posts
    return render(request, "personal/home.html", context)


def get_blog_queryset(query=None):
    queryset = []
    queries = query.split(" ")
    blogs = BlogPost.objects.all()
    for q in queries:
        posts = blogs.filter(
				Q(title__icontains=q) |
				Q(body__icontains=q)
			).distinct()

        for post in posts:
            queryset.append(post)
    return list(set(queryset))


def sync_search_view(request):
    start_time = time.time()
    get_blog_queryset_sync()
    total = (time.time() - start_time)
    print('total sync', total)
    return HttpResponse('sync')
# total sync 2.0138511657714844


def get_blog_queryset_sync():
    print('prepare to get all blogs - sync')
    time.sleep(2)
    blogs = BlogPost.objects.all()
    print(blogs)
    print('got all blogs - sync')


async def async_search_view(request):
    start_time = time.time()
    task = asyncio.ensure_future(get_blogs_async())
    await asyncio.wait([task])
    total = (time.time() - start_time)
    print('total async', total)
    return HttpResponse('async')
# total async 0.030826807022094727


@sync_to_async
def get_blogs_async():
    print('prepare to get all blogs - async')
    asyncio.sleep(2)
    blogs = BlogPost.objects.all()
    print(blogs)
    print('got all blogs - async')