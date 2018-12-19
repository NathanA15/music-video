import requests
import json
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'music_project.settings')
import django
django.setup()
from video_app.models import Playlist,Video

api_key = 'AIzaSyBiqnvo8w7-EhK0lT_TxQoREtFm42nyW4o'
channel_id = 'UCupvZG-5ko_eiXAupbDfxWw'

playlists_api_url = 'https://www.googleapis.com/youtube/v3/playlists?part=snippet&channelId={}&key={}&maxResults=30'.format(channel_id,api_key,30)


def get_videos(playlist):
	
	playlist_api_url= 'https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults={}&playlistId={}&key={}'.format(20,playlist.playlist_id, api_key)
	videos = requests.get(playlist_api_url).json()

	for video in videos['items']:
		video_id = video['snippet']['resourceId']['videoId']
		title = video['snippet']['title']
		description = video['snippet']['description']
		thumbnail_url = video['snippet']['thumbnails']['default']['url']

		Video.objects.get_or_create(title= title, video_id=video_id, description=description
			, thumbnail_url=thumbnail_url, playlist=playlist)[0]
			


def get_playlists(api_url):
	videos = requests.get(api_url).json()
	
	for dic in videos['items']:
		playlist_id = dic['id']
		title = dic['snippet']['title']
		description = dic['snippet']['description']
		thumbnail_url = dic['snippet']['thumbnails']['high']['url']

		playlist = Playlist.objects.get_or_create(playlist_id=playlist_id, title=title, description=description, thumbnail_url=thumbnail_url)[0]
		get_videos(playlist)


if __name__ == '__main__':
    print('Staring to populate...')
    get_playlists(playlists_api_url)
    print('Finished populating!')

