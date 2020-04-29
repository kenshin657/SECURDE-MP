from django.shortcuts import render
from django.http import HttpResponse

from .models import *
# Create your views here.

def home(request):
    borrow = BookInstance.objects.filter(status='r')
    return render(request, 'catalog/dashboard.html', {'borrow':borrow})

def books(request):
    books = BookInstance.objects.all()
    return render(request, 'catalog/books.html', {'books': books})
    
def authors(request):
    return render(request, 'catalog/authors.html')