from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('snes/', views.snes, name='snes'),
    path('neogeo/', views.neogeo, name='neogeo'),
]
