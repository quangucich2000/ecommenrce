from django.urls import path
from . import views

app_name = 'book'
urlpatterns = [
    path('', views.Book.as_view(), name='book'),
    path('bookController/', views.BookController.as_view(), name='bookController'),
    path('authorForm/', views.AuthorForm.as_view(), name='authorForm'),
]
