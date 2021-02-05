from django import forms
from .models import Article

class ArticleCreationForm(forms.ModelForm):

    title = forms.CharField(label="", widget=forms.TextInput(attrs={
        'class':'form-control form-control-style-3',
        'placeholder':'Article Title...',
    }))

    content = forms.CharField(label="", widget=forms.Textarea(attrs={
        'class':'form-control form-control-style-3',
        'placeholder':'Article Content...',
        'rows':'8',
        'cols':'80',
    }))

    class Meta:
        model = Article
        fields = ['title', 'content']
