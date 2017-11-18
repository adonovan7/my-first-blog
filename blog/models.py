from django.db import models
from django.utils import timezone



class Post(models.Model): #creates/ defines an object named Post. models.Model indicates that its a Django Model
	author = models.ForeignKey('auth.User') #blog post author; links to other model
	title = models.CharField(max_length=200) #blog title; limits lenght
	text = models.TextField() #blog body; no limit
	created_date = models.DateTimeField(
		default=timezone.now)
	published_date = models.DateTimeField(
		blank=True, null=True)


	def publish(self): #publishing function
		self.published_date = timezone.now()
		self.save()

	def __str__(self): #example of two dunders (double underscores)
		return self.title


