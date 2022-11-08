from django import forms
from django.contrib.auth.models import User

from .models import Director, Film
from django.core.exceptions import ValidationError


class DirectorForm(forms.ModelForm):
    class Meta:
        model = Director
        fields = 'name '.split()

    def clean_name(self):
        name = self.cleaned_data['name']
        if Director.objects.filter(name=name):
            raise ValidationError('name ALREADY EXISTS')
        return name


class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = '__all__'

    def clean_title(self):
        title = self.cleaned_data['title']
        if Film.objects.filter(title=title):
            raise ValidationError('TITLE ALREADY EXISTS')
        return title


class UserCreateForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
    password1 = forms.CharField(widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username):
            raise ValidationError("User with tis name already exist")
        return username

    def clean_password1(self):
        password = self.cleaned_data['password']
        password1 = self.cleaned_data['password1']
        if password != password1:
            raise ValidationError("Password does not match")
        return password1


class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
