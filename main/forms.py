from django import forms
from .models import Director, Film
from django.core.exceptions import ValidationError

class DirectorForm(forms.ModelForm):
    class Meta:
        model = Director
        fields = 'name'.split()

    def clean_name(self):
        name = self.cleaned_data['name']
        if Director.objects.filter(name=name).count() > 0:
            raise ValidationError('name ALREADY EXISTS')
        return name

class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = '__all__'

    def clean_title(self):
        title = self.cleaned_data['title']
        if Film.objects.filter(title=title).count() > 0:
            raise ValidationError('TITLE ALREADY EXISTS')
        return title
