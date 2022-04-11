from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Author
from .forms import AuthorForm

# Create your views here.
class Book(View):
    def get(self, request):
        return render(request, 'book/book.html')


class BookController(View):
    def get(self, request):
        authorList = Author.objects.all()
        authorForm = AuthorForm
        return render(request, 'book/bookController.html', {'authorList': authorList, 'authorForm': authorForm})


class AuthorForm(View):
    def get(self, request):
        af = AuthorForm()
        return render(request, 'book/authorForm.html', {'af': af})