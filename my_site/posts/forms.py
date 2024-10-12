# posts/forms.py
from django import forms

from .models import Post


class PostForm(forms.ModelForm): 
    
    class Meta: 
        model = Post 
        # Specify the fields to include in the form
        fields = ['title', 'content']  # Add other fields as necessary
        