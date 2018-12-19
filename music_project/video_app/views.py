from django.shortcuts import render
from video_app.models import Playlist, Video
from comment_app.models import Comment 
from comment_app.forms import CommentForm

# Create your views here.

def index(request):
	return render(request, 'index.html')

def get_video(request, video_id):
	video = Video.objects.get(video_id= video_id)
	comments = Comment.objects.filter(video=video)

	return render(request, 'video_page.html', {'video':video, 'comments':comments, 'comment_form':CommentForm } )