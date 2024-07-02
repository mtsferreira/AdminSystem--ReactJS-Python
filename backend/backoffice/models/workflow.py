from django.db import models


class WorkFlow(models.Model):
    idworkflow = models.AutoField(db_column='IDWorkFlow', primary_key=True)  # Field name made lowercase.
    desworkflow = models.CharField(db_column='DesWorkFlow', max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    situacao = models.CharField(db_column='Situacao', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    idlistacor = models.ForeignKey('Listacor', models.DO_NOTHING, db_column='IDListaCor', blank=True, null=True)  # Field name made lowercase.
    coderp = models.IntegerField(db_column='CodERP', blank=True, null=True)  # Field name made lowercase.
    ordem = models.IntegerField(db_column='Ordem', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'WorkFlow'


class PedidoWF(models.Model):
    idpedido = models.OneToOneField('Pedido', models.DO_NOTHING, db_column='IDPedido', primary_key=True)  # Field name made lowercase.
    idworkflow = models.ForeignKey('Workflow', models.DO_NOTHING, db_column='IDWorkFlow', blank=True, null=True)  # Field name made lowercase.
    obsvendedor = models.CharField(db_column='ObsVendedor', max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    obspedido = models.CharField(db_column='ObsPedido', max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    obsnota = models.CharField(db_column='ObsNota', max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PedidoWF'