from django.db import models


class Preco(models.Model):
    idpreco = models.AutoField(db_column='IDPreco', primary_key=True)  # Field name made lowercase.
    codtabela = models.CharField(db_column='CodTabela', max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    destabela = models.CharField(db_column='DesTabela', max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    embtabela = models.CharField(db_column='EmbTabela', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase. 0=UNIDADES, 1=CAIXAS1, 2=CAIXAS2 e 3=TODAS
    permargdesejavel = models.DecimalField(db_column='PerMargDesejavel', max_digits=5, decimal_places=2)  # Field name made lowercase.
    permargminima = models.DecimalField(db_column='PerMargMinima', max_digits=5, decimal_places=2)  # Field name made lowercase.
    perdesconto = models.DecimalField(db_column='PerDesconto', max_digits=4, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    idprecoregra = models.ForeignKey('Precoregra', models.DO_NOTHING, db_column='IDPrecoRegra', blank=True, null=True)  # Field name made lowercase.
    idvolume = models.ForeignKey('Volume', models.DO_NOTHING, db_column='IDVolume', blank=True, null=True)  # Field name made lowercase.
    datainicial = models.DateField(db_column='DataInicial')  # Field name made lowercase.
    datafinal = models.DateField(db_column='DataFinal')  # Field name made lowercase.
    tipofrete = models.ForeignKey('Tipofrete', models.DO_NOTHING, db_column='TipoFrete', blank=True, null=True)  # Field name made lowercase. 0=SIF 1=FOB 2=SEM FRETE
    empresaerp = models.IntegerField(db_column='EmpresaERP', blank=True, null=True)  # Field name made lowercase.
    dtatualizacao = models.DateField(db_column='DtAtualizacao', blank=True, null=True)  # Field name made lowercase.
    idcascata = models.ForeignKey('Cascata', models.DO_NOTHING, db_column='IDCascata', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Preco'


class PrecoRegra(models.Model):
    idprecoregra = models.AutoField(db_column='IDPrecoRegra', primary_key=True)  # Field name made lowercase.
    desregra = models.CharField(db_column='DesRegra', max_length=40, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    datainicial = models.DateField(db_column='DataInicial')  # Field name made lowercase.
    datafinal = models.DateField(db_column='DataFinal')  # Field name made lowercase.
    peracrescimo = models.DecimalField(db_column='PerAcrescimo', max_digits=5, decimal_places=2)  # Field name made lowercase.
    perdesconto = models.DecimalField(db_column='PerDesconto', max_digits=4, decimal_places=2)  # Field name made lowercase.
    ipi = models.CharField(db_column='IPI', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    st = models.CharField(db_column='ST', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    pis = models.CharField(db_column='PIS', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    cofins = models.CharField(db_column='COFINS', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    icms = models.CharField(db_column='ICMS', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PrecoRegra'
        

class PrecoEstrutura(models.Model):
    idprecoestrutura = models.AutoField(db_column='IDPrecoEstrutura', primary_key=True)  # Field name made lowercase.
    descprecoestrutura = models.CharField(db_column='DescPrecoEstrutura', max_length=40, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    datainicial = models.DateField(db_column='DataInicial')  # Field name made lowercase.
    datafinal = models.DateField(db_column='DataFinal')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PrecoEstrutura'


class Precocliente(models.Model):
    idpreco = models.OneToOneField(Preco, models.DO_NOTHING, db_column='IDPreco', primary_key=True)  # Field name made lowercase. The composite primary key (IDPreco, IDCliente) found, that is not supported. The first column is selected.
    idcliente = models.IntegerField(db_column='IDCliente')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PrecoCliente'
        unique_together = (('idpreco', 'idcliente'),)


class PrecoFaixa(models.Model):
    idprecofaixa = models.AutoField(db_column='IDPrecoFaixa', primary_key=True)  # Field name made lowercase. The composite primary key (IDPrecoFaixa, IDPrecoEstrutura) found, that is not supported. The first column is selected.
    idprecoestrutura = models.ForeignKey('PrecoEstrutura', models.DO_NOTHING, db_column='IDPrecoEstrutura')  # Field name made lowercase.
    familia = models.ForeignKey('Familia', models.DO_NOTHING, db_column='Familia', blank=True, null=True)  # Field name made lowercase.
    ggrupo = models.ForeignKey('Grandegrupo', models.DO_NOTHING, db_column='GGrupo', blank=True, null=True)  # Field name made lowercase.
    grupo = models.ForeignKey('Grupo', models.DO_NOTHING, db_column='Grupo', blank=True, null=True)  # Field name made lowercase.
    sgrupo = models.ForeignKey('Subgrupo', models.DO_NOTHING, db_column='Sgrupo', blank=True, null=True)  # Field name made lowercase.
    marca = models.ForeignKey('Marca', models.DO_NOTHING, db_column='Marca', blank=True, null=True)  # Field name made lowercase.
    categoria = models.ForeignKey('Categoria', models.DO_NOTHING, db_column='Categoria', blank=True, null=True)  # Field name made lowercase.
    fabricante = models.ForeignKey('Fabricante', models.DO_NOTHING, db_column='Fabricante', blank=True, null=True)  # Field name made lowercase.
    idlinha = models.ForeignKey('LinhaProduto', models.DO_NOTHING, db_column='IDLinha', blank=True, null=True)  # Field name made lowercase.
    origem = models.ForeignKey('Tabgeral', models.DO_NOTHING, db_column='Origem', blank=True, null=True)  # Field name made lowercase.
    pervariacao = models.DecimalField(db_column='PerVariacao', max_digits=7, decimal_places=4)  # Field name made lowercase.
    tipovariacao = models.CharField(db_column='TipoVariacao', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PrecoFaixa'
        unique_together = (('idprecofaixa', 'idprecoestrutura'),)


class PrecoLocal(models.Model):
    idpreco = models.OneToOneField(Preco, models.DO_NOTHING, db_column='IDPreco', primary_key=True)  # Field name made lowercase. The composite primary key (IDPreco, IDLocalVenda) found, that is not supported. The first column is selected.
    idlocalvenda = models.ForeignKey('LocalVenda', models.DO_NOTHING, db_column='IDLocalVenda')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PrecoLocal'
        unique_together = (('idpreco', 'idlocalvenda'),)


class PrecoPrazo(models.Model):
    idpreco = models.ForeignKey('Preco', models.DO_NOTHING, db_column='IDPreco')  # Field name made lowercase.
    prazodias = models.IntegerField(db_column='PrazoDias')  # Field name made lowercase.
    idprecoprazo = models.AutoField(db_column='IDPrecoPrazo', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PrecoPrazo'
        unique_together = (('idpreco', 'prazodias'),)


class PrecoProduto(models.Model):
    idpreco = models.OneToOneField(Preco, models.DO_NOTHING, db_column='IDPreco', primary_key=True)  # Field name made lowercase. The composite primary key (IDPreco, IDProduto, CodEmbalagem) found, that is not supported. The first column is selected.
    idproduto = models.IntegerField(db_column='IDProduto')  # Field name made lowercase.
    codembalagem = models.IntegerField(db_column='CodEmbalagem')  # Field name made lowercase.
    precobase = models.DecimalField(db_column='PrecoBase', max_digits=19, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    perdescmaximo = models.DecimalField(db_column='PerDescMaximo', max_digits=6, decimal_places=3)  # Field name made lowercase.
    situacao = models.CharField(db_column='Situacao', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PrecoProduto'
        unique_together = (('idpreco', 'idproduto', 'codembalagem'),)

    def get_product_infos(self):
        from BO.product.product import Product
        product = Product(id=self.idproduto).get_single_product()
        return product['product']


class PrecoUf(models.Model):
    idpreco = models.OneToOneField(Preco, models.DO_NOTHING, db_column='IDPreco', primary_key=True)  # Field name made lowercase. The composite primary key (IDPreco, UFValida) found, that is not supported. The first column is selected.
    ufvalida = models.CharField(db_column='UFValida', max_length=2, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PrecoUF'
        unique_together = (('idpreco', 'ufvalida'),)


class PrecoUsuario(models.Model):
    idpreco = models.OneToOneField(Preco, models.DO_NOTHING, db_column='IDPreco', primary_key=True)  # Field name made lowercase. The composite primary key (IDPreco, IDUsuario) found, that is not supported. The first column is selected.
    idusuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='IDUsuario')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PrecoUsuario'
        unique_together = (('idpreco', 'idusuario'),)


class PrecoVendedor(models.Model):
    idpreco = models.OneToOneField(Preco, models.DO_NOTHING, db_column='IDPreco', primary_key=True)  # Field name made lowercase. The composite primary key (IDPreco, IDUsuario) found, that is not supported. The first column is selected.
    idusuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='IDUsuario')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PrecoVendedor'
        unique_together = (('idpreco', 'idusuario'),)