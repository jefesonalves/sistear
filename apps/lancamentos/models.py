from django.db import models
from apps.evento.models import Evento
from apps.tear.models import Tear
from apps.eficiencia.models import Eficiencia

class Lancamentos(models.Model):
    data = models.DateField(null=True)
    hora = models.TimeField(null=True)
    tear = models.ForeignKey(Tear, null=False, blank=False, on_delete=models.PROTECT)
    eficiencia = models.ForeignKey(Eficiencia, null=False, blank=False, on_delete=models.PROTECT)
    evento = models.ForeignKey(Evento, null=False, blank=False, on_delete=models.PROTECT)   

    class Meta:
        verbose_name_plural = "01 - Lançamentos"
    
    def __str__(self):
        return self.tear.descricao + " " + self.eficiencia.descricao + " " + self.evento.descricao