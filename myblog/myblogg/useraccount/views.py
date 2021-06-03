from django.contrib.auth import get_user_model
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.shortcuts import render, redirect, reverse
from .forms import CustomUserCreationForm, DeleteAccountForm, UserInfoForm, UpdatePictureForm
from article.models import BlogPost
User = get_user_model()


def registration_view(request):
    context = {}
    if request.POST:
        form = CustomUserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            form = CustomUserCreationForm
            context['form'] = form
    else:
        form = CustomUserCreationForm
        context['form'] = form
    messages.success(request, 'Successfully registered')
    return render(request, 'useraccount/register.html', context)


def logout_view(request):
    logout(request)
    messages.success(request, 'Logged out')
    return redirect('home')


def login_view(request):
    context = {}
    if request.POST:
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm
    context['form'] = form
    return render(request, 'useraccount/login.html', context)


def account_view(request):
    context = {}
    if request.POST:
        delete_form = DeleteAccountForm(data=request.POST)
        if delete_form.is_valid():
            user = User.objects.filter(email=delete_form.clean_email())
            if user[0].email == request.user.email:
                user.delete()
                return redirect(reverse('home'))

        blog_posts = BlogPost.objects.filter(author=request.user)
        context['blog_posts'] = blog_posts
        context['delete_form'] = delete_form
        context['user'] = request.user
        return render(request, 'useraccount/useraccount.html', context)
    else:
        delete_form = DeleteAccountForm
        form = UserInfoForm(
            initial={
                'username': request.user.username,
                'email': request.user.email,
                'first_name': request.user.first_name,
                'last_name': request.user.last_name
            }
        )

        form.set_placeholders()
        user = request.user
        picture_form = UpdatePictureForm
        context['delete_form'] = delete_form
        context['user'] = request.user
        context['form'] = form
        context['picture_form'] = picture_form
        return render(request, 'useraccount/useraccount.html', context)


def change_avatar(request):
    context = {}
    if request.POST:
        user = User.objects.get(id=request.user.id)
        update_picture_form = UpdatePictureForm(data=request.POST, files=request.FILES)
        if update_picture_form.is_valid():
            picture = request.FILES['picture']
            print(picture.size)
            print(picture.name)
            user.picture = picture
            print(user.picture)
            user.save()
            messages.success(request, 'Done')
    context['user'] = request.user
    return redirect(reverse('useraccount'), 'useraccount/useraccount.html', context)


def save_changes(request):
    context = {}
    if request.POST:
        user_info_form = UserInfoForm(data=request.POST)
        if user_info_form.is_valid():
            username = user_info_form.get_username(request)
            email = user_info_form.get_email(request)
            first_name = user_info_form.get_first_name()
            last_name = user_info_form.get_last_name()
            user = User.objects.get(id=request.user.id)
            user.first_name = first_name
            user.last_name = last_name
            user.username = username
            user.email = email
            user.save()
            messages.success(request, 'Done')
    context['user'] = request.user
    return redirect(reverse('account'), 'registration/account.html', context)


def must_authenticate_view(request):
    messages.error(request, 'You must be authenticated')
    return render(request, 'useraccount/must_authenticate.html', {})