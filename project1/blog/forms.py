from django import forms
from django.forms import ModelForm
from .models import Blog

class CreateForm(ModelForm):
    class Meta:
        model = Blog
        labels = {
            'Title': 'Blog title',
            'content': 'Blog Content',
            'Tag': 'Tags'
        }
        fields = ['Title', 'content', 'Tag']
        widgets = {
            'Title': forms.TextInput(attrs={'class':'form-control'}),
            'Tag': forms.Select(attrs={'class':'form-control'})
        }
    # email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))