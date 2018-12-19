from django.urls import path
from . import views

app_name = 'video_app'

urlpatterns = [
	path('index/', views.index, name='index'),
	path('video_page/<video_id>/', views.get_video, name='video_page'),
]