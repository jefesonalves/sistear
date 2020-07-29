from django.db import models

class Tear(models.Model):
    descricao = models.CharField(max_length=10)

    class Meta:
        verbose_name_plural = "01 - Cadastro de Tear"
    
    def __str__(self):
        return self.descricao