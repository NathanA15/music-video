from django import forms
from django.core import validators
from django.contrib.auth.models import User
from profile_app.models import UserProfileInfo
from datetime import datetime


class UserForm(forms.ModelForm):
	password = forms.CharField(widget= forms.PasswordInput)
	class Meta:
		model = User
		fields = ('first_name','last_name', 'username', 'email', 'password')


class UserProfileInfoForm(forms.ModelForm):
	birth_date = forms.DateField(widget = forms.SelectDateWidget(years=range(datetime.now().year - 60, datetime.now().year)))
	class Meta:
		model = UserProfileInfo
		fields = ('birth_date','bio', 'profile_pic')


class LoginForm(forms.Form):
	username = forms.CharField(max_length=150)
	password = forms.CharField(widget=forms.PasswordInput())
	def clean(self):
		all_clean_data = super().clean()
		return all_clean_data