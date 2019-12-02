from django.forms import ModelForm
from .models import AreaMaestro

class AreaMaestroForm(ModelForm):
    class Meta:
        model = AreaMaestro
        fields = ['area']
