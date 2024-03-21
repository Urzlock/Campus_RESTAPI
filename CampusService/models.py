from django.db import models

class Campus(models.Model):

    nombre = models.CharField(max_length=250, db_column='nombre')
    calle = models.CharField(max_length=250, db_column='calle')
    colonia = models.CharField(max_length=250, db_column='colonia')
    numexterior = models.CharField(max_length=10, db_column='numexterior')
    ciudad = models.CharField(max_length=250, db_column='ciudad')
    estado = models.CharField(max_length=250, db_column='estado')
    codigopostal = models.CharField(max_length=5, db_column='codigopostal')
    telcontacto = models.CharField(max_length=10, db_column='telcontacto')

    class Meta:
        db_table = 'Campus'
        verbose_name_plural = "Campus"           

    def __str__(self):
        return f'{self.nombre}'