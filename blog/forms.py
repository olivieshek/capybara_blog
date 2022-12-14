from django import forms
from .models import Post
from django.contrib.auth.forms import AuthenticationForm


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.DateInput(attrs={'type': 'time'})
        }


class AuthenticateForm(AuthenticationForm):
    """
    A form that creates a user, with no privileges, from the given username and
    password.
    """
    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput
    )
