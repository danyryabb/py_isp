import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myblogg.settings')
import django
django.setup()

from article.models import BlogPost
from useraccount.models import Account
from useraccount.forms import CustomUserCreationForm, UpdatePictureForm, DeleteAccountForm, UserInfoForm
from article.views import create_blog_view
from article.forms import CreateBlogPostForm, UpdateBlogPostForm
from useraccount.views import registration_view, login_view, account_view, must_authenticate_view
from personal.views import home_screen_view
from unittest import mock
from django.test import RequestFactory
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from PIL import Image
from django.core.files.base import File
from io import BytesIO
from django.contrib.messages.storage.fallback import FallbackStorage
import pytest
from django.test import Client


User = get_user_model()
acc = Account.objects.get(id=1)


def test_first_name_label():
    first_name_label = acc._meta.get_field('first_name').verbose_name
    print(first_name_label)
    assert first_name_label == 'first name'

def test_email_label():
    email_label = acc._meta.get_field('email').verbose_name
    assert email_label == 'email'

def test_email_equals():
    email_label = acc.email
    assert email_label == 'ryaby01@mail.ru'

def test_username_max_length():
    max_length = acc._meta.get_field('username').max_length
    assert max_length == 30

def test_object_name_is_username():
    expected_object_name = f'{acc.username}'
    assert str(acc) == expected_object_name

def test_post_name_is_title():
    expected_object_name = BlogPost(title="title", body="body", image=get_image_file1, date_published="31/05/2021", author=acc).__str__()
    assert expected_object_name == 'title'

def test_acc_manager_user():
    test_user = User.objects.create_user('user22', 'user22@mail.ru', 'qwaszx12')
    assert test_user.username == 'user22'

def test_acc_manager_superuser():
    test_user = User.objects.create_superuser('user21', 'user21@mail.ru', 'qwaszx12')
    assert test_user.email == 'user21@mail.ru'

def test_user_create_form():
    form = CustomUserCreationForm()
    assert form.fields['email'].label == 'Enter Email'
    assert form.fields['username'].label == 'Enter Username'
    assert form.fields['password1'].label == 'Enter password'
    assert form.fields['password2'].label == 'Confirm password'

def test_user_info_form():
    form = UserInfoForm()
    assert form.fields['email'].label == 'Enter Email'
    assert form.fields['username'].label == 'Enter Username'
    assert form.fields['first_name'].label == 'Enter First Name'
    assert form.fields['last_name'].label == 'Enter Last Name'

def test_user_info_form_is_valid():
    form = UserInfoForm(data={
        'email': 'gang@mail.ru',
        'username': 'test_user_gang',
        'first_name': 'bulba',
        'last_name': 'gnilaya'
    })
    assert form.is_valid() == True

def test_update_pic_form():
    form = UpdatePictureForm()
    assert form.fields['picture'].label == 'Select a picture'

def test_delete_user_form():
    form = DeleteAccountForm()
    assert form.fields['email'].label == 'Enter email'

def test_user_create_form_is_valid():
    form = CustomUserCreationForm(data={
        'email': 'gang@mail.ru',
        'username': 'test_user_gang',
        'password1': 'qwaszx12',
        'password2': 'qwaszx12'
    })
    assert form.is_valid() == True

def test_article_create_form_is_valid():
    form = CreateBlogPostForm(
        data={
            'title': 'title',
            'body': 'body',
            'image': get_image_file1
        }
    )
    assert form.is_valid() == True

def test_article_update_form_is_valid():
    form = UpdateBlogPostForm(
        data={
            'title': 'new_title',
            'body': 'new_body',
            'image': get_image_file1
        }
    )
    assert form.is_valid() == True

def test_response_from_base_view():
    factory = RequestFactory()
    request = factory.get('')
    request.user = acc
    response = home_screen_view(request)
    assert response.status_code == 200

# def test_home_view_pag():
#     factory = RequestFactory()
#     request = factory.get('')
#     request.user = acc
#     response = home_screen_view(request)
#     assert response == render(request, "personal/home.html", context)

def test_response_from_create_blog_view():
    factory = RequestFactory()
    request = factory.get('/create/')
    request.user = acc
    response = create_blog_view(request)
    assert response.status_code == 200

def test_response_from_must_auth_view():
    factory = RequestFactory()
    request = factory.get('/must_authenticate/')
    response = must_authenticate_view(request)
    assert response.status_code == 200

def test_response_from_account_view():
    factory = RequestFactory()
    request = factory.get('/account/')
    request.user = acc
    response = account_view(request)
    assert response.status_code == 200

def test_response_from_registration_view():
    factory = RequestFactory()
    request = factory.get('/register/')
    request.user = acc
    response = registration_view(request)
    assert response.status_code == 200

def test_login_get_view():
    factory = RequestFactory()
    request = factory.get('/login/')
    request.user = acc
    response = login_view(request)
    assert response.status_code == 200

def test_login_post_view():
    c = Client()
    response = c.post('/account/login/', {'username': 'duracell', 'password': 'qwaszx12'})
    assert response.status_code == 302

@pytest.fixture
def get_image_file1():
    name = 'me.jpg'
    ext = 'jpeg'
    size = (700, 700)
    color = (256, 0, 0)
    file_obj = BytesIO()
    image = Image.new("RGB", size=size, color=color)
    image.save(file_obj, ext)
    file_obj.seek(0)
    return File(file_obj, name=name)

@pytest.fixture
def user():
    user = User.objects.create(username='user14', email='user14@mail.ru', password="qwaszx12")
    return user

@pytest.fixture
def blog_post(get_image_file1, user):
    image = get_image_file1
    blog_post = BlogPost(
        title="title",
        body="body",
        image=image,
        date_published="01/06/2021",
        slug='new_test_slug',
        author=acc
    )
    return blog_post



@pytest.mark.parametrize("expected", [302, ''])
def test_registration_post_view(expected):
    c = Client()
    response = c.post('/account/register/', {
        'username': 'bulbash', 'email': 'testmail54@mail.ru', 'password1': 'qwaszx12', 'password2': 'qwaszx12'
    })
    assert response.status_code, response.url == expected

@pytest.mark.parametrize("expected", [302, ''])
def test_blog_add_post_view(expected):
    c = Client()
    image = get_image_file1
    response = c.post('/post/create/', {
        'title': 'new_title',
        'body': 'new_body',
        'image': image,
    })
    assert response.status_code, response.url == expected



