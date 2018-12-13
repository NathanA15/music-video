from django.db import models
from django.core.validators import URLValidator
from category_app.models import Category

# Create your models here.

class Video(models.Model):
	title = models.CharField(max_length=400)
	url = models.CharField(max_length=2000, validators=[URLValidator()])
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
