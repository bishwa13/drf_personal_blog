from django.urls import path
from . import views
from .views import post_create

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('create/', post_create, name='post_create'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
]
