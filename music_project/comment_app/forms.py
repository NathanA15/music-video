from django import forms
from comment_app.models import Comment

class CommentForm(forms.ModelForm):
	class Meta:
		model=  Comment
		fields = ['text']
		widget = {
			'title': forms.TextInput(attrs={
				'id': 'comment_text',
				'placeholder': 'text',
				'required': True,
				}),
		}