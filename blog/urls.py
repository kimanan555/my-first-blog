from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_first, name='post_first'),
    path('cost/', views.post_detail, name='post_detail'),
    path('care/', views.post_new, name='post_new'),
    # path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]