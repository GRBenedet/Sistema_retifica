from django import forms
from .models import clientes, pecas, servicos, motor, orcamentos
from django.contrib.admin.widgets import FilteredSelectMultiple


class ClientesForm(forms.ModelForm):
    class Meta:
        model = clientes
        fields = '__all__'
        label  = {'__all__': ''}
        widgets = {'__all__': forms.Textarea(attrs={'cols':20})}

class PecasForm(forms.ModelForm):
    class Meta:
        model = pecas
        fields = '__all__'
        label = {'__all__': ''}
        widgets = {'__all__': forms.Textarea(attrs={'cols':20})}

class ServicosForm(forms.ModelForm):
    class Meta:
        model = servicos
        fields = '__all__'
        label = {'__all__': ''}
        widgets = {'__all__': forms.Textarea(attrs={'cols':20})}

class MotorForm(forms.ModelForm):
    class Meta:
        model = motor
        fields = '__all__'
        label = {'__all__': ''}
        widgets = {'__all__': forms.Textarea(attrs={'cols':20})}

class OrcForm(forms.ModelForm):
    class Meta:
        model = orcamentos
        fields = '__all__'
        label = {'__all__': ''}
        widgets = {'__all__': forms.Textarea(attrs={'cols':80})}