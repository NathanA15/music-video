from video_app.models import Video
from rest_framework import serializers
from profile_app.serializers import UserSerializer, UserProfileInfoSerializer


class PlaylistSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Playlist
		fields = ('playlist_id', 'title', 'description', 'thumbnail_url' )

		

class VideoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Video
        fields = ('title', 'video_id', 'description', 'playlist', 'liked_by')

