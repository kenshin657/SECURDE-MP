from django.shortcuts import render
from django.http import HttpResponse

from .models import *
# Create your views here.

def home(request):
    borrow = BookInstance.objects.filter(status='r')
    return render(request, 'catalog/dashboard.html', {'borrow':borrow})

def books(request):
    books = Book.objects.all()
    return render(request, 'catalog/books.html', {'books': books})
    
def authors(request):
    return render(request, 'catalog/authors.html')

def booksID(request, pk):
    book = Book.objects.get(id=pk)

    instance = BookInstance.objects.filter(book=pk)

    context = {'book':book, 'instance':instance}
    return render(request, 'catalog/bookinstance.html', context)