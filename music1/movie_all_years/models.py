from django.db import models

def loc(self):
	BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
	loc = os.path.join(BASE_DIR, 'Media/Songs/Year_2011')
	return loc

class Movie(models.Model):
	name = models.CharField(max_length=100)
	year = models.IntegerField()

	def __str__(self):
		return self.name

class Song(models.Model):
	name = models.CharField(max_length=100)
	movie = models.ForeignKey(Movie, null=True)

	def __str__(self):
		return self.name