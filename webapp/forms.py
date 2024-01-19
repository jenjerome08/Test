from django.forms import ModelForm
from .models import Musician

class MusicianForm(ModelForm):
    class Meta:
        model = Musician
        fields = '__all__'