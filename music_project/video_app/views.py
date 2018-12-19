from django.shortcuts import render
from video_app.models import Playlist, Video
from django.contrib.auth.decorators import login_required


# Create your views here.
def homepage(request):
	playlists = Playlist.objects.all()
	last_videos = Video.objects.order_by('id')[0:20]

	return render(request, 'homepage.html', context ={
			'playlists': playlists,
			'videos': last_videos
		})


def playlist_page(request, playlist_id):
	print('###############')
	# playlist = Playlist.objects.get(playlist_id=playlist_id)
	playlist_videos = Video.objects.filter(playlist__playlist_id=playlist_id)

	return render(request, 'playlist_page.html', context={'videos':playlist_videos, 'playlist': Playlist.objects.get(playlist_id=playlist_id)})