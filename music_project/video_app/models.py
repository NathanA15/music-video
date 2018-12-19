from django.db import models
from django.core.validators import URLValidator
from category_app.models import Category
from profile_app.models import UserProfileInfo

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
	# liked_by = models.ManyToManyField('UserProfileInfo', related_name='likes', blank=True)
	

	def __repr__(self):
		return '<Video {}>'.format(self.title)

	def __str__(self):
		return self.title