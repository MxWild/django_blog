from django import forms
from django.contrib.auth.forms import UserCreationForm

from account.models import Profile


class ProfileForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'type': 'text',
            'placeholder': 'Username: '
        }
    ))

    email = forms.EmailField(widget=forms.TextInput(
        attrs={
            'type': 'email',
            'placeholder': 'Email: '
        }
    ))

    class Meta:
        model = Profile
        fields = ('username', 'email', 'avatar',)
