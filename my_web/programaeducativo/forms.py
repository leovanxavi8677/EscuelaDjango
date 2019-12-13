from django.forms import ModelForm
from .models import ProgramaEducativo
from django.forms.widgets import TextInput, Select, SelectMultiple, NumberInput


class ProgramaEducativoForm(ModelForm):
    class Meta:
        model = ProgramaEducativo
        fields = ['nombre']
        required = ['nombre']
        widgets = {
            'nombre': TextInput(attrs={
                'class': 'txt_nombre',
                'id': 'txt_nomnbre',
                'name': 'txt_nombre',
                'onKeyPress': 'return ValidateAlpha(event);',

            }),
        }
