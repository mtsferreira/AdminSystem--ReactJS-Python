# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Cidade(models.Model):
    codibge = models.IntegerField(db_column='CodIBGE', primary_key=True)  # Field name made lowercase.
    descidade = models.CharField(db_column='DesCidade', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    uf = models.CharField(db_column='UF', max_length=2, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    ddd = models.CharField(db_column='DDD', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Cidade'


class Carimbo(models.Model):
    idcarimbo = models.AutoField(db_column='IDCarimbo', primary_key=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=1000, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    carimboerp = models.IntegerField(db_column='CarimboERP', blank=True, null=True)  # Field name made lowercase.
    situacao = models.CharField(db_column='Situacao', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    desccomplementar = models.CharField(db_column='DescComplementar', max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Carimbo'


class TipoFrete(models.Model):
    idtipofrete = models.AutoField(db_column='IDTipoFrete', primary_key=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=1000, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    tipofreteerp = models.IntegerField(db_column='TipoFreteERP', blank=True, null=True)  # Field name made lowercase.
    situacao = models.CharField(db_column='Situacao', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TipoFrete'
        

class GrupoEconomico(models.Model):
    idgrupoeconomico = models.AutoField(db_column='IDGrupoEconomico', primary_key=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    grupoeconomicoerp = models.IntegerField(db_column='GrupoEconomicoERP', blank=True, null=True)  # Field name made lowercase.
    situacao = models.CharField(db_column='Situacao', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GrupoEconomico'


class Rede(models.Model):
    idrede = models.AutoField(db_column='IDRede', primary_key=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    redeerp = models.IntegerField(db_column='RedeERP', blank=True, null=True)  # Field name made lowercase.
    situacao = models.CharField(db_column='Situacao', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Rede'
        

class EquipeVenda(models.Model):
    idequipe = models.AutoField(db_column='IDEquipe', primary_key=True)  # Field name made lowercase.
    desequipe = models.CharField(db_column='DesEquipe', max_length=40, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    nivel1 = models.IntegerField(db_column='Nivel1')  # Field name made lowercase.
    nivel2 = models.IntegerField(db_column='Nivel2', blank=True, null=True)  # Field name made lowercase.
    nivel3 = models.IntegerField(db_column='Nivel3', blank=True, null=True)  # Field name made lowercase.
    situacao = models.CharField(db_column='Situacao', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EquipeVenda'
        
        
class ListaCor(models.Model):
    idlistacor = models.AutoField(db_column='IDListaCor', primary_key=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', unique=True, max_length=25, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    cor = models.CharField(db_column='Cor', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ListaCor'