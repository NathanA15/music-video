from django.urls import path
from . import views

app_name = 'video_app'

urlpatterns = [
	path('', views.homepage, name='homepage'),
	path('playlist_page/<playlist_id>/', views.playlist_page, name='playlist_page'),
]