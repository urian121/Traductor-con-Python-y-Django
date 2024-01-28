from django.db import models


class Idioma(models.Model):
    idIdioma = models.AutoField(primary_key=True, db_column='idIdioma')
    prefijo = models.CharField(max_length=5, db_column='prefijo')
    idioma = models.CharField(max_length=50, db_column='idioma')

    class Meta:
        db_table = 'tbl_idiomas'
