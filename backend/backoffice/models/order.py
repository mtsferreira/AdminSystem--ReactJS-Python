from django.db import models

class Pedido(models.Model):
    idpedido = models.BigAutoField(db_column='IDPedido', primary_key=True)  # Field name made lowercase.
    idlocal = models.ForeignKey('Localvenda', models.DO_NOTHING, db_column='IDLocal')  # Field name made lowercase.
    nrpedido = models.IntegerField(db_column='NrPedido', blank=True, null=True)  # Field name made lowercase.
    origemvenda = models.ForeignKey('OrigemVenda', models.DO_NOTHING, db_column='OrigemVenda')  # Field name made lowercase.
    dtpedido = models.DateTimeField(db_column='DtPedido', blank=True, null=True)  # Field name made lowercase.
    codvendedor = models.IntegerField(db_column='CodVendedor')  # Field name made lowercase.
    codrepresentante = models.IntegerField(db_column='CodRepresentante', blank=True, null=True)  # Field name made lowercase.
    idcliente = models.ForeignKey('Cliente', models.DO_NOTHING, db_column='IDCliente')  # Field name made lowercase.
    cnpjcpf = models.CharField(db_column='CNPJCPF', max_length=18, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    idusuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='IDUsuario')  # Field name made lowercase.
    contato = models.CharField(db_column='Contato', max_length=60, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    telcelular = models.CharField(db_column='TelCelular', max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    whats = models.CharField(db_column='Whats', max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    situacao = models.CharField(db_column='Situacao', max_length=2, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    dtorcamento = models.DateTimeField(db_column='DTOrcamento', blank=True, null=True)  # Field name made lowercase.
    idcontato = models.IntegerField(db_column='IDContato', blank=True, null=True)  # Field name made lowercase.
    dtvalidade = models.DateField(db_column='DtValidade', blank=True, null=True)  # Field name made lowercase.
    idpedidoerp = models.BigIntegerField(db_column='IDPedidoERP', blank=True, null=True)  # Field name made lowercase.
    idresponsavel = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='IDResponsavel', related_name='pedido_idresponsavel_set')  # Field name made lowercase.
    nroriginal = models.CharField(db_column='NrOriginal', max_length=60, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Pedido'


class Pedidoresumo(models.Model):
    idpedido = models.OneToOneField(Pedido, models.DO_NOTHING, db_column='IDPedido', primary_key=True)  # Field name made lowercase.
    vlbrutomercadoria = models.DecimalField(db_column='VlBrutoMercadoria', max_digits=19, decimal_places=4)  # Field name made lowercase.
    vldesconto = models.DecimalField(db_column='VlDesconto', max_digits=19, decimal_places=4)  # Field name made lowercase.
    vlliquidomercadoria = models.DecimalField(db_column='VlLiquidoMercadoria', max_digits=19, decimal_places=4)  # Field name made lowercase.
    vlipi = models.DecimalField(db_column='VlIPI', max_digits=19, decimal_places=4)  # Field name made lowercase.
    vlst = models.DecimalField(db_column='VlST', max_digits=19, decimal_places=4)  # Field name made lowercase.
    vlcomimpostos = models.DecimalField(db_column='VlComImpostos', max_digits=19, decimal_places=4)  # Field name made lowercase.
    vldescincondicional = models.DecimalField(db_column='VlDescIncondicional', max_digits=19, decimal_places=4)  # Field name made lowercase.
    vlfrete = models.DecimalField(db_column='VlFrete', max_digits=19, decimal_places=4)  # Field name made lowercase.
    vlseguro = models.DecimalField(db_column='VlSeguro', max_digits=19, decimal_places=4)  # Field name made lowercase.
    vldespesas = models.DecimalField(db_column='VlDespesas', max_digits=19, decimal_places=4)  # Field name made lowercase.
    vloutras = models.DecimalField(db_column='VlOutras', max_digits=19, decimal_places=4)  # Field name made lowercase.
    vlorcamento = models.DecimalField(db_column='VlOrcamento', max_digits=19, decimal_places=4)  # Field name made lowercase.
    vlmargem = models.DecimalField(db_column='VlMargem', max_digits=19, decimal_places=4)  # Field name made lowercase.
    permargem = models.DecimalField(db_column='PerMargem', max_digits=7, decimal_places=4)  # Field name made lowercase.
    alteroudespesa = models.CharField(db_column='AlterouDespesa', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    cormargem = models.CharField(db_column='CorMargem', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PedidoResumo'


class TipoPedido(models.Model):
    idtipopedido = models.AutoField(db_column='IDTipoPedido', primary_key=True)  # Field name made lowercase.
    destipopedido = models.CharField(db_column='DesTipoPedido', max_length=40, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    temvolume = models.CharField(db_column='TemVolume', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    temcascata = models.CharField(db_column='TemCascata', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    temmargem = models.CharField(db_column='TemMargem', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    temminimo = models.CharField(db_column='TemMinimo', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    temestoque = models.CharField(db_column='TemEstoque', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    coderp = models.IntegerField(db_column='CodERP')  # Field name made lowercase.
    idpreco = models.IntegerField(db_column='IDPreco', blank=True, null=True)  # Field name made lowercase.
    idmargem = models.IntegerField(db_column='IDMargem', blank=True, null=True)  # Field name made lowercase.
    situacao = models.CharField(db_column='Situacao', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    idfretecif = models.ForeignKey('Fretecif', models.DO_NOTHING, db_column='IDFreteCIF', blank=True, null=True)  # Field name made lowercase.
    ordemimpressao = models.CharField(db_column='OrdemImpressao', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    layoutimpressao = models.CharField(db_column='LayoutImpressao', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    alterarvalorfrete = models.CharField(db_column='AlterarValorFrete', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    desccomposto = models.ForeignKey('Cascata', models.DO_NOTHING, db_column='DescComposto', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TipoPedido'
        

class TempCarteiraPedido(models.Model):
    idoperacao = models.CharField(db_column='IDOperacao', max_length=36, blank=True, null=True)  # Field name made lowercase.
    idlocal = models.IntegerField(db_column='IDLocal')  # Field name made lowercase.
    fantasialocal = models.CharField(db_column='FantasiaLocal', max_length=40, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    idvendedor = models.IntegerField(db_column='IDVendedor', blank=True, null=True)  # Field name made lowercase.
    nomevendedor = models.CharField(db_column='NomeVendedor', max_length=84, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    idresponsavel = models.IntegerField(db_column='IDResponsavel', blank=True, null=True)  # Field name made lowercase.
    nomeresponsavel = models.CharField(db_column='NomeResponsavel', max_length=84, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    idrepresentada = models.IntegerField(db_column='IDRepresentada', blank=True, null=True)  # Field name made lowercase.
    fantasiarepresentada = models.CharField(db_column='FantasiaRepresentada', max_length=73, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    nrpedido = models.IntegerField(db_column='NrPedido')  # Field name made lowercase.
    idcliente = models.IntegerField(db_column='IDCliente')  # Field name made lowercase.
    fantasiacliente = models.CharField(db_column='FantasiaCliente', max_length=73, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    dtpedido = models.DateField(db_column='DtPedido')  # Field name made lowercase.
    vlpedido = models.DecimalField(db_column='VlPedido', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    nrseriedanfe = models.CharField(db_column='NrSerieDANFE', max_length=6, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    nrdanfe = models.IntegerField(db_column='NrDANFE', blank=True, null=True)  # Field name made lowercase.
    dtemissao = models.DateTimeField(db_column='DtEmissao', blank=True, null=True)  # Field name made lowercase.
    vldanfe = models.DecimalField(db_column='VlDANFE', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    situacaodanfe = models.CharField(db_column='SituacaoDANFE', max_length=4, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    nrserietitulo = models.CharField(db_column='NrSerieTitulo', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    nrtitulo = models.IntegerField(db_column='NrTitulo', blank=True, null=True)  # Field name made lowercase.
    qtparcela = models.SmallIntegerField(db_column='QtParcela', blank=True, null=True)  # Field name made lowercase.
    situacaopedido = models.CharField(db_column='SituacaoPedido', max_length=13, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    idcarteirapedido = models.AutoField(db_column='IDCarteiraPedido', primary_key=True)

    class Meta:
        managed = False
        db_table = 'TempCarteiraPedido'


class OrigemVenda(models.Model):
    idorigemvenda = models.AutoField(db_column='IDOrigemVenda', primary_key=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    coderp = models.IntegerField(db_column='CodERP', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OrigemVenda'