from django import forms
from .models import Post

class PostsForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['mensagem', 'autor']
        widgets = {
            'mensagem': forms.TextInput(attrs={'class': 'form-control'}),
            'autor': forms.Select(attrs={'class': 'form-control'})
        }