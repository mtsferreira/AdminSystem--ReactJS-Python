from django.db import models


class PortalMensagem(models.Model):
    idportalmensagem = models.AutoField(db_column='IDPortalMensagem', primary_key=True)  # Field name made lowercase.
    datainicial = models.DateTimeField(db_column='DataInicial')  # Field name made lowercase.
    datafinal = models.DateTimeField(db_column='DataFinal')  # Field name made lowercase.
    vendedor = models.CharField(db_column='Vendedor', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    varejo = models.CharField(db_column='Varejo', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    clienteb2b = models.CharField(db_column='ClienteB2B', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    clienteb2c = models.CharField(db_column='ClienteB2C', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    representante = models.CharField(db_column='Representante', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    mensagem = models.CharField(db_column='Mensagem', max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PortalMensagem'
        