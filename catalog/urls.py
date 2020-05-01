from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name= 'home'),
	path('books', views.books, name = 'books'),
	path('books/<str:pk>/', views.booksID, name= 'instance'),
	path('borrow/<str:pk>/', views.reserveBook, name='reserve'),
	path('return/<str:pk>/', views.returnBook, name='ret')
]