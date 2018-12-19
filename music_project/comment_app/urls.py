from django.urls import path
from . import views

app_name = 'comment_app'

urlpatterns = [
	path('write_comment/<video_id>', views.write_comment, name='write_comment'),
]