
from django.db import models
import uuid
from django.contrib.auth.models import User

# Create your models here.
class Events(models.Model):
	title = models.CharField(max_length=100)
	location = models.CharField(max_length=100)
	eventDate = models.DateField()
	eventTime = models.TimeField()
	upvotes = models.IntegerField()
	description = models.CharField(max_length=3000)
	image = models.CharField(max_length=500)
	timestamp = models.DateField(auto_now_add=True)
	byUser = models.ForeignKey(User, on_delete=models.CASCADE)
	tags = models.ManyToManyField("Tags")

	def __str__(self):
		return self.title

class Tags(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name

class Comments(models.Model):
	name = models.CharField(max_length=500)
	forEvent = models.ForeignKey(Events, on_delete=models.CASCADE)
	byUser = models.ForeignKey(User, on_delete=models.CASCADE)
	timestamp = models.DateField(auto_now_add=True)
	#timestamp = models.DateField(default=0)

	def __str__(self):
		return self.name
