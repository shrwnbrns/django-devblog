from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body'] # We omit 'author' because the view will automatically set it to the logged-in user.