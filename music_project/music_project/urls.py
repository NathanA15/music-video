"""music_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from profile_app import views
from video_app import views
from login_app import views
from comment_app import views
from category_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('profile_app/', include('profile_app.urls')),
    path('video_app/', include('video_app.urls')),
    path('login_app/', include('login_app.urls')),
    path('comment_app/', include('comment_app.urls')),
    path('category_app/', include('profile_app.urls')),

]
