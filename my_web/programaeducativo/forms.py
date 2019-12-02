from django.forms import ModelForm
from .models import ProgramaEducativo

class ProgramaEducativoForm(ModelForm):
    class Meta:
        model = ProgramaEducativo
        fields = ['nombre']
