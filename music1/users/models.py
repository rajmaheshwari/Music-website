from django.db import models

class User(models.Model):
	name = models.CharField(max_length=50)
	email = models.EmailField(max_length=100)
	username = models.CharField(max_length=30)
	password = models.CharField(max_length=300)
	# picture = models.ImageField(upload_to = 'static/users/images/user_pictures/', default = 'static/users/images/user_pictures/Unknown-3.png')

	def __str__(self):
		return self.name