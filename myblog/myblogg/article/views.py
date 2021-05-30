from django import forms
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect, reverse
from .models import BlogPost, Comment
from django.db.models import Q
from django.http import HttpResponse
from useraccount.models import Account


class CreateBlogPostForm(forms.ModelForm):
	class Meta:
		model = BlogPost
		fields = ['title', 'body', 'image']


class UpdateBlogPostForm(forms.ModelForm):
	class Meta:
		model = BlogPost
		fields = ['title', 'body', 'image']

	def save(self, commit=True):
		blog_post = self.instance
		blog_post.title = self.cleaned_data['title']
		blog_post.body = self.cleaned_data['body']

		if self.cleaned_data['image']:
			blog_post.image = self.cleaned_data['image']

		if commit:
			blog_post.save()
		return blog_post


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = {'content'}


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


def get_blog_queryset(query=None):
	queryset = []
	queries = query.split(" ")
	for q in queries:
		posts = BlogPost.objects.filter(
				Q(title__icontains=q) |
				Q(body__icontains=q)
			).distinct()

		for post in posts:
			queryset.append(post)

	return list(set(queryset))


# def PostDetail(self, pk):
#     context = {}
#     post = BlogPost.objects.get(id=pk)
#     comment = Comment.objects.filter(post_id=post.id)
#     is_liked = False
#     if post.likes.filter(id=self.user.pk).exists():
#         is_liked = True
#     if self.POST:
#         form = CommentForm(self.POST)
#         if form.is_valid():
#             if self.user.is_authenticated:
#                 content = self.POST.get('content')
#                 comment = Comment.objects.create(post=post, user_id=self.user.pk, content=content)
#                 comment.save()
#                 return HttpResponseRedirect('/post/' + str(pk))
#             else:
#                 return redirect(reverse('login'))
#     else:
#         form = CommentForm()
#     context['form'] = form
#     context['post'] = post
#     context['comment'] = comment
#     context['is_liked'] = is_liked
#     context['current_user'] = User
#     return render(self, 'article.html', context)
#
#
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