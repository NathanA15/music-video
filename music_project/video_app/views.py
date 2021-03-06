from django.shortcuts import render
from video_app.models import Playlist, Video
from django.contrib.auth.decorators import login_required
from comment_app.models import Comment 
from comment_app.forms import CommentForm
from django.http import HttpResponse, JsonResponse
from profile_app.models import UserProfileInfo
from django.contrib.auth.decorators import login_required


def get_all_video_from_playlist(playlist_id):
	videos = Video.objects.filter(playlist__playlist_id = playlist_id)
	return videos


# Create your views here.
def homepage(request):

	playlists = Playlist.objects.all()
	last_videos = Video.objects.order_by('id')[0:20]
	if request.user.is_authenticated:
		user = request.user
		return render(request, 'homepage.html', context ={
				'playlists': playlists,
				'videos': last_videos,
				'logged_in':True,
				'user':user
			})
	else : 
		return render(request, 'homepage.html', context ={
				'playlists': playlists,
				'videos': last_videos,
				'logged_in':False,
			})


def playlist_page(request, playlist_id):
	print('###############')
	# playlist = Playlist.objects.get(playlist_id=playlist_id)
	playlist_videos = Video.objects.filter(playlist__playlist_id=playlist_id)
	if request.user.is_authenticated:
		user = request.user

		return render(request, 'playlist_page.html', context={'videos':playlist_videos, 'playlist': Playlist.objects.get(playlist_id=playlist_id), 'logged_in':True, 'user':user})
	else : 

		return render(request, 'playlist_page.html', context={'videos':playlist_videos, 'playlist': Playlist.objects.get(playlist_id=playlist_id), 'logged_in':False})


def index(request):
	return render(request, 'index.html')

@login_required
def get_video(request, video_id):
	user = request.user
	user_p = UserProfileInfo.objects.get(user= user)
	has_liked = False
	video = Video.objects.filter(video_id= video_id)[0]
	videos_from_playlist = get_all_video_from_playlist(video.playlist.playlist_id)
	comments = Comment.objects.filter(video=video)
	all_likes = video.liked_by.all()
	


	if user_p in all_likes:
		print('###################')
		print('###################')
		has_liked = True

	nb_likes = len(all_likes)
	print(nb_likes)
	print('###################')

	return render(request, 'video_page.html', {'video':video, 'all_videos':videos_from_playlist, 'comments':comments, 'comment_form':CommentForm, 'nb_likes':nb_likes, 'has_liked':has_liked, 'logged_in':True, 'user':user} )


@login_required
def like_video(request):
	user = request.user
	user_p = UserProfileInfo.objects.get(user=user)

	if request.method == 'POST':
		video_id = request.POST.get('video_id')
		video = Video.objects.filter(video_id= video_id)[0]
		
		has_liked = False
		all_likes = video.liked_by.all()

		if user_p in all_likes :
			video.liked_by.remove(user_p)
		else:
			video.liked_by.add(user_p)
			has_liked = True

		
		all_likes = video.liked_by.all()
		nb_likes = len(all_likes)

		response = {
			'has_liked': has_liked,
			'nb_likes':nb_likes,
			'code':200
		}

		return JsonResponse(response)

	else:
		error = {'error': 'None POST method allowed'}
		return HttpResponse(error)



def search_video(request, search):

		videos = Video.objects.filter(title__icontains = search)
		nb_results = len(videos)
		if len(videos) != 0 : 
			if request.user.is_authenticated:
				user = request.user

				return render(request, 'search_results.html', {
					'videos': videos, 
					'logged_in': True,
					'nb_results': nb_results,
					'search':search,
					})

			else :

				return render(request, 'search_results.html', {
					'videos': videos, 
					'nb_results': nb_results,
					'search':search,
					})

		else:

			if request.user.is_authenticated:
				user = request.user

				return render(request, 'search_results.html', {
					'videos': videos, 
					'logged_in': True,
					'nb_results': nb_results,
					'no_result':True,
					})

			else :

				return render(request, 'search_results.html', {
					'videos': videos, 
					'nb_results': nb_results,
					'no_result':True,
					})


def count_video_watched(request):
	if request.method == 'POST':
		print('AAAAAAAAAAAAAAAAAAAAA')
		# if not request.user.is_authenticated:
		# 	return False

		video_id = request.POST.get('video_id')
		video = Video.objects.filter(video_id=video_id)[0]
		users_views = video.users_views.all()

		if request.user.is_authenticated:
			user_profile = UserProfileInfo.objects.get(user=request.user)

			if user_profile in users_views:
				return False

			video.users_views.add(user_profile)
			video.nb_views += 1
		else:
			video.nb_views += 1

		video.save()

		response = {
			'count': video.nb_views,
		}

		return JsonResponse(response)








	
























