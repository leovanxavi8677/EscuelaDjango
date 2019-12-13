from django.forms import ModelForm
from .models import AreaMaestro
from django.forms.widgets import TextInput

class AreaMaestroForm(ModelForm):
    class Meta:
        model = AreaMaestro
        fields = ['area']
        required = ['area']

        widgets = {
            'area': TextInput(attrs={
                'class': 'txt_area',
                'id': 'txt_area',
                'name': 'txt_area',
                'onKeyPress': 'return ValidateAlpha(event);',
            })
        }
