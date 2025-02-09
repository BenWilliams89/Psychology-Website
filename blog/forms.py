from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'content')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Add a Title'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Add your blog content here'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

        widgets = {
    
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Add your blog content here'}),
        }