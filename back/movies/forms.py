from django import forms
from .models import Review, Comment

from django_summernote.widgets import SummernoteWidget

class ReviewForm(forms.ModelForm):
    
    class Meta:
        model = Review
        fields = ['title', 'movie_title', 'rank', 'content']


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        exclude = ['review', 'user']

class PostForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['title', 'movie_title', 'rank', 'content']
        widgets = {
            'content': SummernoteWidget(),
        }