"""myblogg URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# from django.contrib import admin
# from django.contrib.auth import views as auth_views
# from django.urls import path, include
# from personal.views import (
#     home_screen_view,
# )
# from useraccount.views import (
#     registration_view,
#     logout_view,
#     login_view,
#     account_view,
# )
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('', home_screen_view, name="home"),
    # path('register/', registration_view, name="register"),
    # path('logout/', logout_view, name="logout"),
    # path('login/', login_view, name="login"),
    # path('account/', account_view, name="account"),

    re_path(r'^admin/', admin.site.urls),
    re_path(r'^', include('personal.urls')),
    # re_path(r'menu/', include('menu.urls')),
    # re_path(r'post/', include('article.urls')),
    path('account/', include('useraccount.urls')),
]
