from django.contrib.auth.models import User
from profile_app.models import UserProfileInfo
from rest_framework import serializers



class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')


class UserProfileInfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserProfileInfo
        fields = ('user', 'bio', 'profile_pic')