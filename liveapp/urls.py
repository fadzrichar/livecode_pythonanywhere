from django.contrib import admin
from django.urls import path
from . import views

app_name = 'liveapp'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('product/<int:product_id>/', views.detail, name='detail'),
    
]