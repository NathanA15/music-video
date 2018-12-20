from django.urls import path
from . import views

app_name = 'video_app'

urlpatterns = [
	path('homepage/', views.homepage, name='homepage'),
	path('playlist_page/<playlist_id>/', views.playlist_page, name='playlist_page'),
	path('index/', views.index, name='index'),
	path('video_page/<video_id>/', views.get_video, name='video_page'),
	path('like_video/', views.like_video, name='like_video'),
	path('search_video/<search>/', views.search_video, name='search_video'),
]