from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('snes/', views.snes),
    path('neogeo/', views.neogeo),
]
