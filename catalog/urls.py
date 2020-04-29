from django.urls import path
from . import views

urlpatterns = [
	path('', views.home),
	path('books', views.books),
	path('author', views.authors),
]