from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_screen_view, name='home'),
    path('async/', views.async_search_view, name='async'),
    path('sync/', views.sync_search_view, name='sync')
]
