from django.forms import ModelForm
from .models import AreaEstudioMateria
from django.forms.widgets import TextInput


class AreaEstudioMateriaForm(ModelForm):
    class Meta:
        model = AreaEstudioMateria
        fields = '__all__'

        required = ['area']

        widgets = {
            'area': TextInput(attrs={
                'class': 'txt_area',
                'id': 'txt_area',
                'name': 'txt_area',
                'onKeyPress': 'return ValidateAlpha(event);',

            })
        }
