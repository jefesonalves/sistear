from django.db import models
from apps.evento.models import Evento
from apps.tear.models import Tear
from apps.eficiencia.models import Eficiencia

class Lancamentos(models.Model):
    tear = models.ForeignKey(Tear, null=False, blank=False, on_delete=models.PROTECT)
    eficiencia = models.ForeignKey(Eficiencia, null=False, blank=False, on_delete=models.PROTECT)
    evento = models.ForeignKey(Evento, null=False, blank=False, on_delete=models.PROTECT)    

    class Meta:
        verbose_name_plural = '01 - Lançamentos'