from django import forms
from aplicaciones.encuestas.models import Eleccion, Preguntas

class PreguntaForm(forms.ModelForm):
    class Meta:
        model = Preguntas
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super(PreguntaForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
class EleccionForm(forms.ModelForm):
    class Meta:
        model = Eleccion
        fields = ('pregunta', 'eleccion_text', 'votes')
    def __init__(self, *args, **kwargs):
        super(EleccionForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})