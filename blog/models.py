from django.db import models
from django.utils import timezone



class Post(models.Model):
	author = models.ForeignKey('auth.User') #blog post author
	title = models.CharField(max_length=200) #blog title; limits lenght
	text = models.TextField() #blog body
	created_date = models.DateTimeField(
		default=timezone.now)
	published_date = models.DateTimeField(
		blank=True, null=True)


	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title
		

