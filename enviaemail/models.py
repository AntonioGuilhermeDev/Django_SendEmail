from django.db import models

# Create your models here.

class ROs(models.Model):
    id = models.IntegerField(primary_key=True, null=False)
    data_criacao = models.DateField()
    data_vencimento = models.DateField()