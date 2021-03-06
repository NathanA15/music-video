from django.contrib.auth.models import User
from django.shortcuts import render
from profile_app.models import UserProfileInfo
from video_app.models import Video
from comment_app.models import Comment
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def write_comment(request, video_id):	
	if request.method == 'POST':
		user = request.user
		userprofileinfo = UserProfileInfo.objects.get(user=user)
		text = request.POST.get('text')
		video = Video.objects.get(video_id=video_id)
		comment = Comment(text=text, userprofileinfo = userprofileinfo, video=video)
		comment.save()

		response_data = {
			'result': 'success',
			'id': comment.id,
			'text': comment.text,
			'userprofileinfo': comment.userprofileinfo.user.username,
			'date': comment.date,
			'video': comment.video.title,
		}

		return JsonResponse(response_data)

	else:
		error = {'error': 'Non POST method not allowed'}
		return JsonResponse(error)
		