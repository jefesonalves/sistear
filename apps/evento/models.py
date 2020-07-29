from django.db import models

class Evento(models.Model):
    descricao = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = '01 - Cadastro de Evento'
    
    def __str__(self):
        return self.descricao
