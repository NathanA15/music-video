from django.db import models
from django.core.validators import URLValidator
from category_app.models import Category

# Create your models here.

class Playlist(models.Model):
	playlist_id = models.CharField(max_length=264, unique = True)
	title = models.CharField(max_length=400)
	description = models.CharField(max_length=1000)
	thumbnail_url = models.CharField(max_length=2000, validators=[URLValidator()])

	def __repr__(self):
		return '<Playlist {}>'.format(self.title)

	def __str__(self):
		return self.title


class Video(models.Model):
	title = models.CharField(max_length=400)
	video_id = models.CharField(max_length=400, unique=False)
	description = models.CharField(max_length=2000)
	thumbnail_url = models.CharField(max_length=2000, validators=[URLValidator()])
	playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)
	

	def __repr__(self):
		return '<Video {}>'.format(self.title)

	def __str__(self):
		return self.title