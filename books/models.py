from django.db import models
# Create your models here.

class Publisher(models.Model):
	name = models.CharField(max_length=30)
	address = models.CharField(max_length=50)
	city = models.CharField(max_length=30)
	state_province = models.CharField(max_length=30)
	contry = models.CharField(max_length=50)
	website = models.URLField()

#tabla mucho a muchos
class Author(models.Model):
	salutation = models.CharField(max_length=30)
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=30)
	email = models.CharField(max_length=50)
	#headshot = models.ImageField(upload_to='/tmp')

class Book(models.Model):
	title = models.CharField(max_length=100)
	authors = models.ManyToManyField(Author)
	publisher = models.ForeignKey(Publisher)
	publication_date = models.DateField()
