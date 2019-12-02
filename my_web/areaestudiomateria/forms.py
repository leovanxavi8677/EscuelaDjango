from django.forms import ModelForm
from .models import AreaEstudioMateria

class AreaEstudioMateriaForm(ModelForm):
    class Meta:
        model = AreaEstudioMateria
        fields = '__all__'
