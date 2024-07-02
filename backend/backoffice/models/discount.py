from django.db import models


class DescontoTipo(models.Model):
    iddescontotipo = models.AutoField(db_column='IDDescontoTipo', primary_key=True)  # Field name made lowercase.
    tipocliente = models.ForeignKey('Clientetipo', models.DO_NOTHING, db_column='TipoCliente')  # Field name made lowercase.
    dtinicial = models.DateField(db_column='DtInicial')  # Field name made lowercase.
    dtfinal = models.DateField(db_column='DtFinal')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DescontoTipo'


class DescontoTipoEstrutura(models.Model):
    iddescontotipoestrutura = models.AutoField(db_column='IDDescontoTipoEstrutura', primary_key=True)  # Field name made lowercase.
    iddescontotipo = models.ForeignKey('Descontotipo', models.DO_NOTHING, db_column='IDDescontoTipo')  # Field name made lowercase.
    idproduto = models.ForeignKey('Produto', models.DO_NOTHING, db_column='IDProduto', blank=True, null=True)  # Field name made lowercase.
    idfamilia = models.ForeignKey('Familia', models.DO_NOTHING, db_column='IDFamilia', blank=True, null=True)  # Field name made lowercase.
    idggrupo = models.ForeignKey('Grandegrupo', models.DO_NOTHING, db_column='IDGGrupo', blank=True, null=True)  # Field name made lowercase.
    idgrupo = models.ForeignKey('Grupo', models.DO_NOTHING, db_column='IDGrupo', blank=True, null=True)  # Field name made lowercase.
    idsgrupo = models.ForeignKey('Subgrupo', models.DO_NOTHING, db_column='IDSgrupo', blank=True, null=True)  # Field name made lowercase.
    idmarca = models.ForeignKey('Marca', models.DO_NOTHING, db_column='IDMarca', blank=True, null=True)  # Field name made lowercase.
    idcategoria = models.ForeignKey('Categoria', models.DO_NOTHING, db_column='IDCategoria', blank=True, null=True)  # Field name made lowercase.
    idfabricante = models.ForeignKey('Fabricante', models.DO_NOTHING, db_column='IDFabricante', blank=True, null=True)  # Field name made lowercase.
    idlinha = models.ForeignKey('Linhaproduto', models.DO_NOTHING, db_column='IDLinha', blank=True, null=True)  # Field name made lowercase.
    desconto = models.DecimalField(db_column='Desconto', max_digits=7, decimal_places=3)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DescontoTipoEstrutura'
        unique_together = (('iddescontotipo', 'idproduto', 'idfamilia', 'idggrupo', 'idgrupo', 'idsgrupo', 'idmarca', 'idcategoria', 'idfabricante', 'idlinha'),)


class ComDesconto(models.Model):
    idcomdesconto = models.AutoField(db_column='IDComDesconto', primary_key=True)  # Field name made lowercase.
    descomissaodesc = models.CharField(db_column='DesComissaoDesc', max_length=40, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ComDesconto'


class ComFaixa(models.Model):
    idcomfaixa = models.AutoField(db_column='IDComFaixa', primary_key=True)  # Field name made lowercase. The composite primary key (IDComFaixa, IDComDesconto) found, that is not supported. The first column is selected.
    idcomdesconto = models.ForeignKey('ComDesconto', models.DO_NOTHING, db_column='IDComDesconto')  # Field name made lowercase.
    perdesconto = models.DecimalField(db_column='PerDesconto', max_digits=4, decimal_places=2)  # Field name made lowercase.
    fatorcom = models.DecimalField(db_column='FatorCom', max_digits=19, decimal_places=4)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ComFaixa'
        unique_together = (('idcomfaixa', 'idcomdesconto'),)


class Volume(models.Model):
    idvolume = models.AutoField(db_column='IDVolume', primary_key=True)  # Field name made lowercase.
    desvolume = models.CharField(db_column='DesVolume', max_length=40, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    datainicial = models.DateField(db_column='DataInicial')  # Field name made lowercase.
    datafinal = models.DateField(db_column='DataFinal')  # Field name made lowercase.
    situacao = models.CharField(db_column='Situacao', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Volume'


class VolumeFaixa(models.Model):
    idvolumefaixa = models.AutoField(db_column='IDVolumeFaixa', primary_key=True)  # Field name made lowercase.
    idvolume = models.ForeignKey('Volume', models.DO_NOTHING, db_column='IDVolume')  # Field name made lowercase.
    vlcomprasde = models.DecimalField(db_column='VlComprasDE', max_digits=19, decimal_places=4)  # Field name made lowercase.
    vlcomprasate = models.DecimalField(db_column='VlComprasATE', max_digits=19, decimal_places=4)  # Field name made lowercase.
    perdesconto = models.DecimalField(db_column='PerDesconto', max_digits=4, decimal_places=2)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VolumeFaixa'


class Cascata(models.Model):
    idcascata = models.AutoField(db_column='IDCascata', primary_key=True)  # Field name made lowercase.
    descascata = models.CharField(db_column='DesCascata', max_length=40, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    situacao = models.CharField(db_column='Situacao', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Cascata'


class CascataFaixa(models.Model):
    idcascatafaixa = models.AutoField(db_column='IDCascataFaixa', primary_key=True)  # Field name made lowercase. The composite primary key (IDCascataFaixa, IDCascata) found, that is not supported. The first column is selected.
    idcascata = models.ForeignKey('Cascata', models.DO_NOTHING, db_column='IDCascata')  # Field name made lowercase.
    sigla = models.CharField(db_column='Sigla', max_length=6, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    permaximo = models.DecimalField(db_column='PerMaximo', max_digits=4, decimal_places=2)  # Field name made lowercase.
    tipocascata = models.CharField(db_column='TipoCascata', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CascataFaixa'
        unique_together = (('idcascatafaixa', 'idcascata'),)