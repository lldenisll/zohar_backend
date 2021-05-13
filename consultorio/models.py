from django.db import models
from paciente.models import MyUser
from django.conf import settings
from datetime import datetime 


class Consultorio(models.Model):
    email                           = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    data_da_consulta                = models.DateField(blank="true")
    data_do_retorno                 = models.DateField(blank="true")
    nome_do_medico                  = models.TextField(max_length=30, blank="true")
    exames_solicitados              = models.TextField(max_length=30, blank="true")
    
class Exames(models.Model):
    email                           = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    exames_resultados               = models.FileField() #TODO: Procurar como fazer o fluxo dos arquivos para posterior listagem no frontend
