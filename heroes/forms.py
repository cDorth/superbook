from django import forms
from .models import Hero

class ContatoForm(forms.Form):
    nome = forms.CharField(max_length=100, required=True, label="Seu nome")
    email = forms.EmailField(required=True, label="E-mail")
    mensagem = forms.CharField(widget=forms.Textarea, required=True)

class HeroForm(forms.ModelForm):
    class Meta:
        model = Hero
        fields = ['codinome', 'nome_real', 'poder_principal', 'cidade', 'historia']
        widgets = {
            'codinome': forms.TextInput(attrs={'class': 'form-control'}),
            'nome_real': forms.TextInput(attrs={'class': 'form-control'}),
            'poder_principal': forms.TextInput(attrs={'class': 'form-control'}),
            'cidade': forms.TextInput(attrs={'class': 'form-control'}),
            'historia': forms.Textarea(attrs={'class': 'form-control'}),
        }

    