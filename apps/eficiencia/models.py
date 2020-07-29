from django.db import models

class Eficiencia(models.Model):
    descricao = models.CharField(max_length=10)

    class Meta:
        verbose_name_plural = "01 - Cadastro de Eficência"
    
    def __str__(self):
        return self.descricao