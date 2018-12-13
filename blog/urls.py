from django.urls import path
from . import views

urlpatterns = [
    path('', views.Main, name='Main'),
    path('Cost/', views.Cost, name='Cost'),
    path('How_to_care/', views.How_to_care, name='How_to_care'),
    path('Control01/', views.Control01, name='Control01'),
    path('Control02/', views.Control02, name='Control02'),
    path('Getstarto/', views.Getstarto, name='Getstarto'),
    path('Setting01/', views.Setting01, name='Setting01'),
    path('Setting02/', views.Setting02, name='Setting02'),

    
    # path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]