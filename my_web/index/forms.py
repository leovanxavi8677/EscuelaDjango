from django import forms

class IndexForm(forms.Form):
    usuario = forms.CharField(label="Usuario", max_length=50, required=True)
    password = forms.CharField(widget=forms.PasswordInput(),
                               error_messages={'required': 'Por Favor ingrese contraseña'})

