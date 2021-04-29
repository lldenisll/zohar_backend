from django.db import models

class Humor(models.Model):
    dia                             = models.DateField(primary_key=True,auto_now=True)
    sentimento_comeco_do_dia        = models.TextField(max_length=30, blank="true")
    sentimento_fim_do_dia           = models.TextField(max_length=30, blank="true")
    ansiedade                       = models.IntegerField(blank="true", default=0)



class Remedios(models.Model):
    dia                             = models.DateField(primary_key=True,auto_now=True)
    nome_do_remedio                 = models.TextField(max_length=100,blank="true")
    frequencia_semanal_do_remedio   = models.TextField(max_length=100,blank="true")
    frequencia_diaria_do_remedio    = models.IntegerField(blank="true", default=0)
    horario_primeira_dose           = models.TimeField(blank="true")


class Rigidez(models.Model):
    dia                             = models.DateField(primary_key=True,auto_now=True)
    rigidez_matinal                 = models.IntegerField(blank="true", default=0)

class Dor(models.Model):
    dia                             = models.DateField(primary_key=True,auto_now=True)
    maos                            = models.IntegerField(blank="true", default=0)
    pes                             = models.IntegerField(blank="true", default=0)
    punhos                          = models.IntegerField(blank="true", default=0)
    cotovelos                       = models.IntegerField(blank="true", default=0)
    joelhos                         = models.IntegerField(blank="true", default=0)
    tornozelos                      = models.IntegerField(blank="true", default=0)
    ombros                          = models.IntegerField(blank="true", default=0)
    


# Create your models here.
