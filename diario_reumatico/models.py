from django.db import models
from paciente.models import MyUser
from django.conf import settings
from datetime import datetime    


class Humor(models.Model):
    email                           = models.ForeignKey(MyUser, on_delete=models.CASCADE)  
    dia                             = models.DateField(auto_now=True)
    sentimento_comeco_do_dia        = models.TextField(max_length=30, blank="true")
    sentimento_fim_do_dia           = models.TextField(max_length=30, blank="true")
    ansiedade                       = models.IntegerField(blank="true")



class Remedios(models.Model):
    email                           = models.ForeignKey(MyUser, on_delete=models.CASCADE)  
    dia                             = models.DateField(auto_now=True)
    nome_do_remedio                 = models.TextField(max_length=100,blank="true")
    frequencia_semanal_do_remedio   = models.TextField(max_length=100,blank="true")
    frequencia_diaria_do_remedio    = models.IntegerField(blank="true")
    horario_primeira_dose           = models.TimeField(blank="true")
    data_de_inicio                  = models.DateField(blank="true")
    dosagem                         = models.FloatField(blank="true")


class Rigidez(models.Model):
    email                           = models.ForeignKey(MyUser, on_delete=models.CASCADE)  
    dia                             = models.DateField(auto_now=True)
    rigidez_matinal                 = models.IntegerField(blank="true", default=0)

class Dor(models.Model):
    email                           = models.ForeignKey(MyUser, on_delete=models.CASCADE)  
    dia                             = models.DateField(auto_now=True)
    maos                            = models.IntegerField(blank="true", default=0)
    pes                             = models.IntegerField(blank="true", default=0)
    punhos                          = models.IntegerField(blank="true", default=0)
    cotovelos                       = models.IntegerField(blank="true", default=0)
    joelhos                         = models.IntegerField(blank="true", default=0)
    tornozelos                      = models.IntegerField(blank="true", default=0)
    ombros                          = models.IntegerField(blank="true", default=0)
    


# Create your models here.
