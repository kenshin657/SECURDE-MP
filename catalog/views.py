from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'catalog/dashboard.html')

def books(request):
    return render(request, 'catalog/books.html')
    
def authors(request):
    return render(request, 'catalog/authors.html')