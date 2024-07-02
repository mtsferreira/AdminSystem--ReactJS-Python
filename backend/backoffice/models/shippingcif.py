from django.db import models


class FreteCif(models.Model):
    idfretecif = models.AutoField(db_column='IDFreteCIF', primary_key=True)  # Field name made lowercase.
    desfretecif = models.CharField(db_column='DesFreteCIF', max_length=40, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    perdesconto1 = models.DecimalField(db_column='PerDesconto1', max_digits=4, decimal_places=2)  # Field name made lowercase.
    perdesconto2 = models.DecimalField(db_column='PerDesconto2', max_digits=4, decimal_places=2)  # Field name made lowercase.
    datainicial = models.DateField(db_column='DataInicial')  # Field name made lowercase.
    datafinal = models.DateField(db_column='DataFinal')  # Field name made lowercase.
    situacao = models.CharField(db_column='Situacao', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FreteCIF'


class FreteUf(models.Model):
    idfreteuf = models.AutoField(db_column='IDFreteUF', primary_key=True)  # Field name made lowercase.
    idfretecif = models.ForeignKey('Fretecif', models.DO_NOTHING, db_column='IDFreteCIF')  # Field name made lowercase.
    uforigem = models.CharField(db_column='UFOrigem', max_length=2, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    codibgeorigem = models.ForeignKey('Cidade', models.DO_NOTHING, db_column='CodIBGEOrigem', blank=True, null=True)  # Field name made lowercase.
    ufdestino = models.CharField(db_column='UFDestino', max_length=2, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    codibgedestino = models.ForeignKey('Cidade', models.DO_NOTHING, db_column='CodIBGEDestino', related_name='freteuf_codibgedestino_set', blank=True, null=True)  # Field name made lowercase.
    vlminimo = models.DecimalField(db_column='VlMinimo', max_digits=19, decimal_places=4)  # Field name made lowercase.
    peracrescimo = models.DecimalField(db_column='PerAcrescimo', max_digits=4, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    perdesconto = models.DecimalField(db_column='PerDesconto', max_digits=4, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FreteUF'
        unique_together = (('idfretecif', 'uforigem', 'codibgeorigem', 'ufdestino', 'codibgedestino'), ('idfretecif', 'uforigem', 'codibgeorigem', 'ufdestino', 'codibgedestino'),)