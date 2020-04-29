from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name= 'home'),
	path('books', views.books, name = 'books'),
	path('author', views.authors),
	path('books/<str:pk>/', views.booksID, name= 'instance')
]