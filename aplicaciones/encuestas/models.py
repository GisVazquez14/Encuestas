from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.
class Preguntas(models.Model):
    pregunta_abrebiacion=models.CharField('Abrebiacion', max_length=20, default='N/A')
    pregunta_txt=models.CharField('PREGUNTA', max_length=250)
    publicacion_fecha=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.pregunta_txt
class Eleccion(models.Model):
    pregunta = models.ForeignKey(Preguntas, on_delete=models.CASCADE)
    eleccion_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    user_creo=models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    def __str__(self):
        pregunta = self.pregunta
        respuesta = self.eleccion_text
        return 'Pregunta: '+str(pregunta)+' R='+respuesta 
