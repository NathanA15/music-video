import requests
import json
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'music_project.settings')
import django
django.setup()
from video_app.models import Playlist, Video


api_key = 'AIzaSyCbLgG1oFkY730Hflt84-i_Uv7P-5VOUuw'
channel_id = 'UCPVhZsC2od1xjGhgEc2NEPQ'
playlists_api_url =  'https://www.googleapis.com/youtube/v3/search?key={}&channelId={}&part=snippet,id&order=date&maxResults={}'.format(api_key, channel_id, 20)

def get_videos(playlist):
	playlist_api_url = 'https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults={}&playlistId={}&key={}'.format(20, playlist.playlist_id, api_key)
	videos = requests.get(playlist_api_url).json()
	for video in videos['items']:
		video_id = video['id']
		video_info = video['snippet']
		title = video_info['title']
		description = video_info['description']
		thumbnail_url = video_info['thumbnails']['default']['url']

		Video.objects.get_or_create(video_id=video_id, title=title, 
			description=description, thumbnail_url=thumbnail_url, playlist=playlist)[0]


def get_playlists(playlists_api_url):
	videos = requests.get(playlists_api_url).json()
	item_dict = videos['items']

	for playlist_dict in item_dict:
		playlist = playlist_dict['snippet']
		if playlist_dict['id']['playlistId']:
			playlist_id = playlist_dict['id']['playlistId']
			title = playlist['title']
			description = playlist['description']
			thumbnail_url = playlist['thumbnails']['default']['url']
	
			playlist = Playlist.objects.get_or_create(playlist_id=playlist_id, title=title, description=description,thumbnail_url=thumbnail_url)[0]
			
			get_videos(playlist)

if __name__ == '__main__':
    print('Staring to populate...')
    get_playlists(playlists_api_url)
    print('Finished populating!')


   




