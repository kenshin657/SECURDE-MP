from django.db import models

# Create your models here.
class Language(models.Model):
	lang = models.CharField(max_length=200, help_text='Enter the book language')
	
	def __str__(self):
		return self.lang

class Genre(models.Model):
	"""Model representing a book genre."""
	name = models.CharField(max_length=200, help_text='Enter a book genre (e.g. Science Fiction)')
	
	def __str__(self):
		"""String for representing the Model Object."""
		return self.name
        

class Publisher(models.Model):
	publisher = models.CharField(max_length=200, help_text='Enter Book\'s Publisher')

	def __str__(self):
		return self.publisher

from django.urls import reverse
	
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null = True)
    summary = models.TextField(max_length=1000, help_text='Enter a brief description of the book')
    isbn = models.CharField('ISBN', max_length=13, help_text='13 Character ISBN Number')
    review = models.TextField(max_length=1000, help_text='Give the book a review', null = True, blank=True)
    publisher = models.ForeignKey('Publisher', on_delete=models.SET_NULL, null=True, blank = True)
    yearPub = models.DateField(null=True, )

    def __str__(self):
        return self.title	


import uuid

class BookInstance(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID')
	book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
	due_back = models.DateField(null=True, blank=True)
	
	LOAN_STATUS = (('a', 'Available'),
		('r', 'Reserved'),)
	
	status = models.CharField(max_length=1,
		choices= LOAN_STATUS,
		blank = True,
		default = 'm',
		help_text = 'Book Availability',)
	
	class Meta:
		ordering = ['due_back']
		
	def __str__(self):
		return f'{self.id} ({self.book.title})'
	
class Author(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	date_of_birth = models.DateField(null = True, blank = True)
	date_of_death = models.DateField('Died', null=True, blank=True)
	
	class Meta:
		ordering = ['last_name', 'first_name']
		
	def __str__(self):
		return f'{self.last_name}, {self.first_name}'

