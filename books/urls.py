from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='books-home'),
    path('search/', views.searchBook, name='books-search'),
    path('add/', views.addBook, name='books-add'),
    path('update/', views.updateInfo, name='books-update'),
]
