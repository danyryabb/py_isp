from django import forms
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect, reverse
from .models import BlogPost
from django.http import HttpResponse
from useraccount.models import Account
from .forms import UpdateBlogPostForm, CreateBlogPostForm


def create_blog_view(request):
	context = {}
	user = request.user
	if not user.is_authenticated:
		return redirect('must_authenticate')
	form = CreateBlogPostForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		obj = form.save(commit=False)
		author = Account.objects.filter(email=user.email).first()
		obj.author = author
		obj.save()
		form = CreateBlogPostForm()
	context['form'] = form
	return render(request, "article/create_blog.html", context)


def detail_blog_view(request, slug):
	context = {}
	blog_post = get_object_or_404(BlogPost, slug=slug)
	context['blog_post'] = blog_post
	return render(request, 'article/detail_blog.html', context)


def edit_blog_view(request, slug):
	context = {}
	user = request.user
	if not user.is_authenticated:
		return redirect("must_authenticate")
	blog_post = get_object_or_404(BlogPost, slug=slug)
	if blog_post.author != user:
		return HttpResponse('You are not the author of that post.')

	if request.POST:
		form = UpdateBlogPostForm(request.POST or None, request.FILES or None, instance=blog_post)
		if form.is_valid():
			obj = form.save(commit=False)
			obj.save()
			context['success_message'] = "Updated"
			blog_post = obj

	form = UpdateBlogPostForm(
			initial = {
					"title": blog_post.title,
					"body": blog_post.body,
					"image": blog_post.image,
			}
		)

	context['form'] = form
	return render(request, 'article/edit_blog.html', context)


# def like_post(request):
#     context = {}
#     post = get_object_or_404(BlogPost, id=request.POST.get('post_id'))
#     if post.likes.filter(id=request.user.pk).exists():
#         post.likes.remove(request.user)
#         is_liked = False
#     else:
#         post.likes.add(request.user)
#         is_liked = True
#     context['is_liked'] = is_liked
#     return HttpResponseRedirect(post.get_absolute_url(), context)