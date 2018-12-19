from django.shortcuts import render
from video_app.models import Playlist, Video
from comment_app.models import Comment 
from comment_app.forms import CommentForm


def get_all_video_from_playlist(playlist_id):
	videos = Video.objects.filter(playlist__playlist_id = playlist_id)
	return videos

# Create your views here.

def index(request):
	return render(request, 'index.html')

def get_video(request, video_id):
	video = Video.objects.get(video_id= video_id)
	videos_from_playlist = get_all_video_from_playlist(video.playlist.playlist_id)
	comments = Comment.objects.filter(video=video)

	return render(request, 'video_page.html', {'video':video, 'all_videos':videos_from_playlist, 'comments':comments, 'comment_form':CommentForm} )
