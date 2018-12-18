from django.shortcuts import render
from video_app.models import Playlist, Video

# Create your views here.

def index(request):
	return render(request, 'index.html')

def get_video(request, video_id):
	video = Video.objects.get(video_id= video_id)
	return render(request, 'video_page.html', {'video':video} )