from django.db import models

class Empresa(models.Model):
    idempresa = models.AutoField(db_column='IDEmpresa', primary_key=True)  # Field name made lowercase.
    cnpj = models.CharField(db_column='CNPJ', max_length=18, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    razao = models.CharField(db_column='Razao', max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    fantasia = models.CharField(db_column='Fantasia', max_length=40, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    cep = models.CharField(db_column='CEP', max_length=8, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    numero = models.CharField(db_column='Numero', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    complemento = models.CharField(db_column='Complemento', max_length=60, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bairro = models.CharField(db_column='Bairro', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    codibge = models.ForeignKey('Cidade', models.DO_NOTHING, db_column='CodIBGE')  # Field name made lowercase.
    imagem = models.CharField(db_column='Imagem', max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    banner = models.CharField(db_column='Banner', max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    logradouro = models.CharField(db_column='Logradouro', max_length=60, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Empresa'
    
class LocalConfig(models.Model):
    idlocal = models.IntegerField(db_column='IDLocal', primary_key=True)  # Field name made lowercase.
    comissao = models.CharField(db_column='Comissao', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    desccooperado = models.DecimalField(db_column='DescCooperado', max_digits=4, decimal_places=2)  # Field name made lowercase.
    desclocal = models.DecimalField(db_column='DescLocal', max_digits=4, decimal_places=2)  # Field name made lowercase.
    deslimite = models.DecimalField(db_column='DesLimite', max_digits=4, decimal_places=2)  # Field name made lowercase.
    tipopedido = models.IntegerField(db_column='TipoPedido', blank=True, null=True)  # Field name made lowercase.
    idfretecif = models.ForeignKey('Fretecif', models.DO_NOTHING, db_column='IDFreteCIF', blank=True, null=True)  # Field name made lowercase.
    prazomedio = models.IntegerField(db_column='PrazoMedio')  # Field name made lowercase.
    precoestrutura = models.IntegerField(db_column='PrecoEstrutura', blank=True, null=True)  # Field name made lowercase.
    desccomposto = models.ForeignKey('Cascata', models.DO_NOTHING, db_column='DescComposto', blank=True, null=True)  # Field name made lowercase.
    descvolume = models.ForeignKey('Volume', models.DO_NOTHING, db_column='DescVolume', blank=True, null=True)  # Field name made lowercase.
    comdesconto = models.IntegerField(db_column='ComDesconto', blank=True, null=True)  # Field name made lowercase.
    preco = models.IntegerField(db_column='Preco')  # Field name made lowercase.
    coddeperp = models.IntegerField(db_column='CodDepERP', blank=True, null=True)  # Field name made lowercase.
    repetiritem = models.CharField(db_column='RepetirItem', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    liberardescontovolume = models.CharField(db_column='LiberarDescontoVolume', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    habilitardescontocliente = models.CharField(db_column='HabilitarDescontoCliente', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    habilitareventosdesconto = models.CharField(db_column='HabilitarEventosDesconto', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    permitirvendabloqueado = models.CharField(db_column='PermitirVendaBloqueado', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    visualizarsaldoestoque = models.CharField(db_column='VisualizarSaldoEstoque', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    habilitardescontoadicional = models.CharField(db_column='HabilitarDescontoAdicional', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    habilitarmargemvalor = models.CharField(db_column='HabilitarMargemValor', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    mostrabanner = models.CharField(db_column='MostraBanner', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    comissaocompartilhada = models.CharField(db_column='ComissaoCompartilhada', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    usarvalorcomimposto = models.CharField(db_column='UsarValorComImposto', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    diasvalidade = models.IntegerField(db_column='DiasValidade', blank=True, null=True)  # Field name made lowercase.
    listarvendedor = models.CharField(db_column='ListarVendedor', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LocalConfig'

class LocalEmail(models.Model):
    idlocal = models.OneToOneField('LocalVenda', models.DO_NOTHING, db_column='IDLocal')  # Field name made lowercase. The composite primary key (IDLocal, IDTipoEmail) found, that is not supported. The first column is selected.
    idtipoemail = models.ForeignKey('Tabgeral', models.DO_NOTHING, db_column='IDTipoEmail')  # Field name made lowercase.
    emailresposta = models.CharField(db_column='EmailResposta', max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    assunto = models.TextField(db_column='Assunto', db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    corpo = models.TextField(db_column='Corpo', db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    assinatura = models.TextField(db_column='Assinatura', db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase. This field type is a guess.
    idlocalemail = models.AutoField(db_column='IDLocalEmail', primary_key=True)
    
    class Meta:
        managed = False
        db_table = 'LocalEmail'
        unique_together = (('idlocal', 'idtipoemail'),)
        
class LocalVenda(models.Model):
    idlocalvenda = models.AutoField(db_column='IDLocalVenda', primary_key=True)  # Field name made lowercase.
    cnpj = models.CharField(db_column='CNPJ', max_length=18, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    razao = models.CharField(db_column='Razao', max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    fantasia = models.CharField(db_column='Fantasia', max_length=40, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    cep = models.CharField(db_column='CEP', max_length=8, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    logradouro = models.CharField(db_column='Logradouro', max_length=60, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    numero = models.CharField(db_column='Numero', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    complemento = models.CharField(db_column='Complemento', max_length=60, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bairro = models.CharField(db_column='Bairro', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    codibge = models.ForeignKey('Cidade', models.DO_NOTHING, db_column='CodIBGE')  # Field name made lowercase.
    coderp = models.IntegerField(db_column='CodERP', unique=True)  # Field name made lowercase.
    situacao = models.CharField(db_column='Situacao', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    foto = models.BinaryField(db_column='Foto', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LocalVenda'
        
    def get_status_description(self):
        return 'ATIVO' if self.situacao == 'A' else 'CANCELADO'