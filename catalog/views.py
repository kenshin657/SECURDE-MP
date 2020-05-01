from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import F

from .models import *
# Create your views here.

def home(request, context=None):
    borrow = BookInstance.objects.filter(status='r')
    return render(request, 'catalog/dashboard.html', {'borrow':borrow})

def books(request):
    books = Book.objects.all()
    return render(request, 'catalog/books.html', {'books': books})
    

def booksID(request, pk):
    book = Book.objects.get(id=pk)

    instance = BookInstance.objects.filter(book=pk)

    context = {'book':book, 'instance':instance}
    return render(request, 'catalog/bookinstance.html', context)

def reserveBook(request, pk):
    reserve = BookInstance.objects.get(id=str(pk))

    reserve.status = 'r'
    reserve.save()

    return home(request, {'reserve':reserve})

def returnBook(request, pk):
    ret = BookInstance.objects.get(id=str(pk))

    ret.status = 'a'
    ret.due_back = None
    ret.save()

    return home(request, {'ret':ret})