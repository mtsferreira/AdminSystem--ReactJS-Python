from django.db import models

class Pagamento(models.Model):
    idpagamento = models.AutoField(db_column='IDPagamento', primary_key=True)  # Field name made lowercase.
    prazodias = models.IntegerField(db_column='PrazoDias')  # Field name made lowercase.
    descpagamento = models.CharField(db_column='DescPagamento', max_length=40, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    qparcela = models.IntegerField(db_column='Qparcela')  # Field name made lowercase.
    coderp = models.IntegerField(db_column='CodERP')  # Field name made lowercase.
    situacao = models.CharField(db_column='Situacao', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Pagamento'
        

class PagamentoLocal(models.Model):
    idpagamento = models.OneToOneField(Pagamento, models.DO_NOTHING, db_column='IDPagamento', primary_key=True)  # Field name made lowercase. The composite primary key (IDPagamento, IDLocal) found, that is not supported. The first column is selected.
    idlocal = models.ForeignKey('LocalVenda', models.DO_NOTHING, db_column='IDLocal')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PagamentoLocal'
        unique_together = (('idpagamento', 'idlocal'),)


class PagamentoParcela(models.Model):
    idpagamento = models.OneToOneField(Pagamento, models.DO_NOTHING, db_column='IDPagamento', primary_key=True)  # Field name made lowercase. The composite primary key (IDPagamento, NrParcela) found, that is not supported. The first column is selected.
    nrparcela = models.IntegerField(db_column='NrParcela')  # Field name made lowercase.
    prparcela = models.DecimalField(db_column='PrParcela', max_digits=6, decimal_places=3)  # Field name made lowercase.
    qtdias = models.IntegerField(db_column='QtDias')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PagamentoParcela'
        unique_together = (('idpagamento', 'nrparcela'),)


class PagamentoVendedor(models.Model):
    idpagamento = models.OneToOneField(Pagamento, models.DO_NOTHING, db_column='IDPagamento', primary_key=True)  # Field name made lowercase. The composite primary key (IDPagamento, IDUsuario) found, that is not supported. The first column is selected.
    idusuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='IDUsuario')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PagamentoVendedor'
        unique_together = (('idpagamento', 'idusuario'),)

    
class PrazoFinanceiro(models.Model):
    idprazofinanceiro = models.AutoField(db_column='IDPrazoFinanceiro', primary_key=True)  # Field name made lowercase.
    descprazo = models.CharField(db_column='DescPrazo', max_length=40, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    datainicial = models.DateField(db_column='DataInicial')  # Field name made lowercase.
    datafinal = models.DateField(db_column='DataFinal')  # Field name made lowercase.
    situacao = models.CharField(db_column='Situacao', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PrazoFinanceiro'


class PrazoFaixa(models.Model):
    idprazofinanceiro = models.ForeignKey('Prazofinanceiro', models.DO_NOTHING, db_column='IDPrazoFinanceiro')  # Field name made lowercase.
    prazodias = models.IntegerField(db_column='PrazoDias')  # Field name made lowercase.
    perdesconto = models.DecimalField(db_column='PerDesconto', max_digits=4, decimal_places=2)  # Field name made lowercase.
    peracrescimo = models.DecimalField(db_column='PerAcrescimo', max_digits=5, decimal_places=2)  # Field name made lowercase.
    vlminimo = models.DecimalField(db_column='VlMinimo', max_digits=19, decimal_places=4)  # Field name made lowercase.
    situacao = models.CharField(db_column='Situacao', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    idprazofaixa = models.AutoField(db_column='IDPrazoFaixa', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PrazoFaixa'


class PoliticaComissao(models.Model):
    idpolcomissao = models.AutoField(db_column='IDPolComissao', primary_key=True)  # Field name made lowercase.
    despolitica = models.CharField(db_column='DesPolitica', max_length=40, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    percomissao = models.DecimalField(db_column='PerComissao', max_digits=4, decimal_places=2)  # Field name made lowercase.
    percomnovos = models.DecimalField(db_column='PerComNovos', max_digits=4, decimal_places=2)  # Field name made lowercase.
    situacao = models.CharField(db_column='Situacao', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PoliticaComissao'


class Oferta(models.Model):
    idoferta = models.AutoField(db_column='IDOferta', primary_key=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    dtinicial = models.DateField(db_column='DtInicial')  # Field name made lowercase.
    dtfinal = models.DateField(db_column='DtFinal')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Oferta'


class OfertaEstrutura(models.Model):
    idofertaestrutura = models.AutoField(db_column='IDOfertaEstrutura', primary_key=True)  # Field name made lowercase.
    idoferta = models.ForeignKey(Oferta, models.DO_NOTHING, db_column='IDOferta')  # Field name made lowercase.
    idproduto = models.ForeignKey('Produto', models.DO_NOTHING, db_column='IDProduto', blank=True, null=True)  # Field name made lowercase.
    idfamilia = models.ForeignKey('Familia', models.DO_NOTHING, db_column='IDFamilia', blank=True, null=True)  # Field name made lowercase.
    idggrupo = models.ForeignKey('Grandegrupo', models.DO_NOTHING, db_column='IDGGrupo', blank=True, null=True)  # Field name made lowercase.
    idgrupo = models.ForeignKey('Grupo', models.DO_NOTHING, db_column='IDGrupo', blank=True, null=True)  # Field name made lowercase.
    idsgrupo = models.ForeignKey('Subgrupo', models.DO_NOTHING, db_column='IDSgrupo', blank=True, null=True)  # Field name made lowercase.
    idmarca = models.ForeignKey('Marca', models.DO_NOTHING, db_column='IDMarca', blank=True, null=True)  # Field name made lowercase.
    idcategoria = models.ForeignKey('Categoria', models.DO_NOTHING, db_column='IDCategoria', blank=True, null=True)  # Field name made lowercase.
    idfabricante = models.ForeignKey('Fabricante', models.DO_NOTHING, db_column='IDFabricante', blank=True, null=True)  # Field name made lowercase.
    idlinha = models.ForeignKey('Linhaproduto', models.DO_NOTHING, db_column='IDLinha', blank=True, null=True)  # Field name made lowercase.
    desoferta = models.DecimalField(db_column='DesOferta', max_digits=7, decimal_places=3)  # Field name made lowercase.
    qtoferta = models.DecimalField(db_column='QtOferta', max_digits=19, decimal_places=4)  # Field name made lowercase.
    qtminima = models.DecimalField(db_column='QtMinima', max_digits=19, decimal_places=4)  # Field name made lowercase.
    qtmaxima = models.DecimalField(db_column='QtMaxima', max_digits=19, decimal_places=4)  # Field name made lowercase.
    desoferta2 = models.DecimalField(db_column='DesOferta2', max_digits=7, decimal_places=3, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OfertaEstrutura'
        unique_together = (('idoferta', 'idproduto', 'idfamilia', 'idggrupo', 'idgrupo', 'idsgrupo', 'idmarca', 'idcategoria', 'idfabricante', 'idlinha'),)


class OfertaLocal(models.Model):
    idoferta = models.OneToOneField(Oferta, models.DO_NOTHING, db_column='IDOferta', primary_key=True)  # Field name made lowercase. The composite primary key (IDOferta, IDLocal) found, that is not supported. The first column is selected.
    idlocal = models.ForeignKey('LocalVenda', models.DO_NOTHING, db_column='IDLocal')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OfertaLocal'
        unique_together = (('idoferta', 'idlocal'),)