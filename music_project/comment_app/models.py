from django.db import models
from profile_app.models import UserProfileInfo
from video_app.models import Video
from datetime import datetime

# Create your models here.

class Comment(models.Model):
	userprofileinfo = models.ForeignKey(UserProfileInfo, on_delete=models.CASCADE)
	text = models.TextField()
	date = models.DateTimeField(default=datetime.now())
	video = models.ForeignKey(Video, on_delete=models.CASCADE)


	def __repr__(self):
		return "<Comment of {}>".format(self.userprofileinfo.user.username)

	def __str__(self):
		return "{}".format(self.userprofileinfo.user.username)
