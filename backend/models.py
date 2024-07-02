# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models



class Apiconfiguracao(models.Model):
    integracao = models.IntegerField(db_column='Integracao', primary_key=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    wsurl = models.CharField(db_column='WSUrl', max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    evento = models.CharField(db_column='Evento', max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    usuario = models.CharField(db_column='Usuario', max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    senha = models.CharField(db_column='Senha', max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    parametro = models.CharField(db_column='Parametro', max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    formato = models.CharField(db_column='Formato', max_length=5, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    diretorioorigem = models.CharField(db_column='DiretorioOrigem', max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    diretoriodestino = models.CharField(db_column='DiretorioDestino', max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'APIConfiguracao'


class Acessoperfilpermissao(models.Model):
    idperfil = models.OneToOneField('Acessoperfil', models.DO_NOTHING, db_column='IDPerfil', primary_key=True)  # Field name made lowercase. The composite primary key (IDPerfil, IDMenu) found, that is not supported. The first column is selected.
    idmenu = models.ForeignKey('Menu', models.DO_NOTHING, db_column='IDMenu')  # Field name made lowercase.
    visualizar = models.CharField(db_column='Visualizar', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    alterar = models.CharField(db_column='Alterar', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AcessoPerfilPermissao'
        unique_together = (('idperfil', 'idmenu'),)


class Acessopermissao(models.Model):
    idpermissao = models.AutoField(db_column='IDPermissao', primary_key=True)  # Field name made lowercase.
    grupo = models.CharField(db_column='Grupo', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    situacao = models.CharField(db_column='Situacao', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    urlpermissao = models.CharField(db_column='UrlPermissao', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AcessoPermissao'


class Banner(models.Model):
    idbanner = models.AutoField(db_column='IDBanner', primary_key=True)  # Field name made lowercase.
    datainicial = models.DateTimeField(db_column='DataInicial')  # Field name made lowercase.
    datafinal = models.DateTimeField(db_column='DataFinal')  # Field name made lowercase.
    diretorio = models.CharField(db_column='Diretorio', max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    interno = models.CharField(db_column='Interno', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    externo = models.CharField(db_column='Externo', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    cliente = models.CharField(db_column='Cliente', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    varejo = models.CharField(db_column='Varejo', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Banner'


class Bloqueio(models.Model):
    idbloqueio = models.AutoField(db_column='IDBloqueio', primary_key=True)  # Field name made lowercase.
    idcliente = models.ForeignKey('Cliente', models.DO_NOTHING, db_column='IDCliente')  # Field name made lowercase.
    idlocal = models.ForeignKey('LocalVenda', models.DO_NOTHING, db_column='IDLocal', blank=True, null=True)  # Field name made lowercase.
    tipobloqueio = models.CharField(db_column='TipoBloqueio', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    dtbloqueio = models.DateField(db_column='DtBloqueio')  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    dtliberacao = models.DateField(db_column='DtLiberacao', blank=True, null=True)  # Field name made lowercase.
    motivo = models.CharField(db_column='Motivo', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    coderp = models.BigIntegerField(db_column='CodERP', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Bloqueio'


class Cfop(models.Model):
    codcfop = models.SmallIntegerField(db_column='CodCFOP', primary_key=True)  # Field name made lowercase.
    descfop = models.CharField(db_column='DesCFOP', max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CFOP'








class Cliente(models.Model):
    idcliente = models.AutoField(db_column='IDCliente', primary_key=True)  # Field name made lowercase.
    coderp = models.IntegerField(db_column='CodERP')  # Field name made lowercase.
    cnpjcpf = models.CharField(db_column='CNPJCPF', max_length=18, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    razao = models.CharField(db_column='Razao', max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    fantasia = models.CharField(db_column='Fantasia', max_length=40, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    cidade = models.CharField(db_column='Cidade', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    ufcliente = models.CharField(db_column='UFCliente', max_length=2, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    situacao = models.CharField(db_column='Situacao', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Cliente'
        unique_together = (('idcliente', 'coderp', 'cnpjcpf'),)


class Clienteb2B(models.Model):
    idusuario = models.OneToOneField('Usuario', models.DO_NOTHING, db_column='IDUsuario', primary_key=True)  # Field name made lowercase.
    cnpjcliente = models.CharField(db_column='CNPJCliente', max_length=18, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    codvendedor = models.IntegerField(db_column='CodVendedor')  # Field name made lowercase.
    perdesconto = models.DecimalField(db_column='PerDesconto', max_digits=4, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    percomissao = models.DecimalField(db_column='PerComissao', max_digits=4, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ClienteB2B'


class Clientecontato(models.Model):
    idcontato = models.AutoField(db_column='IDContato', primary_key=True)  # Field name made lowercase.
    idcliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='IDCliente')  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=60, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    datanascimento = models.DateField(db_column='DataNascimento', blank=True, null=True)  # Field name made lowercase.
    funcao = models.CharField(db_column='Funcao', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    departamento = models.CharField(db_column='Departamento', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    telfixo = models.CharField(db_column='TelFixo', max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    telcelular = models.CharField(db_column='TelCelular', max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    numwhats = models.CharField(db_column='NumWhats', max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    emailcorp = models.CharField(db_column='EmailCorp', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    pedidocorp = models.CharField(db_column='PedidoCorp', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    emailpessoal = models.CharField(db_column='EmailPessoal', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    pedidopessoal = models.CharField(db_column='PedidoPessoal', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    situacao = models.CharField(db_column='Situacao', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ClienteContato'


class Clientedado(models.Model):
    idcliente = models.OneToOneField(Cliente, models.DO_NOTHING, db_column='IDCliente', primary_key=True)  # Field name made lowercase.
    cep = models.CharField(db_column='CEP', max_length=8, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    logradouro = models.CharField(db_column='Logradouro', max_length=60, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    numero = models.CharField(db_column='Numero', max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    complemento = models.CharField(db_column='Complemento', max_length=60, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bairro = models.CharField(db_column='Bairro', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    codibge = models.ForeignKey('Cidade', models.DO_NOTHING, db_column='CodIBGE')  # Field name made lowercase.
    datafundacao = models.DateField(db_column='DataFundacao', blank=True, null=True)  # Field name made lowercase.
    telfixo = models.CharField(db_column='TelFixo', max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    telcelular = models.CharField(db_column='TelCelular', max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ClienteDado'


class Clienteendereco(models.Model):
    idendereco = models.AutoField(db_column='IDEndereco', primary_key=True)  # Field name made lowercase.
    idcliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='IDCliente')  # Field name made lowercase.
    cep = models.CharField(db_column='CEP', max_length=8, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    logradouro = models.CharField(db_column='Logradouro', max_length=60, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    numero = models.CharField(db_column='Numero', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    complemento = models.CharField(db_column='Complemento', max_length=60, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bairro = models.CharField(db_column='Bairro', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    codibge = models.ForeignKey('Cidade', models.DO_NOTHING, db_column='CodIBGE')  # Field name made lowercase.
    tipoendereco = models.CharField(db_column='TipoEndereco', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    situacao = models.CharField(db_column='Situacao', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ClienteEndereco'


class Clienteespecial(models.Model):
    idcliente = models.OneToOneField(Cliente, models.DO_NOTHING, db_column='IDCliente', primary_key=True)  # Field name made lowercase.
    regsuframa = models.CharField(db_column='RegSuframa', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    dataregsuframa = models.DateField(db_column='DataRegSuframa', blank=True, null=True)  # Field name made lowercase.
    datavalsuframa = models.DateField(db_column='DataValSuframa', blank=True, null=True)  # Field name made lowercase.
    regtare = models.CharField(db_column='RegTare', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    dataregtare = models.DateField(db_column='DataRegTare', blank=True, null=True)  # Field name made lowercase.
    datavaltare = models.DateField(db_column='DataValTare', blank=True, null=True)  # Field name made lowercase.
    carimbo = models.ForeignKey(Carimbo, models.DO_NOTHING, db_column='Carimbo', blank=True, null=True)  # Field name made lowercase.
    descricaocarimbo = models.CharField(db_column='DescricaoCarimbo', max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ClienteEspecial'


class Clientefiscal(models.Model):
    idcliente = models.OneToOneField(Cliente, models.DO_NOTHING, db_column='IDCliente', primary_key=True)  # Field name made lowercase.
    cnaeprincipal = models.CharField(db_column='CNAEPrincipal', max_length=7, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    inscestadual = models.CharField(db_column='InscEstadual', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    inscmunicipal = models.CharField(db_column='InscMunicipal', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    natjuridica = models.ForeignKey('Tabgeral', models.DO_NOTHING, db_column='NatJuridica', blank=True, null=True)  # Field name made lowercase.
    sitfiscal = models.ForeignKey('Tabgeral', models.DO_NOTHING, db_column='SitFiscal', related_name='clientefiscal_sitfiscal_set', blank=True, null=True)  # Field name made lowercase.
    destinacao = models.ForeignKey('Tabgeral', models.DO_NOTHING, db_column='Destinacao', related_name='clientefiscal_destinacao_set', blank=True, null=True)  # Field name made lowercase.
    contribuinteicms = models.CharField(db_column='ContribuinteICMS', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    orgaopublico = models.CharField(db_column='OrgaoPublico', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ClienteFiscal'


class Clientehistorico(models.Model):
    idcliente = models.IntegerField(db_column='IDCliente', primary_key=True)  # Field name made lowercase. The composite primary key (IDCliente, IDLocal) found, that is not supported. The first column is selected.
    idlocal = models.IntegerField(db_column='IDLocal')  # Field name made lowercase.
    nrnota = models.IntegerField(db_column='NrNota', blank=True, null=True)  # Field name made lowercase.
    dtultimacompra = models.DateField(db_column='DtUltimaCompra', blank=True, null=True)  # Field name made lowercase.
    vlultimacompra = models.DecimalField(db_column='VlUltimaCompra', max_digits=19, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    jsonproduto = models.TextField(db_column='JSONProduto', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    vlmediamensal = models.DecimalField(db_column='VlMediaMensal', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ClienteHistorico'
        unique_together = (('idcliente', 'idlocal'),)


class Clientehistoricoproduto(models.Model):
    idcliente = models.IntegerField(db_column='IDCliente', primary_key=True)  # Field name made lowercase. The composite primary key (IDCliente, IDLocal, IDProduto, DtHistorico) found, that is not supported. The first column is selected.
    idlocal = models.IntegerField(db_column='IDLocal')  # Field name made lowercase.
    dthistorico = models.DateField(db_column='DtHistorico')  # Field name made lowercase.
    dtultimacompra = models.DateField(db_column='DtUltimaCompra', blank=True, null=True)  # Field name made lowercase.
    idproduto = models.IntegerField(db_column='IDProduto')  # Field name made lowercase.
    qtproduto = models.DecimalField(db_column='QtProduto', max_digits=19, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    vlproduto = models.DecimalField(db_column='VlProduto', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ClienteHistoricoProduto'
        unique_together = (('idcliente', 'idlocal', 'idproduto', 'dthistorico'),)


class Clienteperfil(models.Model):
    idcliente = models.OneToOneField(Cliente, models.DO_NOTHING, db_column='IDCliente', primary_key=True)  # Field name made lowercase.
    tipocliente = models.ForeignKey('Clientetipo', models.DO_NOTHING, db_column='TipoCliente', blank=True, null=True)  # Field name made lowercase.
    grupoeco = models.ForeignKey('Grupoeconomico', models.DO_NOTHING, db_column='GrupoEco', blank=True, null=True)  # Field name made lowercase.
    rede = models.ForeignKey('Rede', models.DO_NOTHING, db_column='Rede', blank=True, null=True)  # Field name made lowercase.
    idtipopedido = models.ForeignKey('Tipopedido', models.DO_NOTHING, db_column='IDTipoPedido', blank=True, null=True)  # Field name made lowercase.
    idprecoregra = models.ForeignKey('Precoregra', models.DO_NOTHING, db_column='IDPrecoRegra', blank=True, null=True)  # Field name made lowercase.
    descomposto = models.CharField(db_column='DesComposto', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    perdesconto = models.DecimalField(db_column='PerDesconto', max_digits=4, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    pedidominimo = models.CharField(db_column='PedidoMinimo', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    limitecredito = models.CharField(db_column='LimiteCredito', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    tipofrete = models.ForeignKey('Tipofrete', models.DO_NOTHING, db_column='TipoFrete', blank=True, null=True)  # Field name made lowercase.
    idtransportador = models.IntegerField(db_column='IDTransportador', blank=True, null=True)  # Field name made lowercase.
    idregiao = models.ForeignKey('Regiaovenda', models.DO_NOTHING, db_column='IDRegiao', blank=True, null=True)  # Field name made lowercase.
    descgeral = models.CharField(db_column='DescGeral', max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    presencacomprador = models.IntegerField(db_column='PresencaComprador', blank=True, null=True)  # Field name made lowercase.
    prazomedio = models.IntegerField(db_column='PrazoMedio', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ClientePerfil'


class Clientevendedor(models.Model):
    idclientevendedor = models.AutoField(db_column='IDClienteVendedor', primary_key=True)  # Field name made lowercase.
    idcliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='IDCliente')  # Field name made lowercase.
    idusuario = models.IntegerField(db_column='IDUsuario')  # Field name made lowercase.
    tipousuario = models.CharField(db_column='TipoUsuario', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    idcascata = models.ForeignKey(Cascata, models.DO_NOTHING, db_column='IDCascata', blank=True, null=True)  # Field name made lowercase.
    idvolume = models.ForeignKey('Volume', models.DO_NOTHING, db_column='IDVolume', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ClienteVendedor'
        unique_together = (('idcliente', 'idusuario', 'tipousuario'),)


class Clientevisita(models.Model):
    idclientevendedor = models.OneToOneField(Clientevendedor, models.DO_NOTHING, db_column='IDClienteVendedor', primary_key=True)  # Field name made lowercase.
    seg = models.CharField(db_column='Seg', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    ter = models.CharField(db_column='Ter', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    qua = models.CharField(db_column='Qua', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    qui = models.CharField(db_column='Qui', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    sex = models.CharField(db_column='Sex', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    sab = models.CharField(db_column='Sab', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    dom = models.CharField(db_column='Dom', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    hora1 = models.CharField(db_column='Hora1', max_length=5, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    hora2 = models.CharField(db_column='Hora2', max_length=5, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    recorrencia = models.CharField(db_column='Recorrencia', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ClienteVisita'


class Codigovenda(models.Model):
    idcodigovenda = models.AutoField(db_column='IDCodigoVenda', primary_key=True)  # Field name made lowercase.
    descodigovenda = models.CharField(db_column='DesCodigoVenda', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    coderp = models.CharField(db_column='CodERP', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    situacao = models.CharField(db_column='Situacao', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CodigoVenda'


class Comissaodifere(models.Model):
    idcomdifere = models.AutoField(db_column='IDComDifere', primary_key=True)  # Field name made lowercase. The composite primary key (IDComDifere, IDPolComissao) found, that is not supported. The first column is selected.
    idpolcomissao = models.ForeignKey('Politicacomissao', models.DO_NOTHING, db_column='IDPolComissao')  # Field name made lowercase.
    familia = models.ForeignKey('Familia', models.DO_NOTHING, db_column='Familia', blank=True, null=True)  # Field name made lowercase.
    ggrupo = models.ForeignKey('Grandegrupo', models.DO_NOTHING, db_column='GGrupo', blank=True, null=True)  # Field name made lowercase.
    grupo = models.ForeignKey('Grupo', models.DO_NOTHING, db_column='Grupo', blank=True, null=True)  # Field name made lowercase.
    sgrupo = models.ForeignKey('Subgrupo', models.DO_NOTHING, db_column='Sgrupo', blank=True, null=True)  # Field name made lowercase.
    marca = models.ForeignKey('Tabgeral', models.DO_NOTHING, db_column='Marca', blank=True, null=True)  # Field name made lowercase.
    categoria = models.ForeignKey(Categoria, models.DO_NOTHING, db_column='Categoria', blank=True, null=True)  # Field name made lowercase.
    fabricante = models.ForeignKey('Tabgeral', models.DO_NOTHING, db_column='Fabricante', related_name='comissaodifere_fabricante_set', blank=True, null=True)  # Field name made lowercase.
    origem = models.ForeignKey('Tabgeral', models.DO_NOTHING, db_column='Origem', related_name='comissaodifere_origem_set', blank=True, null=True)  # Field name made lowercase.
    idlinha = models.ForeignKey('Linhaproduto', models.DO_NOTHING, db_column='IDLinha', blank=True, null=True)  # Field name made lowercase.
    percomissao = models.DecimalField(db_column='PerComissao', max_digits=4, decimal_places=2)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ComissaoDifere'
        unique_together = (('idcomdifere', 'idpolcomissao'),)


class Configparametro(models.Model):
    idconfparametro = models.AutoField(db_column='IDConfParametro', primary_key=True)  # Field name made lowercase.
    idconfiguracao = models.ForeignKey('Configuracao', models.DO_NOTHING, db_column='IDConfiguracao')  # Field name made lowercase.
    parametro = models.CharField(db_column='Parametro', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    valor = models.CharField(db_column='Valor', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ConfigParametro'


class Configuracao(models.Model):
    idconfiguracao = models.AutoField(db_column='IDConfiguracao', primary_key=True)  # Field name made lowercase.
    token = models.CharField(db_column='Token', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    usuario = models.CharField(db_column='Usuario', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    senha = models.CharField(db_column='Senha', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    versaoerp = models.CharField(db_column='VersaoERP', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    entidade = models.IntegerField(db_column='Entidade', blank=True, null=True)  # Field name made lowercase.
    cnpjdesenvolvedor = models.CharField(db_column='CNPJDesenvolvedor', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    tokendesenvolvedor = models.CharField(db_column='TokenDesenvolvedor', max_length=40, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    tipoboleto = models.IntegerField(db_column='TipoBoleto', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Configuracao'


class Configuracaofiscal(models.Model):
    idconfiguracaofiscal = models.BigAutoField(db_column='IDConfiguracaoFiscal')  # Field name made lowercase.
    idtabelafiscal = models.ForeignKey('Tabelafiscal', models.DO_NOTHING, db_column='IDTabelaFiscal')  # Field name made lowercase.
    descconfiguracaofiscal = models.CharField(db_column='DescConfiguracaoFiscal', max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    idtipopedido = models.IntegerField(db_column='IDTipoPedido')  # Field name made lowercase.
    produtoorigem = models.SmallIntegerField(db_column='ProdutoOrigem')  # Field name made lowercase.
    produtotipo = models.IntegerField(db_column='ProdutoTipo')  # Field name made lowercase.
    ufdestino = models.CharField(db_column='UFDestino', max_length=2, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    destinacao = models.IntegerField(db_column='Destinacao', blank=True, null=True)  # Field name made lowercase.
    orgaopublico = models.CharField(db_column='OrgaoPublico', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    presencacomprador = models.IntegerField(db_column='PresencaComprador')  # Field name made lowercase.
    contribuinteicms = models.CharField(db_column='ContribuinteICMS', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    usasuframa = models.CharField(db_column='UsaSuframa', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    usaregimeespecial = models.CharField(db_column='UsaRegimeEspecial', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    codcfop = models.ForeignKey(Cfop, models.DO_NOTHING, db_column='CodCFOP')  # Field name made lowercase.
    idicmscst = models.CharField(db_column='IDICMSCST', max_length=4, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    idicmstipobase = models.CharField(db_column='IDICMSTipoBase', max_length=4, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    pricmsreducaobase = models.DecimalField(db_column='PRICMSReducaoBase', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    pricms = models.DecimalField(db_column='PRICMS', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    pricmsfcp = models.DecimalField(db_column='PRICMSFCP', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    pricmsdiferimento = models.DecimalField(db_column='PRICMSDiferimento', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    pricmsdifal = models.DecimalField(db_column='PRICMSDIFAL', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    pricmsdifalfcp = models.DecimalField(db_column='PRICMSDIFALFCP', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    pricmsdifalpartilha = models.DecimalField(db_column='PRICMSDIFALPartilha', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    pricmsdesoneracao = models.DecimalField(db_column='PRICMSDesoneracao', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    idicmsmotivodesoneracao = models.IntegerField(db_column='IDICMSMotivoDesoneracao', blank=True, null=True)  # Field name made lowercase.
    idicmssttipobase = models.CharField(db_column='IDICMSSTTipoBase', max_length=4, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    pricmsstreducaobase = models.DecimalField(db_column='PRICMSSTReducaoBase', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    pricmsst = models.DecimalField(db_column='PRICMSST', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    usaicmsstcargamedia = models.CharField(db_column='UsaICMSSTCargaMedia', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    pricmsstmvainterno = models.DecimalField(db_column='PRICMSSTMVAInterno', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    pricmsstreducao = models.DecimalField(db_column='PRICMSSTReducao', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    pricmsstmvasimplesinterno = models.DecimalField(db_column='PRICMSSTMVASimplesInterno', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    pricmsstreducaosimples = models.DecimalField(db_column='PRICMSSTReducaoSimples', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    pricmsstmva = models.DecimalField(db_column='PRICMSSTMVA', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    idipicst = models.CharField(db_column='IDIPICST', max_length=4, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    idipicenq = models.CharField(db_column='IDIPICENQ', max_length=4, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    pripi = models.DecimalField(db_column='PRIPI', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    vlipipauta = models.DecimalField(db_column='VlIPIPauta', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    usaipidecendial = models.CharField(db_column='UsaIPIDecendial', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    idpiscst = models.CharField(db_column='IDPISCST', max_length=4, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    prpis = models.DecimalField(db_column='PRPIS', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    prpisst = models.DecimalField(db_column='PRPISST', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    vlpisstpauta = models.DecimalField(db_column='VlPISSTPauta', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    idcofinscst = models.CharField(db_column='IDCOFINSCST', max_length=4, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    prcofins = models.DecimalField(db_column='PRCOFINS', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    prcofinsst = models.DecimalField(db_column='PRCOFINSST', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    vlcofinsstpauta = models.DecimalField(db_column='VlCOFINSSTPauta', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    dtinclusao = models.DateField(db_column='DtInclusao')  # Field name made lowercase.
    situacao = models.CharField(db_column='Situacao', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    icmssomaipi = models.CharField(db_column='ICMSSomaIPI', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    pissomaicms = models.CharField(db_column='PISSomaICMS', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    cofinssomaicms = models.CharField(db_column='COFINSSomaICMS', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    pricmsfcpufdestino = models.DecimalField(db_column='PRICMSFCPUFDestino', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    pricmsfcpst = models.DecimalField(db_column='PRICMSFCPST', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    pricmsfcpretido = models.DecimalField(db_column='PRICMSFCPRetido', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    usaicmsstpauta = models.CharField(db_column='UsaICMSSTPauta', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    pricmsstmvainterestadual = models.DecimalField(db_column='PRICMSSTMVAInterestadual', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    pricmsstmvasimplesinterestadual = models.DecimalField(db_column='PRICMSSTMVASimplesInterestadual', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    pricmsdifalreducao = models.DecimalField(db_column='PRICMSDIFALReducao', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    usachavenatural = models.CharField(db_column='UsaChavenatural', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    usaicmsefetivo = models.CharField(db_column='UsaICMSEfetivo', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    dtalteracao = models.DateTimeField(db_column='DtAlteracao', blank=True, null=True)  # Field name made lowercase.
    usaicmsstvalorreferencia = models.CharField(db_column='UsaICMSSTValorReferencia', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    descontardesoneracao = models.CharField(db_column='DescontarDesoneracao', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    pricmsdifalinterestadual = models.DecimalField(db_column='PRICMSDifalInterestadual', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    idconfiguracaofiscalcbenef = models.BigIntegerField(db_column='IDConfiguracaofiscalcbenef', blank=True, null=True)  # Field name made lowercase.
    pricmsfcpdiferimento = models.DecimalField(db_column='PRICMSFCPDiferimento', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    piscofinssomanota = models.CharField(db_column='PISCOFINSSomaNota', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    idicmsstmotivodesoneracao = models.IntegerField(db_column='IDICMSSTMotivoDesoneracao', blank=True, null=True)  # Field name made lowercase.
    somaracrescimobase = models.CharField(db_column='SomarAcrescimoBase', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ConfiguracaoFiscal'


class Contacorrente(models.Model):
    idcontacorrente = models.BigAutoField(db_column='IDContaCorrente', primary_key=True)  # Field name made lowercase.
    idcliente = models.IntegerField(db_column='IDCliente')  # Field name made lowercase.
    idlocal = models.IntegerField(db_column='IDLocal')  # Field name made lowercase.
    documento = models.CharField(db_column='Documento', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    dtlancamento = models.DateField(db_column='DtLancamento')  # Field name made lowercase.
    vllancamento = models.DecimalField(db_column='VlLancamento', max_digits=19, decimal_places=4)  # Field name made lowercase.
    sinal = models.CharField(db_column='Sinal', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    origemmovimento = models.CharField(db_column='OrigemMovimento', max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ContaCorrente'


class Contacorrentesaldo(models.Model):
    idcliente = models.IntegerField(db_column='IDCliente', primary_key=True)  # Field name made lowercase. The composite primary key (IDCliente, IDLocal) found, that is not supported. The first column is selected.
    idlocal = models.IntegerField(db_column='IDLocal')  # Field name made lowercase.
    vlsaldo = models.DecimalField(db_column='VlSaldo', max_digits=19, decimal_places=4)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ContaCorrenteSaldo'
        unique_together = (('idcliente', 'idlocal'),)


class Controleapi(models.Model):
    idcontroleapi = models.BigAutoField(db_column='IDControleAPI', primary_key=True)  # Field name made lowercase.
    integracao = models.IntegerField(db_column='Integracao', blank=True, null=True)  # Field name made lowercase.
    dhintegracao = models.DateTimeField(db_column='DhIntegracao')  # Field name made lowercase.
    jnentrada = models.TextField(db_column='JNEntrada', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    evento = models.CharField(db_column='Evento', max_length=6, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    mensagem = models.CharField(db_column='Mensagem', max_length=2000, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    idusuario = models.IntegerField(db_column='IDUsuario', blank=True, null=True)  # Field name made lowercase.
    tempo = models.IntegerField(db_column='Tempo', blank=True, null=True)  # Field name made lowercase.
    geral = models.CharField(db_column='Geral', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    origem = models.CharField(db_column='Origem', max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    idoperacao = models.CharField(db_column='IDOperacao', max_length=36, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ControleAPI'


class Correlato(models.Model):
    idproduto = models.OneToOneField('Produto', models.DO_NOTHING, db_column='IDProduto', primary_key=True)  # Field name made lowercase. The composite primary key (IDProduto, IDCorrelato) found, that is not supported. The first column is selected.
    idcorrelato = models.IntegerField(db_column='IDCorrelato')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Correlato'
        unique_together = (('idproduto', 'idcorrelato'),)


class Credito(models.Model):
    idcredito = models.AutoField(db_column='IDCredito', primary_key=True)  # Field name made lowercase.
    idcliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='IDCliente')  # Field name made lowercase.
    idlocal = models.ForeignKey('LocalVenda', models.DO_NOTHING, db_column='IDLocal')  # Field name made lowercase.
    tipocredito = models.CharField(db_column='TipoCredito', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    vlcredito = models.DecimalField(db_column='VlCredito', max_digits=19, decimal_places=4)  # Field name made lowercase.
    dtvencimento = models.DateField(db_column='DtVencimento', blank=True, null=True)  # Field name made lowercase.
    observacao = models.CharField(db_column='Observacao', max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Credito'


class Debito(models.Model):
    idcarteira = models.AutoField(db_column='IDCarteira', primary_key=True)  # Field name made lowercase.
    idcliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='IDCliente')  # Field name made lowercase.
    idlocal = models.ForeignKey('LocalVenda', models.DO_NOTHING, db_column='IDLocal')  # Field name made lowercase.
    nrdanfe = models.IntegerField(db_column='NrDANFE')  # Field name made lowercase.
    dtdanfe = models.DateField(db_column='DtDANFE')  # Field name made lowercase.
    nrtitulo = models.IntegerField(db_column='NrTitulo')  # Field name made lowercase.
    nrparcela = models.IntegerField(db_column='NrParcela')  # Field name made lowercase.
    dtvencimento = models.DateField(db_column='DtVencimento')  # Field name made lowercase.
    vltitulo = models.DecimalField(db_column='VlTitulo', max_digits=19, decimal_places=4)  # Field name made lowercase.
    vlsaldo = models.DecimalField(db_column='VlSaldo', max_digits=19, decimal_places=4)  # Field name made lowercase.
    observacao = models.CharField(db_column='Observacao', max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Debito'


class Embcaixa(models.Model):
    idproduto = models.OneToOneField('Produto', models.DO_NOTHING, db_column='IDProduto', primary_key=True)  # Field name made lowercase. The composite primary key (IDProduto, CodEmbalagem) found, that is not supported. The first column is selected.
    codembalagem = models.IntegerField(db_column='CodEmbalagem')  # Field name made lowercase.
    qtcaixa = models.IntegerField(db_column='QtCaixa', blank=True, null=True)  # Field name made lowercase.
    pesobruto = models.DecimalField(db_column='PesoBruto', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pesoliquido = models.DecimalField(db_column='PesoLiquido', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    largura = models.DecimalField(db_column='Largura', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    altura = models.DecimalField(db_column='Altura', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    comprimento = models.DecimalField(db_column='Comprimento', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    m3 = models.DecimalField(db_column='M3', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    codgtin = models.CharField(db_column='CodGTIN', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EmbCaixa'
        unique_together = (('idproduto', 'codembalagem'),)


class Embunidade(models.Model):
    idproduto = models.OneToOneField('Produto', models.DO_NOTHING, db_column='IDProduto', primary_key=True)  # Field name made lowercase.
    unidade = models.IntegerField(db_column='Unidade')  # Field name made lowercase.
    pesobruto = models.DecimalField(db_column='PesoBruto', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pesoliquido = models.DecimalField(db_column='PesoLiquido', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    largura = models.DecimalField(db_column='Largura', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    altura = models.DecimalField(db_column='Altura', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    comprimento = models.DecimalField(db_column='Comprimento', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    m3 = models.DecimalField(db_column='M3', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    codgtin = models.CharField(db_column='CodGTIN', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    fcvenda = models.DecimalField(db_column='FCVenda', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    unimedida = models.CharField(db_column='UniMedida', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    minvenda = models.DecimalField(db_column='MinVenda', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    multvenda = models.DecimalField(db_column='MultVenda', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    qtcaixa = models.DecimalField(db_column='QTCaixa', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EmbUnidade'


class Equipevendedor(models.Model):
    idequipe = models.IntegerField(db_column='IDEquipe', primary_key=True)  # Field name made lowercase. The composite primary key (IDEquipe, IDUsuario) found, that is not supported. The first column is selected.
    idusuario = models.IntegerField(db_column='IDUsuario')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EquipeVendedor'
        unique_together = (('idequipe', 'idusuario'),)


class FrAcao(models.Model):
    aco_codigo = models.IntegerField(db_column='ACO_CODIGO', primary_key=True)  # Field name made lowercase.
    aco_nome = models.CharField(db_column='ACO_NOME', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FR_ACAO'


class FrAcaocomponente(models.Model):
    frm_codigo = models.OneToOneField('FrComponente', models.DO_NOTHING, db_column='FRM_CODIGO', primary_key=True)  # Field name made lowercase. The composite primary key (FRM_CODIGO, COM_CODIGO, ACO_CODIGO, ACC_MOMENTO) found, that is not supported. The first column is selected.
    com_codigo = models.ForeignKey('FrComponente', models.DO_NOTHING, db_column='COM_CODIGO', related_name='fracaocomponente_com_codigo_set')  # Field name made lowercase.
    aco_codigo = models.ForeignKey(FrAcao, models.DO_NOTHING, db_column='ACO_CODIGO')  # Field name made lowercase.
    acc_momento = models.CharField(db_column='ACC_MOMENTO', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    acc_condicao = models.CharField(db_column='ACC_CONDICAO', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FR_ACAOCOMPONENTE'
        unique_together = (('frm_codigo', 'com_codigo', 'aco_codigo', 'acc_momento'),)


class FrAcaoparametro(models.Model):
    aco_codigo = models.OneToOneField(FrAcao, models.DO_NOTHING, db_column='ACO_CODIGO', primary_key=True)  # Field name made lowercase. The composite primary key (ACO_CODIGO, ACP_NOME) found, that is not supported. The first column is selected.
    acp_nome = models.CharField(db_column='ACP_NOME', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    act_codigo = models.ForeignKey('FrAcptipo', models.DO_NOTHING, db_column='ACT_CODIGO')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FR_ACAOPARAMETRO'
        unique_together = (('aco_codigo', 'acp_nome'),)


class FrAcptipo(models.Model):
    act_codigo = models.IntegerField(db_column='ACT_CODIGO', primary_key=True)  # Field name made lowercase.
    act_descricao = models.CharField(db_column='ACT_DESCRICAO', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FR_ACPTIPO'


class FrCampo(models.Model):
    tab_nome = models.OneToOneField('FrTabela', models.DO_NOTHING, db_column='TAB_NOME', primary_key=True)  # Field name made lowercase. The composite primary key (TAB_NOME, CMP_NOME) found, that is not supported. The first column is selected.
    cmp_nome = models.CharField(db_column='CMP_NOME', max_length=96, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    cmp_descricao = models.CharField(db_column='CMP_DESCRICAO', max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    cmp_valorpadrao = models.CharField(db_column='CMP_VALORPADRAO', max_length=60, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    tpd_codigo = models.IntegerField(db_column='TPD_CODIGO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FR_CAMPO'
        unique_together = (('tab_nome', 'cmp_nome'),)


class FrCategoria(models.Model):
    cat_codigo = models.IntegerField(db_column='CAT_CODIGO', primary_key=True)  # Field name made lowercase.
    cat_nome = models.CharField(db_column='CAT_NOME', max_length=60, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FR_CATEGORIA'


class FrCompilador(models.Model):
    cpl_descritor = models.CharField(db_column='CPL_DESCRITOR', primary_key=True, max_length=80, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    cpl_especificacao = models.CharField(db_column='CPL_ESPECIFICACAO', max_length=350, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FR_COMPILADOR'


class FrCompiladorDatabase(models.Model):
    cpl_descritor = models.OneToOneField(FrCompilador, models.DO_NOTHING, db_column='CPL_DESCRITOR', primary_key=True)  # Field name made lowercase. The composite primary key (CPL_DESCRITOR, DBA_CODIGO) found, that is not supported. The first column is selected.
    dba_codigo = models.ForeignKey('FrDatabase', models.DO_NOTHING, db_column='DBA_CODIGO')  # Field name made lowercase.
    cdb_sintaxe = models.CharField(db_column='CDB_SINTAXE', max_length=2000, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FR_COMPILADOR_DATABASE'
        unique_together = (('cpl_descritor', 'dba_codigo'),)


class FrComponente(models.Model):
    frm_codigo = models.OneToOneField('FrFormulario', models.DO_NOTHING, db_column='FRM_CODIGO', primary_key=True)  # Field name made lowercase. The composite primary key (FRM_CODIGO, COM_CODIGO) found, that is not supported. The first column is selected.
    com_codigo = models.IntegerField(db_column='COM_CODIGO')  # Field name made lowercase.
    img_codigo = models.IntegerField(db_column='IMG_CODIGO', blank=True, null=True)  # Field name made lowercase.
    com_tipo = models.CharField(db_column='COM_TIPO', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FR_COMPONENTE'
        unique_together = (('frm_codigo', 'com_codigo'),)


class FrComponenteCategoria(models.Model):
    frm_codigo = models.IntegerField(db_column='FRM_CODIGO', primary_key=True)  # Field name made lowercase. The composite primary key (FRM_CODIGO, COM_CODIGO, CAT_CODIGO) found, that is not supported. The first column is selected.
    com_codigo = models.IntegerField(db_column='COM_CODIGO')  # Field name made lowercase.
    cat_codigo = models.ForeignKey(FrCategoria, models.DO_NOTHING, db_column='CAT_CODIGO')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FR_COMPONENTE_CATEGORIA'
        unique_together = (('frm_codigo', 'com_codigo', 'cat_codigo'),)


class FrConfiguracao(models.Model):
    cnf_codigo = models.IntegerField(db_column='CNF_CODIGO', primary_key=True)  # Field name made lowercase.
    cnf_versiona_formulario = models.IntegerField(db_column='CNF_VERSIONA_FORMULARIO')  # Field name made lowercase.
    cnf_versiona_relatorio = models.IntegerField(db_column='CNF_VERSIONA_RELATORIO')  # Field name made lowercase.
    cnf_versiona_regra = models.IntegerField(db_column='CNF_VERSIONA_REGRA')  # Field name made lowercase.
    cnf_maker_version = models.CharField(db_column='CNF_MAKER_VERSION', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FR_CONFIGURACAO'


class FrConsultaAvancada(models.Model):
    frm_codigo = models.OneToOneField('FrFormulario', models.DO_NOTHING, db_column='FRM_CODIGO', primary_key=True)  # Field name made lowercase. The composite primary key (FRM_CODIGO, CAV_CODIGO) found, that is not supported. The first column is selected.
    cav_codigo = models.IntegerField(db_column='CAV_CODIGO')  # Field name made lowercase.
    cav_descricao = models.CharField(db_column='CAV_DESCRICAO', max_length=60, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    cav_texto = models.TextField(db_column='CAV_TEXTO', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FR_CONSULTA_AVANCADA'
        unique_together = (('frm_codigo', 'cav_codigo'),)


class FrDatabase(models.Model):
    dba_codigo = models.CharField(db_column='DBA_CODIGO', primary_key=True, max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    dba_descricao = models.CharField(db_column='DBA_DESCRICAO', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FR_DATABASE'


class FrDepFormularioCampo(models.Model):
    frm_codigo = models.IntegerField(db_column='FRM_CODIGO', primary_key=True)  # Field name made lowercase. The composite primary key (FRM_CODIGO, TAB_NOME, CMP_NOME) found, that is not supported. The first column is selected.
    tab_nome = models.CharField(db_column='TAB_NOME', max_length=96, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    cmp_nome = models.CharField(db_column='CMP_NOME', max_length=96, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FR_DEP_FORMULARIO_CAMPO'
        unique_together = (('frm_codigo', 'tab_nome', 'cmp_nome'),)


class FrDepFormularioFormulario(models.Model):
    frm_codigo = models.IntegerField(db_column='FRM_CODIGO', primary_key=True)  # Field name made lowercase. The composite primary key (FRM_CODIGO, FRM_CODIGO_REFERENCIA) found, that is not supported. The first column is selected.
    frm_codigo_referencia = models.IntegerField(db_column='FRM_CODIGO_REFERENCIA')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FR_DEP_FORMULARIO_FORMULARIO'
        unique_together = (('frm_codigo', 'frm_codigo_referencia'),)


class FrDepFormularioRegra(models.Model):
    frm_codigo = models.IntegerField(db_column='FRM_CODIGO', primary_key=True)  # Field name made lowercase. The composite primary key (FRM_CODIGO, REG_COD) found, that is not supported. The first column is selected.
    reg_cod = models.IntegerField(db_column='REG_COD')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FR_DEP_FORMULARIO_REGRA'
        unique_together = (('frm_codigo', 'reg_cod'),)


class FrDepFormularioRelatorio(models.Model):
    frm_codigo = models.IntegerField(db_column='FRM_CODIGO', primary_key=True)  # Field name made lowercase. The composite primary key (FRM_CODIGO, REL_CODIGO) found, that is not supported. The first column is selected.
    rel_codigo = models.IntegerField(db_column='REL_CODIGO')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FR_DEP_FORMULARIO_RELATORIO'
        unique_together = (('frm_codigo', 'rel_codigo'),)


class FrDepFormularioTabela(models.Model):
    frm_codigo = models.IntegerField(db_column='FRM_CODIGO', primary_key=True)  # Field name made lowercase. The composite primary key (FRM_CODIGO, TAB_NOME) found, that is not supported. The first column is selected.
    tab_nome = models.CharField(db_column='TAB_NOME', max_length=96, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FR_DEP_FORMULARIO_TABELA'
        unique_together = (('frm_codigo', 'tab_nome'),)


class FrDepRegraCampo(models.Model):
    reg_cod = models.IntegerField(db_column='REG_COD', primary_key=True)  # Field name made lowercase. The composite primary key (REG_COD, TAB_NOME, CMP_NOME) found, that is not supported. The first column is selected.
    tab_nome = models.CharField(db_column='TAB_NOME', max_length=96, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    cmp_nome = models.CharField(db_column='CMP_NOME', max_length=96, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FR_DEP_REGRA_CAMPO'
        unique_together = (('reg_cod', 'tab_nome', 'cmp_nome'),)


class FrDepRegraComponente(models.Model):
    reg_cod = models.IntegerField(db_column='REG_COD', primary_key=True)  # Field name made lowercase. The composite primary key (REG_COD, COM_CODIGO, FRM_CODIGO) found, that is not supported. The first column is selected.
    com_codigo = models.IntegerField(db_column='COM_CODIGO')  # Field name made lowercase.
    frm_codigo = models.IntegerField(db_column='FRM_CODIGO')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FR_DEP_REGRA_COMPONENTE'
        unique_together = (('reg_cod', 'com_codigo', 'frm_codigo'),)


class FrDepRegraFormulario(models.Model):
    reg_cod = models.IntegerField(db_column='REG_COD', primary_key=True)  # Field name made lowercase. The composite primary key (REG_COD, FRM_CODIGO) found, that is not supported. The first column is selected.
    frm_codigo = models.IntegerField(db_column='FRM_CODIGO')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FR_DEP_REGRA_FORMULARIO'
        unique_together = (('reg_cod', 'frm_codigo'),)


class FrDepRegraFuncao(models.Model):
    reg_cod = models.IntegerField(db_column='REG_COD', primary_key=True)  # Field name made lowercase. The composite primary key (REG_COD, FUN_COD) found, that is not supported. The first column is selected.
    fun_cod = models.IntegerField(db_column='FUN_COD')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FR_DEP_REGRA_FUNCAO'
        unique_together = (('reg_cod', 'fun_cod'),)


class FrDepRegraRegra(models.Model):
    reg_cod = models.IntegerField(db_column='REG_COD', primary_key=True)  # Field name made lowercase. The composite primary key (REG_COD, REG_COD_REFERENCIA) found, that is not supported. The first column is selected.
    reg_cod_referencia = models.IntegerField(db_column='REG_COD_REFERENCIA')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FR_DEP_REGRA_REGRA'
        unique_together = (('reg_cod', 'reg_cod_referencia'),)


class FrDepRegraRelatorio(models.Model):
    reg_cod = models.IntegerField(db_column='REG_COD', primary_key=True)  # Field name made lowercase. The composite primary key (REG_COD, REL_CODIGO) found, that is not supported. The first column is selected.
    rel_codigo = models.IntegerField(db_column='REL_CODIGO')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FR_DEP_REGRA_RELATORIO'
        unique_together = (('reg_cod', 'rel_codigo'),)


class FrDepRegraTabela(models.Model):
    reg_cod = models.IntegerField(db_column='REG_COD', primary_key=True)  # Field name made lowercase. The composite primary key (REG_COD, TAB_NOME) found, that is not supported. The first column is selected.
    tab_nome = models.CharField(db_column='TAB_NOME', max_length=96, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FR_DEP_REGRA_TABELA'
        unique_together = (('reg_cod', 'tab_nome'),)


class FrDiagrama(models.Model):
    dgr_cod = models.IntegerField(db_column='DGR_COD', primary_key=True)  # Field name made lowercase.
    dgr_nome = models.CharField(db_column='DGR_NOME', max_length=120, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    dgr_autor = models.CharField(db_column='DGR_AUTOR', max_length=80, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    dgr_versao = models.CharField(db_column='DGR_VERSAO', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    dgr_tipotabela = models.IntegerField(db_column='DGR_TIPOTABELA', blank=True, null=True)  # Field name made lowercase.
    dgr_datacriacao = models.DateTimeField(db_column='DGR_DATACRIACAO', blank=True, null=True)  # Field name made lowercase.
    dgr_atualizacao = models.DateTimeField(db_column='DGR_ATUALIZACAO', blank=True, null=True)  # Field name made lowercase.
    dgr_comentario = models.TextField(db_column='DGR_COMENTARIO', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    dgr_padraofk = models.IntegerField(db_column='DGR_PADRAOFK', blank=True, null=True)  # Field name made lowercase.
    dgr_layout = models.TextField(db_column='DGR_LAYOUT', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FR_DIAGRAMA'


class FrDocAprovacao(models.Model):
    apr_nome = models.CharField(db_column='APR_NOME', primary_key=True, max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase. The composite primary key (APR_NOME, DOC_CODIGO) found, that is not supported. The first column is selected.
    doc_codigo = models.ForeignKey('FrDocPrincipal', models.DO_NOTHING, db_column='DOC_CODIGO')  # Field name made lowercase.
    apr_cargo = models.CharField(db_column='APR_CARGO', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    apr_participacao = models.CharField(db_column='APR_PARTICIPACAO', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FR_DOC_APROVACAO'
        unique_together = (('apr_nome', 'doc_codigo'),)


class FrDocAtor(models.Model):
    ato_codigo = models.IntegerField(db_column='ATO_CODIGO', primary_key=True)  # Field name made lowercase. The composite primary key (ATO_CODIGO, DOC_CODIGO) found, that is not supported. The first column is selected.
    ato_frequencia_uso = models.CharField(db_column='ATO_FREQUENCIA_USO', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ato_nivel_instrucao = models.CharField(db_column='ATO_NIVEL_INSTRUCAO', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ato_nome = models.CharField(db_column='ATO_NOME', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ato_proficiencia_aplicacao = models.CharField(db_column='ATO_PROFICIENCIA_APLICACAO', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ato_proficiencia_informatica = models.CharField(db_column='ATO_PROFICIENCIA_INFORMATICA', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ato_usuario = models.IntegerField(db_column='ATO_USUARIO', blank=True, null=True)  # Field name made lowercase.
    doc_codigo = models.ForeignKey('FrDocPrincipal', models.DO_NOTHING, db_column='DOC_CODIGO')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FR_DOC_ATOR'
        unique_together = (('ato_codigo', 'doc_codigo'),)


class FrDocBeneficio(models.Model):
    ben_descricao = models.CharField(db_column='BEN_DESCRICAO', primary_key=True, max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase. The composite primary key (BEN_DESCRICAO, BEN_VALOR, DOC_CODIGO) found, that is not supported. The first column is selected.
    ben_valor = models.CharField(db_column='BEN_VALOR', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    doc_codigo = models.ForeignKey('FrDocPrincipal', models.DO_NOTHING, db_column='DOC_CODIGO')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FR_DOC_BENEFICIO'
        unique_together = (('ben_descricao', 'ben_valor', 'doc_codigo'),)


class FrDocCasoUso(models.Model):
    doc_codigo = models.OneToOneField('FrDocPrincipal', models.DO_NOTHING, db_column='DOC_CODIGO', primary_key=True)  # Field name made lowercase. The composite primary key (DOC_CODIGO, USO_CODIGO) found, that is not supported. The first column is selected.
    uso_codigo = models.IntegerField(db_column='USO_CODIGO')  # Field name made lowercase.
    uso_nome = models.CharField(db_column='USO_NOME', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    uso_descricao = models.TextField(db_column='USO_DESCRICAO', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    uso_requisito = models.TextField(db_column='USO_REQUISITO', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    uso_validacao = models.TextField(db_column='USO_VALIDACAO', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    uso_cenario = models.TextField(db_column='USO_CENARIO', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FR_DOC_CASO_USO'
        unique_together = (('doc_codigo', 'uso_codigo'),)


class FrDocCasoUsoAtor(models.Model):
    ato_codigo_ativo = models.OneToOneField(FrDocAtor, models.DO_NOTHING, db_column='ATO_CODIGO_ATIVO', primary_key=True)  # Field name made lowercase. The composite primary key (ATO_CODIGO_ATIVO, ATO_CODIGO_PASSIVO, CAS_USO_ATO_CODIGO, DOC_CODIGO, USO_CODIGO) found, that is not supported. The first column is selected.
    ato_codigo_passivo = models.IntegerField(db_column='ATO_CODIGO_PASSIVO')  # Field name made lowercase.
    cas_uso_ato_codigo = models.IntegerField(db_column='CAS_USO_ATO_CODIGO')  # Field name made lowercase.
    doc_codigo = models.ForeignKey(FrDocAtor, models.DO_NOTHING, db_column='DOC_CODIGO', to_field='DOC_CODIGO', related_name='frdoccasousoator_doc_codigo_set')  # Field name made lowercase.
    uso_codigo = models.IntegerField(db_column='USO_CODIGO')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FR_DOC_CASO_USO_ATOR'
        unique_together = (('ato_codigo_ativo', 'ato_codigo_passivo', 'cas_uso_ato_codigo', 'doc_codigo', 'uso_codigo'),)


class FrDocCasoUsoExtensao(models.Model):
    doc_codigo = models.OneToOneField(FrDocCasoUso, models.DO_NOTHING, db_column='DOC_CODIGO', primary_key=True)  # Field name made lowercase. The composite primary key (DOC_CODIGO, DOC_CODIGO, USO_CODIGO_PRINCIPAL, USO_CODIGO_EXTENDIDO) found, that is not supported. The first column is selected.
    uso_codigo_principal = models.ForeignKey(FrDocCasoUso, models.DO_NOTHING, db_column='USO_CODIGO_PRINCIPAL', to_field='USO_CODIGO', related_name='frdoccasousoextensao_uso_codigo_principal_set')  # Field name made lowercase.
    ext_condicao = models.CharField(db_column='EXT_CONDICAO', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    uso_codigo_extendido = models.ForeignKey(FrDocCasoUso, models.DO_NOTHING, db_column='USO_CODIGO_EXTENDIDO', to_field='USO_CODIGO', related_name='frdoccasousoextensao_uso_codigo_extendido_set')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FR_DOC_CASO_USO_EXTENSAO'
        unique_together = (('doc_codigo', 'doc_codigo', 'uso_codigo_principal', 'uso_codigo_extendido'),)


class FrDocCasoUsoGeneralizacao(models.Model):
    doc_codigo = models.OneToOneField(FrDocCasoUso, models.DO_NOTHING, db_column='DOC_CODIGO', primary_key=True)  # Field name made lowercase. The composite primary key (DOC_CODIGO, DOC_CODIGO, USO_CODIGO_HERDADOR, USO_CODIGO_HERDADO) found, that is not supported. The first column is selected.
    uso_codigo_herdador = models.ForeignKey(FrDocCasoUso, models.DO_NOTHING, db_column='USO_CODIGO_HERDADOR', to_field='USO_CODIGO', related_name='frdoccasousogeneralizacao_uso_codigo_herdador_set')  # Field name made lowercase.
    uso_codigo_herdado = models.ForeignKey(FrDocCasoUso, models.DO_NOTHING, db_column='USO_CODIGO_HERDADO', to_field='USO_CODIGO', related_name='frdoccasousogeneralizacao_uso_codigo_herdado_set')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FR_DOC_CASO_USO_GENERALIZACAO'
        unique_together = (('doc_codigo', 'doc_codigo', 'uso_codigo_herdador', 'uso_codigo_herdado'),)


class FrDocCasoUsoInclusao(models.Model):
    doc_codigo = models.OneToOneField(FrDocCasoUso, models.DO_NOTHING, db_column='DOC_CODIGO', primary_key=True)  # Field name made lowercase. The composite primary key (DOC_CODIGO, USO_CODIGO_PRINCIPAL, USO_CODIGO_SUB_CASO) found, that is not supported. The first column is selected.
    uso_codigo_principal = models.ForeignKey(FrDocCasoUso, models.DO_NOTHING, db_column='USO_CODIGO_PRINCIPAL', to_field='USO_CODIGO', related_name='frdoccasousoinclusao_uso_codigo_principal_set')  # Field name made lowercase.
    uso_codigo_sub_caso = models.IntegerField(db_column='USO_CODIGO_SUB_CASO')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FR_DOC_CASO_USO_INCLUSAO'
        unique_together = (('doc_codigo', 'uso_codigo_principal', 'uso_codigo_sub_caso'),)


class FrDocDiagramaContexto(models.Model):
    con_codigo = models.IntegerField(db_column='CON_CODIGO', primary_key=True)  # Field name made lowercase.
    con_descricao = models.CharField(db_column='CON_DESCRICAO', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    con_imagem = models.BinaryField(db_column='CON_IMAGEM', blank=True, null=True)  # Field name made lowercase.
    doc_codigo = models.ForeignKey('FrDocPrincipal', models.DO_NOTHING, db_column='DOC_CODIGO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FR_DOC_DIAGRAMA_CONTEXTO'


class FrDocDiagContCasUsoAto(models.Model):
    cas_uso_ato_codigo = models.IntegerField(db_column='CAS_USO_ATO_CODIGO', primary_key=True)  # Field name made lowercase. The composite primary key (CAS_USO_ATO_CODIGO, CON_CODIGO) found, that is not supported. The first column is selected.
    con_codigo = models.ForeignKey(FrDocDiagramaContexto, models.DO_NOTHING, db_column='CON_CODIGO')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FR_DOC_DIAG_CONT_CAS_USO_ATO'
        unique_together = (('cas_uso_ato_codigo', 'con_codigo'),)


class FrDocFormulario(models.Model):
    doc_codigo = models.OneToOneField('FrDocPrincipal', models.DO_NOTHING, db_column='DOC_CODIGO', primary_key=True)  # Field name made lowercase. The composite primary key (DOC_CODIGO, FRM_CODIGO) found, that is not supported. The first column is selected.
    frm_codigo = models.IntegerField(db_column='FRM_CODIGO')  # Field name made lowercase.
    frm_observacao = models.TextField(db_column='FRM_OBSERVACAO', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FR_DOC_FORMULARIO'
        unique_together = (('doc_codigo', 'frm_codigo'),)


class FrDocFormularioImagem(models.Model):
    doc_codigo = models.OneToOneField('FrDocPrincipal', models.DO_NOTHING, db_column='DOC_CODIGO', primary_key=True)  # Field name made lowercase. The composite primary key (DOC_CODIGO, FRM_CODIGO, FIM_ABA) found, that is not supported. The first column is selected.
    frm_codigo = models.IntegerField(db_column='FRM_CODIGO')  # Field name made lowercase.
    fim_aba = models.CharField(db_column='FIM_ABA', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    fim_aba_nome_original = models.CharField(db_column='FIM_ABA_NOME_ORIGINAL', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    fim_imagem = models.BinaryField(db_column='FIM_IMAGEM', blank=True, null=True)  # Field name made lowercase.
    fim_versao = models.CharField(db_column='FIM_VERSAO', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FR_DOC_FORMULARIO_IMAGEM'
        unique_together = (('doc_codigo', 'frm_codigo', 'fim_aba'),)


class FrDocHipoteseTrabalho(models.Model):
    ato_codigo = models.OneToOneField(FrDocAtor, models.DO_NOTHING, db_column='ATO_CODIGO', primary_key=True)  # Field name made lowercase. The composite primary key (ATO_CODIGO, DOC_CODIGO, TRA_DESCRICAO) found, that is not supported. The first column is selected.
    doc_codigo = models.ForeignKey(FrDocAtor, models.DO_NOTHING, db_column='DOC_CODIGO', to_field='DOC_CODIGO', related_name='frdochipotesetrabalho_doc_codigo_set')  # Field name made lowercase.
    tra_descricao = models.CharField(db_column='TRA_DESCRICAO', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FR_DOC_HIPOTESE_TRABALHO'
        unique_together = (('ato_codigo', 'doc_codigo', 'tra_descricao'),)


class FrDocInterface(models.Model):
    doc_codigo = models.OneToOneField('FrDocPrincipal', models.DO_NOTHING, db_column='DOC_CODIGO', primary_key=True)  # Field name made lowercase. The composite primary key (DOC_CODIGO, INT_DESCRICAO, INT_TIPO) found, that is not supported. The first column is selected.
    int_descricao = models.CharField(db_column='INT_DESCRICAO', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    int_tipo = models.CharField(db_column='INT_TIPO', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FR_DOC_INTERFACE'
        unique_together = (('doc_codigo', 'int_descricao', 'int_tipo'),)


class FrDocInterpretacaoCampo(models.Model):
    cam_padrao = models.CharField(db_column='CAM_PADRAO', primary_key=True, max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase. The composite primary key (CAM_PADRAO, CAM_TIPO, DOC_CODIGO) found, that is not supported. The first column is selected.
    cam_tipo = models.CharField(db_column='CAM_TIPO', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    doc_codigo = models.ForeignKey('FrDocPrincipal', models.DO_NOTHING, db_column='DOC_CODIGO')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FR_DOC_INTERPRETACAO_CAMPO'
        unique_together = (('cam_padrao', 'cam_tipo', 'doc_codigo'),)


class FrDocLimite(models.Model):
    doc_codigo = models.OneToOneField('FrDocPrincipal', models.DO_NOTHING, db_column='DOC_CODIGO', primary_key=True)  # Field name made lowercase. The composite primary key (DOC_CODIGO, LIM_DESCRICAO) found, that is not supported. The first column is selected.
    lim_descricao = models.CharField(db_column='LIM_DESCRICAO', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FR_DOC_LIMITE'
        unique_together = (('doc_codigo', 'lim_descricao'),)


class FrDocMaterialReferencia(models.Model):
    doc_codigo = models.OneToOneField('FrDocPrincipal', models.DO_NOTHING, db_column='DOC_CODIGO', primary_key=True)  # Field name made lowercase. The composite primary key (DOC_CODIGO, REF_BIBLIOGRAFIA, REF_TIPO) found, that is not supported. The first column is selected.
    ref_bibliografia = models.CharField(db_column='REF_BIBLIOGRAFIA', max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    ref_tipo = models.CharField(db_column='REF_TIPO', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FR_DOC_MATERIAL_REFERENCIA'
        unique_together = (('doc_codigo', 'ref_bibliografia', 'ref_tipo'),)


class FrDocModoOperacao(models.Model):
    doc_codigo = models.OneToOneField('FrDocPrincipal', models.DO_NOTHING, db_column='DOC_CODIGO', primary_key=True)  # Field name made lowercase. The composite primary key (DOC_CODIGO, OPE_DESCRICAO) found, that is not supported. The first column is selected.
    ope_descricao = models.CharField(db_column='OPE_DESCRICAO', max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FR_DOC_MODO_OPERACAO'
        unique_together = (('doc_codigo', 'ope_descricao'),)


class FrDocPrincipal(models.Model):
    doc_codigo = models.IntegerField(db_column='DOC_CODIGO', primary_key=True)  # Field name made lowercase.
    doc_autoria = models.CharField(db_column='DOC_AUTORIA', max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    sis_codigo = models.ForeignKey('FrSistema', models.DO_NOTHING, db_column='SIS_CODIGO', blank=True, null=True)  # Field name made lowercase.
    doc_data = models.CharField(db_column='DOC_DATA', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    doc_empresa = models.CharField(db_column='DOC_EMPRESA', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    doc_local = models.CharField(db_column='DOC_LOCAL', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    doc_modelo_dados = models.BinaryField(db_column='DOC_MODELO_DADOS', blank=True, null=True)  # Field name made lowercase.
    doc_objetivo = models.TextField(db_column='DOC_OBJETIVO', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    doc_missao = models.TextField(db_column='DOC_MISSAO', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    doc_componentes = models.TextField(db_column='DOC_COMPONENTES', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    doc_visao_geral = models.TextField(db_column='DOC_VISAO_GERAL', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    doc_convencoes = models.TextField(db_column='DOC_CONVENCOES', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    doc_observacoes = models.TextField(db_column='DOC_OBSERVACOES', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    doc_usuario_descricao = models.TextField(db_column='DOC_USUARIO_DESCRICAO', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FR_DOC_PRINCIPAL'


class FrDocRegrasImagem(models.Model):
    doc_codigo = models.OneToOneField(FrDocPrincipal, models.DO_NOTHING, db_column='DOC_CODIGO', primary_key=True)  # Field name made lowercase. The composite primary key (DOC_CODIGO, REG_COD) found, that is not supported. The first column is selected.
    reg_cod = models.ForeignKey('FrRegras', models.DO_NOTHING, db_column='REG_COD')  # Field name made lowercase.
    reg_dependencia = models.TextField(db_column='REG_DEPENDENCIA', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    reg_imagem = models.BinaryField(db_column='REG_IMAGEM', blank=True, null=True)  # Field name made lowercase.
    sis_cod = models.CharField(db_column='SIS_COD', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    reg_hash = models.CharField(db_column='REG_HASH', max_length=32, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FR_DOC_REGRAS_IMAGEM'
        unique_together = (('doc_codigo', 'reg_cod'),)


class FrDocRelatorio(models.Model):
    doc_codigo = models.OneToOneField(FrDocPrincipal, models.DO_NOTHING, db_column='DOC_CODIGO', primary_key=True)  # Field name made lowercase. The composite primary key (DOC_CODIGO, REL_CODIGO) found, that is not supported. The first column is selected.
    rel_codigo = models.ForeignKey('FrRelatorio', models.DO_NOTHING, db_column='REL_CODIGO')  # Field name made lowercase.
    rel_descricao = models.CharField(db_column='REL_DESCRICAO', max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    rel_objetivo = models.CharField(db_column='REL_OBJETIVO', max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    rel_imagem = models.BinaryField(db_column='REL_IMAGEM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FR_DOC_RELATORIO'
        unique_together = (('doc_codigo', 'rel_codigo'),)


class FrDocRequisito(models.Model):
    doc_codigo = models.OneToOneField(FrDocPrincipal, models.DO_NOTHING, db_column='DOC_CODIGO', primary_key=True)  # Field name made lowercase. The composite primary key (DOC_CODIGO, REQ_DESCRICAO, REQ_TIPO) found, that is not supported. The first column is selected.
    req_descricao = models.CharField(db_column='REQ_DESCRICAO', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    req_tipo = models.CharField(db_column='REQ_TIPO', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FR_DOC_REQUISITO'
        unique_together = (('doc_codigo', 'req_descricao', 'req_tipo'),)


class FrDocRestricao(models.Model):
    doc_codigo = models.OneToOneField(FrDocPrincipal, models.DO_NOTHING, db_column='DOC_CODIGO', primary_key=True)  # Field name made lowercase. The composite primary key (DOC_CODIGO, RES_DESCRICAO, RES_TIPO) found, that is not supported. The first column is selected.
    res_descricao = models.CharField(db_column='RES_DESCRICAO', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    res_tipo = models.CharField(db_column='RES_TIPO', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FR_DOC_RESTRICAO'
        unique_together = (('doc_codigo', 'res_descricao', 'res_tipo'),)


class FrDocVersao(models.Model):
    doc_codigo = models.OneToOneField(FrDocPrincipal, models.DO_NOTHING, db_column='DOC_CODIGO', primary_key=True)  # Field name made lowercase. The composite primary key (DOC_CODIGO, VER_DATA, VER_REVISADA) found, that is not supported. The first column is selected.
    ver_data = models.CharField(db_column='VER_DATA', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    ver_revisada = models.CharField(db_column='VER_REVISADA', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    ver_descricao = models.CharField(db_column='VER_DESCRICAO', max_length=2000, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FR_DOC_VERSAO'
        unique_together = (('doc_codigo', 'ver_data', 'ver_revisada'),)


class FrFontedados(models.Model):
    fnt_codigo = models.IntegerField(db_column='FNT_CODIGO', primary_key=True)  # Field name made lowercase.
    fnt_codigo_parent = models.IntegerField(db_column='FNT_CODIGO_PARENT', blank=True, null=True)  # Field name made lowercase.
    fnt_campochave = models.CharField(db_column='FNT_CAMPOCHAVE', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    fnt_tabela = models.CharField(db_column='FNT_TABELA', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    fnt_sqlselect = models.CharField(db_column='FNT_SQLSELECT', max_length=6000, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    fnt_sqlinsert = models.CharField(db_column='FNT_SQLINSERT', max_length=6000, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    fnt_sqlupdate = models.CharField(db_column='FNT_SQLUPDATE', max_length=6000, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    fnt_sqldelete = models.CharField(db_column='FNT_SQLDELETE', max_length=6000, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    fnt_campoincremento = models.CharField(db_column='FNT_CAMPOINCREMENTO', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    frm_codigo = models.ForeignKey('FrFormulario', models.DO_NOTHING, db_column='FRM_CODIGO')  # Field name made lowercase.
    fnt_campograde = models.CharField(db_column='FNT_CAMPOGRADE', max_length=6000, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    fnt_campopesquisa = models.CharField(db_column='FNT_CAMPOPESQUISA', max_length=6000, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    fnt_sqldefault = models.CharField(db_column='FNT_SQLDEFAULT', max_length=6000, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    fnt_sqlmascara = models.CharField(db_column='FNT_SQLMASCARA', max_length=2000, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FR_FONTEDADOS'


class FrFormulario(models.Model):
    frm_codigo = models.IntegerField(db_column='FRM_CODIGO', primary_key=True)  # Field name made lowercase.
    img_incluir = models.IntegerField(db_column='IMG_INCLUIR', blank=True, null=True)  # Field name made lowercase.
    img_alterar = models.IntegerField(db_column='IMG_ALTERAR', blank=True, null=True)  # Field name made lowercase.
    img_excluir = models.IntegerField(db_column='IMG_EXCLUIR', blank=True, null=True)  # Field name made lowercase.
    img_gravar = models.IntegerField(db_column='IMG_GRAVAR', blank=True, null=True)  # Field name made lowercase.
    img_gravar_mais = models.IntegerField(db_column='IMG_GRAVAR_MAIS', blank=True, null=True)  # Field name made lowercase.
    img_cancelar = models.IntegerField(db_column='IMG_CANCELAR', blank=True, null=True)  # Field name made lowercase.
    img_atualizar = models.IntegerField(db_column='IMG_ATUALIZAR', blank=True, null=True)  # Field name made lowercase.
    img_valores_padrao = models.IntegerField(db_column='IMG_VALORES_PADRAO', blank=True, null=True)  # Field name made lowercase.
    img_utilitario = models.IntegerField(db_column='IMG_UTILITARIO', blank=True, null=True)  # Field name made lowercase.
    img_log = models.IntegerField(db_column='IMG_LOG', blank=True, null=True)  # Field name made lowercase.
    img_sair = models.IntegerField(db_column='IMG_SAIR', blank=True, null=True)  # Field name made lowercase.
    img_imprimir = models.IntegerField(db_column='IMG_IMPRIMIR', blank=True, null=True)  # Field name made lowercase.
    img_ajuda = models.IntegerField(db_column='IMG_AJUDA', blank=True, null=True)  # Field name made lowercase.
    img_proximo = models.IntegerField(db_column='IMG_PROXIMO', blank=True, null=True)  # Field name made lowercase.
    img_ultimo = models.IntegerField(db_column='IMG_ULTIMO', blank=True, null=True)  # Field name made lowercase.
    img_primeiro = models.IntegerField(db_column='IMG_PRIMEIRO', blank=True, null=True)  # Field name made lowercase.
    img_anterior = models.IntegerField(db_column='IMG_ANTERIOR', blank=True, null=True)  # Field name made lowercase.
    frm_descricao = models.CharField(db_column='FRM_DESCRICAO', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    frm_tipo = models.CharField(db_column='FRM_TIPO', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    frm_posicaox = models.IntegerField(db_column='FRM_POSICAOX', blank=True, null=True)  # Field name made lowercase.
    frm_posicaoy = models.IntegerField(db_column='FRM_POSICAOY', blank=True, null=True)  # Field name made lowercase.
    frm_tamanho = models.IntegerField(db_column='FRM_TAMANHO', blank=True, null=True)  # Field name made lowercase.
    frm_altura = models.IntegerField(db_column='FRM_ALTURA', blank=True, null=True)  # Field name made lowercase.
    frm_tipo_criacao = models.CharField(db_column='FRM_TIPO_CRIACAO', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    frm_guid = models.CharField(db_column='FRM_GUID', max_length=38, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    rel_codigo = models.ForeignKey('FrRelatorio', models.DO_NOTHING, db_column='REL_CODIGO', blank=True, null=True)  # Field name made lowercase.
    usr_codigo = models.IntegerField(db_column='USR_CODIGO', blank=True, null=True)  # Field name made lowercase.
    frm_log = models.CharField(db_column='FRM_LOG', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FR_FORMULARIO'


class FrFormularioCategoria(models.Model):
    frm_codigo = models.OneToOneField(FrFormulario, models.DO_NOTHING, db_column='FRM_CODIGO', primary_key=True)  # Field name made lowercase. The composite primary key (FRM_CODIGO, CAT_CODIGO) found, that is not supported. The first column is selected.
    cat_codigo = models.ForeignKey(FrCategoria, models.DO_NOTHING, db_column='CAT_CODIGO')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FR_FORMULARIO_CATEGORIA'
        unique_together = (('frm_codigo', 'cat_codigo'),)


class FrFormularioSistema(models.Model):
    frm_codigo = models.OneToOneField(FrFormulario, models.DO_NOTHING, db_column='FRM_CODIGO', primary_key=True)  # Field name made lowercase. The composite primary key (FRM_CODIGO, SIS_CODIGO) found, that is not supported. The first column is selected.
    sis_codigo = models.ForeignKey('FrSistema', models.DO_NOTHING, db_column='SIS_CODIGO')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FR_FORMULARIO_SISTEMA'
        unique_together = (('frm_codigo', 'sis_codigo'),)


class FrGrupo(models.Model):
    grp_codigo = models.IntegerField(db_column='GRP_CODIGO', primary_key=True)  # Field name made lowercase. The composite primary key (GRP_CODIGO, SIS_CODIGO) found, that is not supported. The first column is selected.
    sis_codigo = models.CharField(db_column='SIS_CODIGO', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    grp_nome = models.CharField(db_column='GRP_NOME', max_length=40, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    grp_filtro_dicionario = models.CharField(db_column='GRP_FILTRO_DICIONARIO', max_length=2000, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FR_GRUPO'
        unique_together = (('grp_codigo', 'sis_codigo'),)


class FrHistoricoSql(models.Model):
    sql_codigo = models.IntegerField(db_column='SQL_CODIGO', primary_key=True)  # Field name made lowercase.
    sql_script = models.TextField(db_column='SQL_SCRIPT', db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    sql_data = models.DateTimeField(db_column='SQL_DATA')  # Field name made lowercase.
    sis_codigo = models.ForeignKey('FrSistema', models.DO_NOTHING, db_column='SIS_CODIGO')  # Field name made lowercase.
    sql_tabela = models.CharField(db_column='SQL_TABELA', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FR_HISTORICO_SQL'


class FrIdioma(models.Model):
    idi_codigo = models.IntegerField(db_column='IDI_CODIGO', primary_key=True)  # Field name made lowercase.
    idi_nome = models.CharField(db_column='IDI_NOME', max_length=60, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    idi_sigla = models.CharField(db_column='IDI_SIGLA', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    idi_ordem = models.IntegerField(db_column='IDI_ORDEM')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FR_IDIOMA'


class FrImagem(models.Model):
    img_codigo = models.IntegerField(db_column='IMG_CODIGO', primary_key=True)  # Field name made lowercase.
    img_imagem = models.BinaryField(db_column='IMG_IMAGEM')  # Field name made lowercase.
    img_guid = models.CharField(db_column='IMG_GUID', max_length=38, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FR_IMAGEM'


class FrLog(models.Model):
    log = models.CharField(db_column='LOG', max_length=6000, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FR_LOG'


class FrLogEvent(models.Model):
    log_id = models.IntegerField(db_column='LOG_ID', primary_key=True)  # Field name made lowercase.
    log_data = models.DateTimeField(db_column='LOG_DATA', blank=True, null=True)  # Field name made lowercase.
    log_hora = models.CharField(db_column='LOG_HORA', max_length=8, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    log_codform = models.IntegerField(db_column='LOG_CODFORM', blank=True, null=True)  # Field name made lowercase.
    log_descform = models.CharField(db_column='LOG_DESCFORM', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    log_operacao = models.CharField(db_column='LOG_OPERACAO', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    log_usuario = models.CharField(db_column='LOG_USUARIO', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    log_sistema = models.CharField(db_column='LOG_SISTEMA', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    log_chave = models.CharField(db_column='LOG_CHAVE', max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    log_chavecont = models.CharField(db_column='LOG_CHAVECONT', max_length=128, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    log_conteudo = models.TextField(db_column='LOG_CONTEUDO', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    log_ip = models.CharField(db_column='LOG_IP', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FR_LOG_EVENT'


class FrMenu(models.Model):
    sis_codigo = models.OneToOneField('FrSistema', models.DO_NOTHING, db_column='SIS_CODIGO', primary_key=True)  # Field name made lowercase. The composite primary key (SIS_CODIGO, MNU_CODIGO) found, that is not supported. The first column is selected.
    mnu_codigo = models.IntegerField(db_column='MNU_CODIGO')  # Field name made lowercase.
    mnu_descricao = models.CharField(db_column='MNU_DESCRICAO', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    mnu_codigo_parent = models.IntegerField(db_column='MNU_CODIGO_PARENT', blank=True, null=True)  # Field name made lowercase.
    mnu_indice = models.IntegerField(db_column='MNU_INDICE')  # Field name made lowercase.
    frm_codigo = models.ForeignKey(FrFormulario, models.DO_NOTHING, db_column='FRM_CODIGO', blank=True, null=True)  # Field name made lowercase.
    mnu_tecla = models.CharField(db_column='MNU_TECLA', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    img_codigo = models.IntegerField(db_column='IMG_CODIGO', blank=True, null=True)  # Field name made lowercase.
    mnu_separador = models.CharField(db_column='MNU_SEPARADOR', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    mnu_guid = models.CharField(db_column='MNU_GUID', max_length=38, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    mnu_tipo = models.CharField(db_column='MNU_TIPO', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    rel_codigo = models.IntegerField(db_column='REL_CODIGO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FR_MENU'
        unique_together = (('sis_codigo', 'mnu_codigo'),)


class FrOperador(models.Model):
    opdr_codigo = models.IntegerField(db_column='OPDR_CODIGO', primary_key=True)  # Field name made lowercase.
    opdr_nome = models.CharField(db_column='OPDR_NOME', max_length=40, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    opdr_tipo = models.CharField(db_column='OPDR_TIPO', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    opdr_parametros = models.CharField(db_column='OPDR_PARAMETROS', max_length=80, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FR_OPERADOR'


class FrOperando(models.Model):
    fmla_codigo = models.IntegerField(db_column='FMLA_CODIGO', primary_key=True)  # Field name made lowercase. The composite primary key (FMLA_CODIGO, OPDO_ORDEM) found, that is not supported. The first column is selected.
    opdo_ordem = models.IntegerField(db_column='OPDO_ORDEM')  # Field name made lowercase.
    opdo_fmla_codigo = models.IntegerField(db_column='OPDO_FMLA_CODIGO', blank=True, null=True)  # Field name made lowercase.
    opdo_expressao = models.CharField(db_column='OPDO_EXPRESSAO', max_length=6000, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FR_OPERANDO'
        unique_together = (('fmla_codigo', 'opdo_ordem'),)


class FrParametro(models.Model):
    frm_codigo = models.OneToOneField(FrAcaocomponente, models.DO_NOTHING, db_column='FRM_CODIGO', primary_key=True)  # Field name made lowercase. The composite primary key (FRM_CODIGO, COM_CODIGO, ACO_CODIGO, ACC_MOMENTO, PAR_NOME) found, that is not supported. The first column is selected.
    com_codigo = models.ForeignKey(FrAcaocomponente, models.DO_NOTHING, db_column='COM_CODIGO', related_name='frparametro_com_codigo_set')  # Field name made lowercase.
    aco_codigo = models.ForeignKey(FrAcaocomponente, models.DO_NOTHING, db_column='ACO_CODIGO', related_name='frparametro_aco_codigo_set')  # Field name made lowercase.
    acc_momento = models.ForeignKey(FrAcaocomponente, models.DO_NOTHING, db_column='ACC_MOMENTO', related_name='frparametro_acc_momento_set')  # Field name made lowercase.
    par_nome = models.CharField(db_column='PAR_NOME', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    par_valor = models.CharField(db_column='PAR_VALOR', max_length=5000, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FR_PARAMETRO'
        unique_together = (('frm_codigo', 'com_codigo', 'aco_codigo', 'acc_momento', 'par_nome'),)


class FrPermissao(models.Model):
    per_codigo = models.IntegerField(db_column='PER_CODIGO', primary_key=True)  # Field name made lowercase.
    grp_codigo = models.ForeignKey(FrGrupo, models.DO_NOTHING, db_column='GRP_CODIGO', to_field='SIS_CODIGO')  # Field name made lowercase.
    sis_codigo = models.ForeignKey(FrGrupo, models.DO_NOTHING, db_column='SIS_CODIGO', to_field='SIS_CODIGO', related_name='frpermissao_sis_codigo_set')  # Field name made lowercase.
    rel_codigo = models.ForeignKey('FrRelatorio', models.DO_NOTHING, db_column='REL_CODIGO', blank=True, null=True)  # Field name made lowercase.
    frm_codigo = models.ForeignKey(FrFormulario, models.DO_NOTHING, db_column='FRM_CODIGO', blank=True, null=True)  # Field name made lowercase.
    com_codigo = models.IntegerField(db_column='COM_CODIGO', blank=True, null=True)  # Field name made lowercase.
    mnu_codigo = models.IntegerField(db_column='MNU_CODIGO', blank=True, null=True)  # Field name made lowercase.
    per_adicionar = models.CharField(db_column='PER_ADICIONAR', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    per_excluir = models.CharField(db_column='PER_EXCLUIR', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    per_editar = models.CharField(db_column='PER_EDITAR', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    per_visualizar = models.CharField(db_column='PER_VISUALIZAR', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    per_habilitado = models.CharField(db_column='PER_HABILITADO', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FR_PERMISSAO'


class FrPermissaoMaker(models.Model):
    pmk_codigo = models.IntegerField(db_column='PMK_CODIGO')  # Field name made lowercase.
    grp_codigo = models.IntegerField(db_column='GRP_CODIGO')  # Field name made lowercase.
    pmk_editar = models.CharField(db_column='PMK_EDITAR', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    pmk_excluir = models.CharField(db_column='PMK_EXCLUIR', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    frm_codigo = models.IntegerField(db_column='FRM_CODIGO', blank=True, null=True)  # Field name made lowercase.
    rel_codigo = models.IntegerField(db_column='REL_CODIGO', blank=True, null=True)  # Field name made lowercase.
    reg_cod = models.IntegerField(db_column='REG_COD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FR_PERMISSAO_MAKER'


class FrPropriedade(models.Model):
    frm_codigo = models.OneToOneField(FrComponente, models.DO_NOTHING, db_column='FRM_CODIGO', primary_key=True)  # Field name made lowercase. The composite primary key (FRM_CODIGO, COM_CODIGO, PRO_NOME) found, that is not supported. The first column is selected.
    com_codigo = models.ForeignKey(FrComponente, models.DO_NOTHING, db_column='COM_CODIGO', related_name='frpropriedade_com_codigo_set')  # Field name made lowercase.
    pro_nome = models.CharField(db_column='PRO_NOME', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    pro_valor = models.TextField(db_column='PRO_VALOR', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FR_PROPRIEDADE'
        unique_together = (('frm_codigo', 'com_codigo', 'pro_nome'),)


class FrRegras(models.Model):
    reg_cod = models.IntegerField(db_column='REG_COD', primary_key=True)  # Field name made lowercase.
    reg_nome = models.CharField(db_column='REG_NOME', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    reg_descricao = models.TextField(db_column='REG_DESCRICAO', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    reg_params = models.TextField(db_column='REG_PARAMS', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    reg_variaveis = models.TextField(db_column='REG_VARIAVEIS', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    reg_params_out = models.TextField(db_column='REG_PARAMS_OUT', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    reg_interface = models.TextField(db_column='REG_INTERFACE', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    reg_script = models.TextField(db_column='REG_SCRIPT', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    reg_data = models.DateTimeField(db_column='REG_DATA', blank=True, null=True)  # Field name made lowercase.
    reg_hora = models.DateTimeField(db_column='REG_HORA', blank=True, null=True)  # Field name made lowercase.
    reg_compilada = models.CharField(db_column='REG_COMPILADA', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    reg_destino = models.IntegerField(db_column='REG_DESTINO', blank=True, null=True)  # Field name made lowercase.
    reg_hash = models.CharField(db_column='REG_HASH', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cat_cod = models.ForeignKey('FrRegrasCategorias', models.DO_NOTHING, db_column='CAT_COD', blank=True, null=True)  # Field name made lowercase.
    usr_codigo = models.IntegerField(db_column='USR_CODIGO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FR_REGRAS'


class FrRegrasAtividades(models.Model):
    atv_cod = models.IntegerField(db_column='ATV_COD', primary_key=True)  # Field name made lowercase.
    atv_nome = models.CharField(db_column='ATV_NOME', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    atv_nome_real = models.CharField(db_column='ATV_NOME_REAL', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    atv_descricao = models.CharField(db_column='ATV_DESCRICAO', max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    atv_params = models.CharField(db_column='ATV_PARAMS', max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    atv_retorno = models.CharField(db_column='ATV_RETORNO', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    atv_compatibilidade = models.CharField(db_column='ATV_COMPATIBILIDADE', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FR_REGRAS_ATIVIDADES'


class FrRegrasBanco(models.Model):
    reg_cod = models.IntegerField(db_column='REG_COD', primary_key=True)  # Field name made lowercase.
    ban_script = models.TextField(db_column='BAN_SCRIPT', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ban_compilacao = models.DateTimeField(db_column='BAN_COMPILACAO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FR_REGRAS_BANCO'


class FrRegrasCategorias(models.Model):
    cat_cod = models.IntegerField(db_column='CAT_COD', primary_key=True)  # Field name made lowercase.
    cat_nome = models.CharField(db_column='CAT_NOME', max_length=40, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cat_super = models.IntegerField(db_column='CAT_SUPER', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FR_REGRAS_CATEGORIAS'


class FrRegrasFuncoes(models.Model):
    fun_cod = models.IntegerField(db_column='FUN_COD', primary_key=True)  # Field name made lowercase.
    fun_nome = models.CharField(db_column='FUN_NOME', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    fun_descricao = models.TextField(db_column='FUN_DESCRICAO', db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    fun_nome_real = models.CharField(db_column='FUN_NOME_REAL', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    fun_params = models.TextField(db_column='FUN_PARAMS', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    fun_retorno = models.CharField(db_column='FUN_RETORNO', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    fun_tipo = models.IntegerField(db_column='FUN_TIPO')  # Field name made lowercase.
    fun_compatibilidade = models.CharField(db_column='FUN_COMPATIBILIDADE', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    fun_resumo = models.CharField(db_column='FUN_RESUMO', max_length=2000, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    fun_conteudo_servidor = models.TextField(db_column='FUN_CONTEUDO_SERVIDOR', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    fun_conteudo_cliente = models.TextField(db_column='FUN_CONTEUDO_CLIENTE', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    fun_conteudo_banco = models.TextField(db_column='FUN_CONTEUDO_BANCO', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    fun_versao = models.CharField(db_column='FUN_VERSAO', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FR_REGRAS_FUNCOES'


class FrRegrasFuncoesTipos(models.Model):
    ftp_cod = models.IntegerField(db_column='FTP_COD', primary_key=True)  # Field name made lowercase.
    ftp_nome = models.CharField(db_column='FTP_NOME', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FR_REGRAS_FUNCOES_TIPOS'


class FrRegrasTipos(models.Model):
    tip_cod = models.IntegerField(db_column='TIP_COD', primary_key=True)  # Field name made lowercase.
    tip_nome = models.CharField(db_column='TIP_NOME', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    tip_visivel = models.IntegerField(db_column='TIP_VISIVEL', blank=True, null=True)  # Field name made lowercase.
    tip_equivalente = models.CharField(db_column='TIP_EQUIVALENTE', max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    tip_aspas = models.IntegerField(db_column='TIP_ASPAS', blank=True, null=True)  # Field name made lowercase.
    tip_default = models.IntegerField(db_column='TIP_DEFAULT', blank=True, null=True)  # Field name made lowercase.
    tip_categoria = models.IntegerField(db_column='TIP_CATEGORIA', blank=True, null=True)  # Field name made lowercase.
    tip_super = models.IntegerField(db_column='TIP_SUPER', blank=True, null=True)  # Field name made lowercase.
    tip_nome_interno = models.CharField(db_column='TIP_NOME_INTERNO', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    tip_tam_obrigatorio = models.IntegerField(db_column='TIP_TAM_OBRIGATORIO', blank=True, null=True)  # Field name made lowercase.
    tip_visivel_param_entrada = models.IntegerField(db_column='TIP_VISIVEL_PARAM_ENTRADA', blank=True, null=True)  # Field name made lowercase.
    tip_visivel_var = models.IntegerField(db_column='TIP_VISIVEL_VAR', blank=True, null=True)  # Field name made lowercase.
    tip_visivel_const = models.IntegerField(db_column='TIP_VISIVEL_CONST', blank=True, null=True)  # Field name made lowercase.
    tip_visivel_param_saida = models.IntegerField(db_column='TIP_VISIVEL_PARAM_SAIDA', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FR_REGRAS_TIPOS'


class FrRegrasTriggers(models.Model):
    tab_nome = models.CharField(db_column='TAB_NOME', primary_key=True, max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase. The composite primary key (TAB_NOME, TAB_EVENTO, REG_COD) found, that is not supported. The first column is selected.
    tab_evento = models.IntegerField(db_column='TAB_EVENTO')  # Field name made lowercase.
    reg_cod = models.IntegerField(db_column='REG_COD')  # Field name made lowercase.
    tab_params = models.TextField(db_column='TAB_PARAMS', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    tab_script = models.TextField(db_column='TAB_SCRIPT', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    tab_compilacao = models.DateTimeField(db_column='TAB_COMPILACAO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FR_REGRAS_TRIGGERS'
        unique_together = (('tab_nome', 'tab_evento', 'reg_cod'),)


class FrRelatorio(models.Model):
    rel_codigo = models.IntegerField(db_column='REL_CODIGO', primary_key=True)  # Field name made lowercase.
    sis_codigo = models.CharField(db_column='SIS_CODIGO', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    rel_nome = models.CharField(db_column='REL_NOME', max_length=196, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    rel_conteudo = models.TextField(db_column='REL_CONTEUDO', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    rel_modificado = models.DateTimeField(db_column='REL_MODIFICADO', blank=True, null=True)  # Field name made lowercase.
    rel_tamanho = models.IntegerField(db_column='REL_TAMANHO', blank=True, null=True)  # Field name made lowercase.
    usr_codigo = models.IntegerField(db_column='USR_CODIGO')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FR_RELATORIO'


class FrRelatorioCategoria(models.Model):
    rel_codigo = models.IntegerField(db_column='REL_CODIGO', primary_key=True)  # Field name made lowercase. The composite primary key (REL_CODIGO, CAT_CODIGO) found, that is not supported. The first column is selected.
    cat_codigo = models.ForeignKey(FrCategoria, models.DO_NOTHING, db_column='CAT_CODIGO')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FR_RELATORIO_CATEGORIA'
        unique_together = (('rel_codigo', 'cat_codigo'),)


class FrSchema(models.Model):
    sch_nome = models.CharField(db_column='SCH_NOME', primary_key=True, max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    sch_versao = models.IntegerField(db_column='SCH_VERSAO')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FR_SCHEMA'


class FrSessao(models.Model):
    ses_conexao = models.IntegerField(db_column='SES_CONEXAO', primary_key=True)  # Field name made lowercase.
    ses_datahora_login = models.DateTimeField(db_column='SES_DATAHORA_LOGIN', blank=True, null=True)  # Field name made lowercase.
    ses_usuario = models.CharField(db_column='SES_USUARIO', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ses_nome_usuario = models.CharField(db_column='SES_NOME_USUARIO', max_length=40, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ses_nome_maquina = models.CharField(db_column='SES_NOME_MAQUINA', max_length=40, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ses_end_ip = models.CharField(db_column='SES_END_IP', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    sis_codigo = models.CharField(db_column='SIS_CODIGO', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FR_SESSAO'


class FrSistema(models.Model):
    sis_codigo = models.CharField(db_column='SIS_CODIGO', primary_key=True, max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    sis_descricao = models.CharField(db_column='SIS_DESCRICAO', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    img_codigo = models.ForeignKey(FrImagem, models.DO_NOTHING, db_column='IMG_CODIGO', blank=True, null=True)  # Field name made lowercase.
    img_codigo_icone = models.IntegerField(db_column='IMG_CODIGO_ICONE', blank=True, null=True)  # Field name made lowercase.
    sis_sqldatalimite = models.CharField(db_column='SIS_SQLDATALIMITE', max_length=2000, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    sis_sqldadosentidade = models.CharField(db_column='SIS_SQLDADOSENTIDADE', max_length=2000, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    sis_sqlinformacoes = models.CharField(db_column='SIS_SQLINFORMACOES', max_length=2000, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    sis_check = models.CharField(db_column='SIS_CHECK', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    sis_acessoexterno = models.BooleanField(db_column='SIS_ACESSOEXTERNO', blank=True, null=True)  # Field name made lowercase.
    sis_grupoexterno = models.IntegerField(db_column='SIS_GRUPOEXTERNO', blank=True, null=True)  # Field name made lowercase.
    sis_informacao = models.CharField(db_column='SIS_INFORMACAO', max_length=2000, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    sis_resumo = models.CharField(db_column='SIS_RESUMO', max_length=1000, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FR_SISTEMA'


class FrSistemaCategoria(models.Model):
    sis_codigo = models.CharField(db_column='SIS_CODIGO', primary_key=True, max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase. The composite primary key (SIS_CODIGO, CAT_CODIGO) found, that is not supported. The first column is selected.
    cat_codigo = models.ForeignKey(FrCategoria, models.DO_NOTHING, db_column='CAT_CODIGO')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FR_SISTEMA_CATEGORIA'
        unique_together = (('sis_codigo', 'cat_codigo'),)


class FrTabela(models.Model):
    tab_nome = models.CharField(db_column='TAB_NOME', primary_key=True, max_length=96, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    tab_descricao = models.CharField(db_column='TAB_DESCRICAO', max_length=96, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FR_TABELA'


class FrTarefa(models.Model):
    trf_codigo = models.IntegerField(db_column='TRF_CODIGO', primary_key=True)  # Field name made lowercase.
    trf_descricao = models.CharField(db_column='TRF_DESCRICAO', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    sis_codigo = models.ForeignKey(FrSistema, models.DO_NOTHING, db_column='SIS_CODIGO')  # Field name made lowercase.
    reg_codigo = models.ForeignKey(FrRegras, models.DO_NOTHING, db_column='REG_CODIGO')  # Field name made lowercase.
    trf_data_inicial = models.DateTimeField(db_column='TRF_DATA_INICIAL', blank=True, null=True)  # Field name made lowercase.
    trf_data_final = models.DateTimeField(db_column='TRF_DATA_FINAL', blank=True, null=True)  # Field name made lowercase.
    trf_ativa = models.CharField(db_column='TRF_ATIVA', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    trf_regra_parametros = models.TextField(db_column='TRF_REGRA_PARAMETROS', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    trf_tipo_agendamento = models.CharField(db_column='TRF_TIPO_AGENDAMENTO', max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FR_TAREFA'


class FrTarefaTempo(models.Model):
    trt_codigo = models.IntegerField(db_column='TRT_CODIGO', primary_key=True)  # Field name made lowercase.
    trf_codigo = models.ForeignKey(FrTarefa, models.DO_NOTHING, db_column='TRF_CODIGO')  # Field name made lowercase.
    trt_tipo = models.CharField(db_column='TRT_TIPO', max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    trt_valor = models.IntegerField(db_column='TRT_VALOR')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FR_TAREFA_TEMPO'


class FrTipodado(models.Model):
    tpd_codigo = models.IntegerField(db_column='TPD_CODIGO', primary_key=True)  # Field name made lowercase.
    tpd_descricao = models.CharField(db_column='TPD_DESCRICAO', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    tpd_mascaraformatacao = models.CharField(db_column='TPD_MASCARAFORMATACAO', max_length=254, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    tpd_mascaraedicao = models.CharField(db_column='TPD_MASCARAEDICAO', max_length=254, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FR_TIPODADO'


class FrTipoEvent(models.Model):
    fte_cod = models.AutoField(db_column='FTE_COD', primary_key=True)  # Field name made lowercase.
    fte_descricao = models.CharField(db_column='FTE_DESCRICAO', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    fte_sigla = models.CharField(db_column='FTE_SIGLA', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FR_TIPO_EVENT'


class FrTraducao(models.Model):
    tra_codigo = models.IntegerField(db_column='TRA_CODIGO', primary_key=True)  # Field name made lowercase.
    tra_item = models.CharField(db_column='TRA_ITEM', max_length=300, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    tra_texto = models.CharField(db_column='TRA_TEXTO', max_length=2000, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    tra_tipo = models.CharField(db_column='TRA_TIPO', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FR_TRADUCAO'


class FrTraducaoIdioma(models.Model):
    tra_codigo = models.OneToOneField(FrTraducao, models.DO_NOTHING, db_column='TRA_CODIGO', primary_key=True)  # Field name made lowercase. The composite primary key (TRA_CODIGO, IDI_CODIGO) found, that is not supported. The first column is selected.
    idi_codigo = models.ForeignKey(FrIdioma, models.DO_NOTHING, db_column='IDI_CODIGO')  # Field name made lowercase.
    tri_texto = models.CharField(db_column='TRI_TEXTO', max_length=2000, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    tri_situacao = models.CharField(db_column='TRI_SITUACAO', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    tri_hash = models.CharField(db_column='TRI_HASH', max_length=40, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FR_TRADUCAO_IDIOMA'
        unique_together = (('tra_codigo', 'idi_codigo'),)


class FrUsuario(models.Model):
    usr_codigo = models.IntegerField(db_column='USR_CODIGO', primary_key=True)  # Field name made lowercase.
    usr_login = models.CharField(db_column='USR_LOGIN', unique=True, max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    usr_senha = models.CharField(db_column='USR_SENHA', max_length=64, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    usr_administrador = models.CharField(db_column='USR_ADMINISTRADOR', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    usr_tipo_expiracao = models.CharField(db_column='USR_TIPO_EXPIRACAO', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    usr_dias_expiracao = models.IntegerField(db_column='USR_DIAS_EXPIRACAO', blank=True, null=True)  # Field name made lowercase.
    usr_imagem_digital = models.BinaryField(db_column='USR_IMAGEM_DIGITAL', blank=True, null=True)  # Field name made lowercase.
    usr_foto = models.BinaryField(db_column='USR_FOTO', blank=True, null=True)  # Field name made lowercase.
    usr_nome = models.CharField(db_column='USR_NOME', max_length=60, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    usr_email = models.CharField(db_column='USR_EMAIL', max_length=120, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    usr_digital = models.BigIntegerField(db_column='USR_DIGITAL', blank=True, null=True)  # Field name made lowercase.
    usr_inicio_expiracao = models.DateTimeField(db_column='USR_INICIO_EXPIRACAO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FR_USUARIO'


class FrUsuarioGrupo(models.Model):
    grp_codigo = models.OneToOneField(FrGrupo, models.DO_NOTHING, db_column='GRP_CODIGO', primary_key=True)  # Field name made lowercase. The composite primary key (GRP_CODIGO, SIS_CODIGO, USR_CODIGO) found, that is not supported. The first column is selected.
    sis_codigo = models.ForeignKey(FrGrupo, models.DO_NOTHING, db_column='SIS_CODIGO', to_field='SIS_CODIGO', related_name='frusuariogrupo_sis_codigo_set')  # Field name made lowercase.
    usr_codigo = models.ForeignKey(FrUsuario, models.DO_NOTHING, db_column='USR_CODIGO')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FR_USUARIO_GRUPO'
        unique_together = (('grp_codigo', 'sis_codigo', 'usr_codigo'),)


class FrUsuarioSistema(models.Model):
    usr_codigo = models.OneToOneField(FrUsuario, models.DO_NOTHING, db_column='USR_CODIGO', primary_key=True)  # Field name made lowercase. The composite primary key (USR_CODIGO, SIS_CODIGO) found, that is not supported. The first column is selected.
    sis_codigo = models.CharField(db_column='SIS_CODIGO', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    uss_acesso_externo = models.CharField(db_column='USS_ACESSO_EXTERNO', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    uss_administrador = models.CharField(db_column='USS_ADMINISTRADOR', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    uss_acesso_maker = models.CharField(db_column='USS_ACESSO_MAKER', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    uss_criar_formulario = models.CharField(db_column='USS_CRIAR_FORMULARIO', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    uss_criar_relatorio = models.CharField(db_column='USS_CRIAR_RELATORIO', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    uss_acessar = models.CharField(db_column='USS_ACESSAR', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    uss_criar_regra = models.CharField(db_column='USS_CRIAR_REGRA', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FR_USUARIO_SISTEMA'
        unique_together = (('usr_codigo', 'sis_codigo'),)


class FrVersao(models.Model):
    ver_codigo = models.AutoField(db_column='VER_CODIGO', primary_key=True)  # Field name made lowercase.
    ver_tipo = models.CharField(db_column='VER_TIPO', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    sis_codigo = models.CharField(db_column='SIS_CODIGO', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    obj_codigo = models.IntegerField(db_column='OBJ_CODIGO', blank=True, null=True)  # Field name made lowercase.
    ver_descricao = models.CharField(db_column='VER_DESCRICAO', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    ver_conteudo = models.BinaryField(db_column='VER_CONTEUDO')  # Field name made lowercase.
    ver_data_hora = models.DateTimeField(db_column='VER_DATA_HORA')  # Field name made lowercase.
    ver_versao = models.CharField(db_column='VER_VERSAO', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    usr_codigo = models.IntegerField(db_column='USR_CODIGO')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FR_VERSAO'





class Financeiro(models.Model):
    idcliente = models.OneToOneField(Cliente, models.DO_NOTHING, db_column='IDCliente', primary_key=True)  # Field name made lowercase. The composite primary key (IDCliente, TituloERP) found, that is not supported. The first column is selected.
    tituloerp = models.BigIntegerField(db_column='TituloERP')  # Field name made lowercase.
    idlocal = models.ForeignKey('LocalVenda', models.DO_NOTHING, db_column='IDLocal')  # Field name made lowercase.
    serie = models.CharField(db_column='Serie', max_length=6, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    nrtitulo = models.IntegerField(db_column='NrTitulo')  # Field name made lowercase.
    parcela = models.IntegerField(db_column='Parcela')  # Field name made lowercase.
    valor = models.DecimalField(db_column='Valor', max_digits=19, decimal_places=4)  # Field name made lowercase.
    saldo = models.DecimalField(db_column='Saldo', max_digits=19, decimal_places=4)  # Field name made lowercase.
    dtvencimento = models.DateField(db_column='DtVencimento')  # Field name made lowercase.
    dtliquidacao = models.DateField(db_column='DtLiquidacao', blank=True, null=True)  # Field name made lowercase.
    idboleto = models.CharField(db_column='IDBoleto', max_length=40, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Financeiro'
        unique_together = (('idcliente', 'tituloerp'),)


class Grupoeconomico(models.Model):
    idgrupoeconomico = models.AutoField(db_column='IDGrupoEconomico', primary_key=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    grupoeconomicoerp = models.IntegerField(db_column='GrupoEconomicoERP', blank=True, null=True)  # Field name made lowercase.
    situacao = models.CharField(db_column='Situacao', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GrupoEconomico'


class Jsonproc(models.Model):
    idjson = models.AutoField(db_column='IDJson', primary_key=True)  # Field name made lowercase.
    spid = models.IntegerField()
    origem = models.CharField(db_column='Origem', max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    dhevento = models.DateTimeField(db_column='DHEvento')  # Field name made lowercase.
    texto = models.TextField(db_column='Texto', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    evento_saida = models.CharField(db_column='Evento_saida', max_length=6, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    mensagem_saida = models.CharField(db_column='Mensagem_saida', max_length=5000, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'JSONProc'


class Limitecredito(models.Model):
    idlimitecredito = models.AutoField(db_column='IDLimiteCredito', primary_key=True)  # Field name made lowercase.
    idcliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='IDCliente')  # Field name made lowercase.
    idlocal = models.ForeignKey('LocalVenda', models.DO_NOTHING, db_column='IDLocal')  # Field name made lowercase.
    vllimitelocal = models.DecimalField(db_column='VlLimiteLocal', max_digits=19, decimal_places=4)  # Field name made lowercase.
    vllimitetotal = models.DecimalField(db_column='VlLimiteTotal', max_digits=19, decimal_places=4)  # Field name made lowercase.
    observacao = models.CharField(db_column='Observacao', max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LimiteCredito'


class Logatualizacao(models.Model):
    idlogatualizacao = models.AutoField(db_column='IDLogAtualizacao', primary_key=True)  # Field name made lowercase.
    tabela = models.CharField(db_column='Tabela', max_length=40, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    idregistro1 = models.IntegerField(db_column='IDRegistro1')  # Field name made lowercase.
    idregistro2 = models.IntegerField(db_column='IDRegistro2', blank=True, null=True)  # Field name made lowercase.
    idregistro3 = models.IntegerField(db_column='IDRegistro3', blank=True, null=True)  # Field name made lowercase.
    dataatualizacao = models.DateTimeField(db_column='DataAtualizacao')  # Field name made lowercase.
    idusuario = models.IntegerField(db_column='IDUsuario')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LogAtualizacao'


class Menu(models.Model):
    idmenu = models.AutoField(db_column='IDMenu', primary_key=True)  # Field name made lowercase.
    descmenu = models.CharField(db_column='DescMenu', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    idmenupai = models.ForeignKey('self', models.DO_NOTHING, db_column='IDMenuPai', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Menu'


class Ncmconfiguracaofiscal(models.Model):
    codigoncm = models.CharField(db_column='CodigoNCM', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    idlocal = models.IntegerField(db_column='IDLocal')  # Field name made lowercase.
    idconfiguracaofiscaltabela = models.IntegerField(db_column='IDConfiguracaoFiscalTabela')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NCMConfiguracaoFiscal'


class Organograma(models.Model):
    idorganograma = models.AutoField(db_column='IDOrganograma', primary_key=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    nivel = models.IntegerField(db_column='Nivel')  # Field name made lowercase.
    idpai = models.ForeignKey('self', models.DO_NOTHING, db_column='IDPai', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Organograma'








class Pedidocapa(models.Model):
    idpedido = models.OneToOneField(Pedido, models.DO_NOTHING, db_column='IDPedido', primary_key=True)  # Field name made lowercase.
    idtipopedido = models.ForeignKey('Tipopedido', models.DO_NOTHING, db_column='IDTipoPedido')  # Field name made lowercase.
    idpreco = models.ForeignKey('Preco', models.DO_NOTHING, db_column='IDPreco')  # Field name made lowercase.
    prazomedio = models.IntegerField(db_column='PrazoMedio')  # Field name made lowercase.
    idpagamento = models.ForeignKey(Pagamento, models.DO_NOTHING, db_column='IDPagamento')  # Field name made lowercase.
    idvolume = models.ForeignKey('Volume', models.DO_NOTHING, db_column='IDVolume', blank=True, null=True)  # Field name made lowercase.
    idvolumefaixa = models.ForeignKey('Volumefaixa', models.DO_NOTHING, db_column='IDVolumeFaixa', blank=True, null=True)  # Field name made lowercase.
    pervolume = models.DecimalField(db_column='PerVolume', max_digits=6, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    perclientetabela = models.DecimalField(db_column='PerClienteTabela', max_digits=6, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    idcascata = models.ForeignKey(Cascata, models.DO_NOTHING, db_column='IDCascata', blank=True, null=True)  # Field name made lowercase.
    percascata1 = models.DecimalField(db_column='PerCascata1', max_digits=6, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    percascata2 = models.DecimalField(db_column='PerCascata2', max_digits=6, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    percascata3 = models.DecimalField(db_column='PerCascata3', max_digits=6, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    percascata4 = models.DecimalField(db_column='PerCascata4', max_digits=6, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    perdescfinal = models.DecimalField(db_column='PerDescFinal', max_digits=6, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tipofrete = models.ForeignKey('Tipofrete', models.DO_NOTHING, db_column='TipoFrete')  # Field name made lowercase.
    idendereco = models.IntegerField(db_column='IDEndereco', blank=True, null=True)  # Field name made lowercase.
    idtransportador = models.IntegerField(db_column='IDTransportador', blank=True, null=True)  # Field name made lowercase.
    idtipotransporte = models.ForeignKey('Tipotransporte', models.DO_NOTHING, db_column='IDTipoTransporte', blank=True, null=True)  # Field name made lowercase.
    pedidoconcluido = models.CharField(db_column='PedidoConcluido', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    idredespacho = models.ForeignKey('Transportador', models.DO_NOTHING, db_column='IDRedespacho', blank=True, null=True)  # Field name made lowercase.
    dtprogramacao = models.DateField(db_column='DtProgramacao', blank=True, null=True)  # Field name made lowercase.
    idcarimbo = models.ForeignKey(Carimbo, models.DO_NOTHING, db_column='IDCarimbo', blank=True, null=True)  # Field name made lowercase.
    idcodigovenda = models.ForeignKey(Codigovenda, models.DO_NOTHING, db_column='IDCodigoVenda', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PedidoCapa'


class Pedidocomissao(models.Model):
    idpedido = models.OneToOneField(Pedido, models.DO_NOTHING, db_column='IDPedido', primary_key=True)  # Field name made lowercase.
    codvendedor = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='CodVendedor')  # Field name made lowercase.
    vlbase = models.DecimalField(db_column='VlBase', max_digits=19, decimal_places=4)  # Field name made lowercase.
    prcomissao = models.DecimalField(db_column='PrComissao', max_digits=7, decimal_places=3)  # Field name made lowercase.
    vlcomissao = models.DecimalField(db_column='VlComissao', max_digits=19, decimal_places=4)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PedidoComissao'


class Pedidoerp(models.Model):
    idpedido = models.IntegerField(db_column='IDPedido')  # Field name made lowercase.
    nritem = models.SmallIntegerField(db_column='NrItem')  # Field name made lowercase.
    idproduto = models.IntegerField(db_column='IDProduto')  # Field name made lowercase.
    dtpedidoerp = models.DateTimeField(db_column='DtPedidoERP')  # Field name made lowercase.
    qtcortada = models.DecimalField(db_column='QtCortada', max_digits=6, decimal_places=4)  # Field name made lowercase.
    qtatendida = models.DecimalField(db_column='QtAtendida', max_digits=6, decimal_places=4)  # Field name made lowercase.
    vlunitario = models.DecimalField(db_column='VlUnitario', max_digits=19, decimal_places=4)  # Field name made lowercase.
    vlproduto = models.DecimalField(db_column='VlProduto', max_digits=19, decimal_places=4)  # Field name made lowercase.
    vlpedido = models.DecimalField(db_column='VlPedido', max_digits=19, decimal_places=4)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PedidoERP'


class Pedidoestagio(models.Model):
    idpedidoestagio = models.AutoField(db_column='IDPedidoEstagio', primary_key=True)  # Field name made lowercase.
    idpedido = models.ForeignKey(Pedido, models.DO_NOTHING, db_column='IDPedido')  # Field name made lowercase.
    dtestagio = models.DateTimeField(db_column='DtEstagio')  # Field name made lowercase.
    idusuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='IDUsuario')  # Field name made lowercase.
    codmensagem = models.CharField(db_column='CodMensagem', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    mensagem = models.CharField(db_column='Mensagem', max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PedidoEstagio'


class Pedidoimposto(models.Model):
    idpedido = models.OneToOneField('Pedidoproduto', models.DO_NOTHING, db_column='IDPedido', primary_key=True)  # Field name made lowercase. The composite primary key (IDPedido, NrItem) found, that is not supported. The first column is selected.
    nritem = models.ForeignKey('Pedidoproduto', models.DO_NOTHING, db_column='NrItem', to_field='NrItem', related_name='pedidoimposto_nritem_set')  # Field name made lowercase.
    vlmargem = models.DecimalField(db_column='VLMargem', max_digits=19, decimal_places=4)  # Field name made lowercase.
    prmargem = models.DecimalField(db_column='PRMargem', max_digits=6, decimal_places=3)  # Field name made lowercase.
    vlfrete = models.DecimalField(db_column='VLFrete', max_digits=19, decimal_places=4)  # Field name made lowercase.
    vlseguro = models.DecimalField(db_column='VLSeguro', max_digits=19, decimal_places=4)  # Field name made lowercase.
    vldespesas = models.DecimalField(db_column='VLDespesas', max_digits=19, decimal_places=4)  # Field name made lowercase.
    vloutras = models.DecimalField(db_column='VLOutras', max_digits=19, decimal_places=4)  # Field name made lowercase.
    ccfop = models.SmallIntegerField(db_column='cCFOP', blank=True, null=True)  # Field name made lowercase.
    idicmscst = models.CharField(db_column='IDICMSCST', max_length=4, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    idicmstipobase = models.CharField(db_column='IDICMSTipoBase', max_length=4, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    pricmsreducaobase = models.DecimalField(db_column='PRICMSReducaoBase', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    icmssomaipi = models.CharField(db_column='ICMSSomaIPI', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    vlicmsbase = models.DecimalField(db_column='VLICMSBase', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pricms = models.DecimalField(db_column='PRICMS', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    vlicms = models.DecimalField(db_column='VLICMS', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vlicmsbasefcp = models.DecimalField(db_column='VLICMSBaseFCP', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pricmsfcp = models.DecimalField(db_column='PRICMSFCP', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    vlicmsfcp = models.DecimalField(db_column='VLICMSFCP', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vlicmsbasefcpufdestino = models.DecimalField(db_column='VLICMSBaseFCPUFDestino', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pricmsfcpufdestino = models.DecimalField(db_column='PRICMSFCPUFDestino', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    vlicmsfcpufdestino = models.DecimalField(db_column='VLICMSFCPUFDestino', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vlicmsbasefcpst = models.DecimalField(db_column='VLICMSBaseFCPST', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pricmsfcpst = models.DecimalField(db_column='PRICMSFCPST', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    vlicmsfcpst = models.DecimalField(db_column='VLICMSFCPST', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vlicmsbasefcpretido = models.DecimalField(db_column='VLICMSBaseFCPRetido', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pricmsfcpretido = models.DecimalField(db_column='PRICMSFCPRetido', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    vlicmsfcpretido = models.DecimalField(db_column='VLICMSFCPRetido', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pricmsfcpdiferimento = models.DecimalField(db_column='PRICMSFCPDiferimento', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    vlicmsfcpdiferimento = models.DecimalField(db_column='VLICMSFCPDiferimento', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vlicmsfcpefetivo = models.DecimalField(db_column='VLICMSFCPEfetivo', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pricmsnaocomputado = models.DecimalField(db_column='PRICMSNaoComputado', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    pricmsdiferimento = models.DecimalField(db_column='PRICMSDiferimento', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    vlicmsdiferimentooperacao = models.DecimalField(db_column='VLICMSDiferimentoOperacao', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vlicmsdiferimento = models.DecimalField(db_column='VLICMSDiferimento', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vlicmsdiferido = models.DecimalField(db_column='VLICMSDiferido', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pricmsdesoneracao = models.DecimalField(db_column='PRICMSDesoneracao', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    vlicmsdesoneracao = models.DecimalField(db_column='VLICMSDesoneracao', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    idicmsmotivodesoneracao = models.IntegerField(db_column='IDICMSMotivoDesoneracao', blank=True, null=True)  # Field name made lowercase.
    idicmssttipobase = models.CharField(db_column='IDICMSSTTipoBase', max_length=4, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    vlicmsstbase = models.DecimalField(db_column='VLICMSSTBase', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pricmsstmva = models.DecimalField(db_column='PRICMSSTMVA', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    pricmsstreducao = models.DecimalField(db_column='PRICMSSTReducao', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    vlicmsstpauta = models.DecimalField(db_column='VLICMSSTPauta', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pricmsst = models.DecimalField(db_column='PRICMSST', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    vlicmsst = models.DecimalField(db_column='VLICMSST', max_digits=19, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    vlicmsstnaocomputado = models.DecimalField(db_column='VLICMSSTNaoComputado', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vlicmsstbasenaocomputado = models.DecimalField(db_column='VLICMSSTBaseNaoComputado', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    usaicmsstvalorreferencia = models.CharField(db_column='UsaICMSSTValorReferencia', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    vlicmsstreferencia = models.DecimalField(db_column='VLICMSSTReferencia', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pricmsstpauta = models.DecimalField(db_column='PRICMSSTPauta', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    idicmsstmotivodesoneracao = models.IntegerField(db_column='IDICMSSTMotivoDesoneracao', blank=True, null=True)  # Field name made lowercase.
    vlicmsstdesoneracao = models.DecimalField(db_column='VLICMSSTDesoneracao', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pricmsdifalpartilha = models.DecimalField(db_column='PRICMSDifalPartilha', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    pricmssimplescredito = models.DecimalField(db_column='PRICMSSimplesCredito', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    vlicmssimplescredito = models.DecimalField(db_column='VLICMSSimplesCredito', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vlicmsdifalbase = models.DecimalField(db_column='VLICMSDifalBase', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vlicmsdifalpartilhaorigem = models.DecimalField(db_column='VLICMSDifalPartilhaOrigem', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vlicmsdifalpartilhadestino = models.DecimalField(db_column='VLICMSDifalPartilhaDestino', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pricmsdifal = models.DecimalField(db_column='PRICMSDifal', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    vlicmsdifal = models.DecimalField(db_column='VLICMSDifal', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pricmsdifalinterno = models.DecimalField(db_column='PRICMSDifalInterno', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    pricmsdifalinterestadual = models.DecimalField(db_column='PRICMSDifalInterestadual', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    vlicmsisentas = models.DecimalField(db_column='VLICMSIsentas', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vlicmsoutras = models.DecimalField(db_column='VLICMSOutras', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vlicmsefetivobase = models.DecimalField(db_column='VLICMSEfetivoBase', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vlicmsefetivo = models.DecimalField(db_column='VLICMSEfetivo', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pricmsefetivo = models.DecimalField(db_column='PRICMSEfetivo', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    usaicmsefetivo = models.CharField(db_column='UsaICMSEfetivo', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    pricmsreducaobaseefetivo = models.DecimalField(db_column='PRICMSReducaoBaseEfetivo', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    pricmspautamaximo = models.DecimalField(db_column='PRICMSPautaMaximo', max_digits=20, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    vlicmssubstitutoretido = models.DecimalField(db_column='VLICMSSubstitutoRetido', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pricmsantecipacao = models.DecimalField(db_column='PRICMSAntecipacao', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    pricmsmvaantecipacao = models.DecimalField(db_column='PRICMSMVAAntecipacao', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    pricmsreducaoantecipacao = models.DecimalField(db_column='PRICMSReducaoAntecipacao', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    vlicmspautaantecipacao = models.DecimalField(db_column='VLICMSPautaAntecipacao', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    dtvencpautaantecipacao = models.DateField(db_column='DTVencPautaAntecipacao', blank=True, null=True)  # Field name made lowercase.
    idipicst = models.CharField(db_column='IDIPICST', max_length=4, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    idipicenq = models.CharField(db_column='IDIPICenq', max_length=4, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    vlipibase = models.DecimalField(db_column='VLIPIBase', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pripi = models.DecimalField(db_column='PRIPI', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    qtipiunidade = models.BigIntegerField(db_column='QTIPIUnidade', blank=True, null=True)  # Field name made lowercase.
    vlipiunidade = models.DecimalField(db_column='VLIPIUnidade', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vlipi = models.DecimalField(db_column='VLIPI', max_digits=19, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    vlipiisentas = models.DecimalField(db_column='VLIPIIsentas', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vlipioutras = models.DecimalField(db_column='VLIPIOutras', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vlipidevolucao = models.DecimalField(db_column='VLIPIDevolucao', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    idpiscst = models.CharField(db_column='IDPISCST', max_length=4, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    pissomaicms = models.CharField(db_column='PISSomaICMS', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    vlpisbase = models.DecimalField(db_column='VLPISBase', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    prpis = models.DecimalField(db_column='PRPIS', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    qtpisunidade = models.BigIntegerField(db_column='QTPISUnidade', blank=True, null=True)  # Field name made lowercase.
    vlpisunidade = models.DecimalField(db_column='VLPISUnidade', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vlpis = models.DecimalField(db_column='VLPIS', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vlpisstbase = models.DecimalField(db_column='VLPISSTBase', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    prpisst = models.DecimalField(db_column='PRPISST', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    qtpisstunidade = models.BigIntegerField(db_column='QTPISSTUnidade', blank=True, null=True)  # Field name made lowercase.
    vlpisstunidade = models.DecimalField(db_column='VLPISSTUnidade', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vlpisst = models.DecimalField(db_column='VLPISST', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    idcofinscst = models.CharField(db_column='IDCOFINSCST', max_length=4, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cofinssomaicms = models.CharField(db_column='COFINSSomaICMS', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    vlcofinsbase = models.DecimalField(db_column='VLCOFINSBase', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    prcofins = models.DecimalField(db_column='PRCOFINS', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    qtcofinsunidade = models.BigIntegerField(db_column='QTCOFINSUnidade', blank=True, null=True)  # Field name made lowercase.
    vlcofinsunidade = models.DecimalField(db_column='VLCOFINSUnidade', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vlcofins = models.DecimalField(db_column='VLCOFINS', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vlcofinsstbase = models.DecimalField(db_column='VLCOFINSSTBase', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    prcofinsst = models.DecimalField(db_column='PRCOFINSST', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    qtcofinsstunidade = models.BigIntegerField(db_column='QTCOFINSSTUnidade', blank=True, null=True)  # Field name made lowercase.
    vlcofinsstunidade = models.DecimalField(db_column='VLCOFINSSTUnidade', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vlcofinsst = models.DecimalField(db_column='VLCOFINSST', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    idconfiguracaofiscal = models.BigIntegerField(db_column='IDConfiguracaoFiscal', blank=True, null=True)  # Field name made lowercase.
    usachavenatural = models.CharField(db_column='UsaChaveNatural', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    vldescontodesoneracao = models.DecimalField(db_column='VLDescontoDesoneracao', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    descontardesoneracao = models.CharField(db_column='DescontarDesoneracao', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    idcbenef = models.BigIntegerField(db_column='IDcbenef', blank=True, null=True)  # Field name made lowercase.
    idchavenatural = models.CharField(db_column='IDChaveNatural', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    piscofinssomanota = models.CharField(db_column='PISCOFINSSomaNota', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    somaracrescimobase = models.CharField(db_column='SomarAcrescimoBase', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    cormargem = models.CharField(db_column='CorMargem', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PedidoImposto'
        unique_together = (('idpedido', 'nritem'),)


class Pedidomotivo(models.Model):
    idpedido = models.OneToOneField(Pedido, models.DO_NOTHING, db_column='IDPedido', primary_key=True)  # Field name made lowercase.
    dtcancelado = models.DateTimeField(db_column='DtCancelado')  # Field name made lowercase.
    idusuario = models.IntegerField(db_column='IDUsuario')  # Field name made lowercase.
    idmotivo = models.ForeignKey('Tabgeral', models.DO_NOTHING, db_column='IDMotivo')  # Field name made lowercase.
    motivo = models.CharField(db_column='Motivo', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PedidoMotivo'


class Pedidonota(models.Model):
    idlocal = models.OneToOneField('LocalVenda', models.DO_NOTHING, db_column='IDLocal', primary_key=True)  # Field name made lowercase. The composite primary key (IDLocal, IDPedidoERP, IDCliente) found, that is not supported. The first column is selected.
    idpedidoerp = models.BigIntegerField(db_column='IDPedidoERP')  # Field name made lowercase.
    idcliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='IDCliente')  # Field name made lowercase.
    seriepedido = models.CharField(db_column='SeriePedido', max_length=6, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    nrpedido = models.IntegerField(db_column='NrPedido')  # Field name made lowercase.
    dtpedido = models.DateTimeField(db_column='DtPedido')  # Field name made lowercase.
    situacaopedido = models.CharField(db_column='SituacaoPedido', max_length=4, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    nrdanfe = models.IntegerField(db_column='NrDANFE', blank=True, null=True)  # Field name made lowercase.
    nrseriedanfe = models.CharField(db_column='NrSerieDANFE', max_length=6, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    dtemissao = models.DateTimeField(db_column='DtEmissao', blank=True, null=True)  # Field name made lowercase.
    vldanfe = models.DecimalField(db_column='VlDANFE', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    situacaodanfe = models.CharField(db_column='SituacaoDANFE', max_length=4, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    nrtitulo = models.IntegerField(db_column='NrTitulo', blank=True, null=True)  # Field name made lowercase.
    nrserietitulo = models.CharField(db_column='NrSerieTitulo', max_length=6, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    qtparcela = models.SmallIntegerField(db_column='QtParcela', blank=True, null=True)  # Field name made lowercase.
    idpedido = models.ForeignKey(Pedido, models.DO_NOTHING, db_column='IDPedido', blank=True, null=True)  # Field name made lowercase.
    vendedorerp = models.IntegerField(db_column='VendedorERP', blank=True, null=True)  # Field name made lowercase.
    responsavelerp = models.IntegerField(db_column='ResponsavelERP', blank=True, null=True)  # Field name made lowercase.
    representadaerp = models.IntegerField(db_column='RepresentadaERP', blank=True, null=True)  # Field name made lowercase.
    idvendedor = models.IntegerField(db_column='IDVendedor', blank=True, null=True)  # Field name made lowercase.
    idresponsavel = models.IntegerField(db_column='IDResponsavel', blank=True, null=True)  # Field name made lowercase.
    idrepresentada = models.IntegerField(db_column='IDRepresentada', blank=True, null=True)  # Field name made lowercase.
    vlpedido = models.DecimalField(db_column='VlPedido', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tabpreco = models.CharField(db_column='TabPreco', max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    pagamento = models.CharField(db_column='Pagamento', max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    prazomedio = models.IntegerField(db_column='PrazoMedio', blank=True, null=True)  # Field name made lowercase.
    vlmercadoria = models.DecimalField(db_column='VlMercadoria', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vlimposto = models.DecimalField(db_column='VlImposto', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vlfrete = models.DecimalField(db_column='VlFrete', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vldespesas = models.DecimalField(db_column='VlDespesas', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    prdesconto = models.DecimalField(db_column='PrDesconto', max_digits=7, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    tipofrete = models.IntegerField(db_column='TipoFrete', blank=True, null=True)  # Field name made lowercase.
    vldesconto = models.DecimalField(db_column='VlDesconto', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PedidoNota'
        unique_together = (('idlocal', 'idpedidoerp', 'idcliente'),)


class Pedidonotaparcela(models.Model):
    idlocal = models.OneToOneField(Pedidonota, models.DO_NOTHING, db_column='IDLocal', primary_key=True)  # Field name made lowercase. The composite primary key (IDLocal, IDPedidoERP, IDCliente, NrParcela) found, that is not supported. The first column is selected.
    idpedidoerp = models.ForeignKey(Pedidonota, models.DO_NOTHING, db_column='IDPedidoERP', to_field='IDPedidoERP', related_name='pedidonotaparcela_idpedidoerp_set')  # Field name made lowercase.
    idcliente = models.ForeignKey(Pedidonota, models.DO_NOTHING, db_column='IDCliente', to_field='IDPedidoERP', related_name='pedidonotaparcela_idcliente_set')  # Field name made lowercase.
    nrparcela = models.IntegerField(db_column='NrParcela')  # Field name made lowercase.
    dtvencimento = models.DateField(db_column='DtVencimento', blank=True, null=True)  # Field name made lowercase.
    vlparcela = models.DecimalField(db_column='VlParcela', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vlsaldo = models.DecimalField(db_column='VlSaldo', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    dtliquidacao = models.DateField(db_column='DtLiquidacao', blank=True, null=True)  # Field name made lowercase.
    tituloerp = models.BigIntegerField(db_column='TituloERP', blank=True, null=True)  # Field name made lowercase.
    idboleto = models.CharField(db_column='IDBoleto', max_length=40, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PedidoNotaParcela'
        unique_together = (('idlocal', 'idpedidoerp', 'idcliente', 'nrparcela'),)


class Pedidonotaproduto(models.Model):
    idlocal = models.OneToOneField(Pedidonota, models.DO_NOTHING, db_column='IDLocal', primary_key=True)  # Field name made lowercase. The composite primary key (IDLocal, IDPedidoERP, IDCliente, NrOrdem) found, that is not supported. The first column is selected.
    idpedidoerp = models.ForeignKey(Pedidonota, models.DO_NOTHING, db_column='IDPedidoERP', to_field='IDPedidoERP', related_name='pedidonotaproduto_idpedidoerp_set')  # Field name made lowercase.
    idcliente = models.ForeignKey(Pedidonota, models.DO_NOTHING, db_column='IDCliente', to_field='IDPedidoERP', related_name='pedidonotaproduto_idcliente_set')  # Field name made lowercase.
    nrordem = models.IntegerField(db_column='NrOrdem')  # Field name made lowercase.
    idproduto = models.IntegerField(db_column='IDProduto', blank=True, null=True)  # Field name made lowercase.
    produtoerp = models.CharField(db_column='ProdutoERP', max_length=60, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    sku = models.CharField(db_column='SKU', max_length=60, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    desproduto = models.CharField(db_column='DesProduto', max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    unidade = models.CharField(db_column='Unidade', max_length=6, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    qtpedido = models.DecimalField(db_column='QtPedido', max_digits=19, decimal_places=6)  # Field name made lowercase.
    qtcortada = models.DecimalField(db_column='QtCortada', max_digits=19, decimal_places=6)  # Field name made lowercase.
    qtfaturada = models.DecimalField(db_column='QtFaturada', max_digits=19, decimal_places=6)  # Field name made lowercase.
    vlunitario = models.DecimalField(db_column='VlUnitario', max_digits=19, decimal_places=6)  # Field name made lowercase.
    prdesconto = models.DecimalField(db_column='PrDesconto', max_digits=6, decimal_places=3)  # Field name made lowercase.
    vldesconto = models.DecimalField(db_column='VlDesconto', max_digits=19, decimal_places=4)  # Field name made lowercase.
    vlliquido = models.DecimalField(db_column='VlLiquido', max_digits=19, decimal_places=4)  # Field name made lowercase.
    vlipi = models.DecimalField(db_column='VlIPI', max_digits=19, decimal_places=4)  # Field name made lowercase.
    vlicmsst = models.DecimalField(db_column='VlICMSST', max_digits=19, decimal_places=4)  # Field name made lowercase.
    vltotal = models.DecimalField(db_column='VlTotal', max_digits=19, decimal_places=4)  # Field name made lowercase.
    observacao = models.CharField(db_column='Observacao', max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PedidoNotaProduto'
        unique_together = (('idlocal', 'idpedidoerp', 'idcliente', 'nrordem'),)


class Pedidoparcela(models.Model):
    idpedido = models.OneToOneField(Pedido, models.DO_NOTHING, db_column='IDPedido', primary_key=True)  # Field name made lowercase. The composite primary key (IDPedido, NrParcela) found, that is not supported. The first column is selected.
    nrparcela = models.IntegerField(db_column='NrParcela')  # Field name made lowercase.
    dtvencimento = models.DateField(db_column='DtVencimento')  # Field name made lowercase.
    valor = models.DecimalField(db_column='Valor', max_digits=19, decimal_places=4)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PedidoParcela'
        unique_together = (('idpedido', 'nrparcela'),)


class Pedidopolitica(models.Model):
    idpedido = models.OneToOneField(Pedido, models.DO_NOTHING, db_column='IDPedido', primary_key=True)  # Field name made lowercase.
    usardescontovolume = models.CharField(db_column='UsarDescontoVolume', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    usardescontocascata = models.CharField(db_column='UsarDescontoCascata', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    habilitardescontovolume = models.CharField(db_column='HabilitarDescontoVolume', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    habilitardescontocliente = models.CharField(db_column='HabilitarDescontoCliente', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    habilitardescontocascata = models.CharField(db_column='HabilitarDescontoCascata', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    habilitardescontoadicional = models.CharField(db_column='HabilitarDescontoAdicional', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    visualizarsaldoestoque = models.CharField(db_column='VisualizarSaldoEstoque', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    usarpedidominimo = models.CharField(db_column='UsarPedidoMinimo', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    controlamargem = models.CharField(db_column='ControlaMargem', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    controlaestoque = models.CharField(db_column='ControlaEstoque', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    permaxvolume = models.DecimalField(db_column='PerMaxVolume', max_digits=6, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    permaxclientetabela = models.DecimalField(db_column='PerMaxClienteTabela', max_digits=6, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    sigla1 = models.CharField(db_column='Sigla1', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    permaxcascata1 = models.DecimalField(db_column='PerMaxCascata1', max_digits=6, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    sigla2 = models.CharField(db_column='Sigla2', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    permaxcascata2 = models.DecimalField(db_column='PerMaxCascata2', max_digits=6, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    sigla3 = models.CharField(db_column='Sigla3', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    permaxcascata3 = models.DecimalField(db_column='PerMaxCascata3', max_digits=6, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    sigla4 = models.CharField(db_column='Sigla4', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    permaxcascata4 = models.DecimalField(db_column='PerMaxCascata4', max_digits=6, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    idcascata = models.IntegerField(db_column='IDCascata', blank=True, null=True)  # Field name made lowercase.
    idvolume = models.IntegerField(db_column='IDVolume', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PedidoPolitica'


class Pedidoproduto(models.Model):
    idpedido = models.OneToOneField(Pedido, models.DO_NOTHING, db_column='IDPedido', primary_key=True)  # Field name made lowercase. The composite primary key (IDPedido, NrItem) found, that is not supported. The first column is selected.
    nritem = models.SmallIntegerField(db_column='NrItem')  # Field name made lowercase.
    idproduto = models.ForeignKey('Produto', models.DO_NOTHING, db_column='IDProduto')  # Field name made lowercase.
    codembalagem = models.IntegerField(db_column='CodEmbalagem')  # Field name made lowercase.
    precobase = models.DecimalField(db_column='PrecoBase', max_digits=19, decimal_places=6)  # Field name made lowercase.
    perdescpedido = models.DecimalField(db_column='PerDescPedido', max_digits=7, decimal_places=4)  # Field name made lowercase.
    perdescitem = models.DecimalField(db_column='PerDescItem', max_digits=7, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    vldesconto = models.DecimalField(db_column='VlDesconto', max_digits=19, decimal_places=6)  # Field name made lowercase.
    vlliquido = models.DecimalField(db_column='VlLiquido', max_digits=19, decimal_places=6)  # Field name made lowercase.
    qtitem = models.DecimalField(db_column='QTItem', max_digits=19, decimal_places=4)  # Field name made lowercase.
    qtcortada = models.DecimalField(db_column='QTCortada', max_digits=19, decimal_places=4)  # Field name made lowercase.
    vlmercadoria = models.DecimalField(db_column='VlMercadoria', max_digits=19, decimal_places=4)  # Field name made lowercase.
    observacao = models.CharField(db_column='Observacao', max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    alteroupreco = models.CharField(db_column='AlterouPreco', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    mensagem = models.CharField(max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    vlcusto = models.DecimalField(db_column='VLCusto', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    usaoferta = models.CharField(db_column='UsaOferta', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    idoferta = models.ForeignKey(Oferta, models.DO_NOTHING, db_column='IDOferta', blank=True, null=True)  # Field name made lowercase.
    alterardesconto = models.CharField(db_column='AlterarDesconto', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    precooriginal = models.DecimalField(db_column='PrecoOriginal', max_digits=19, decimal_places=6)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PedidoProduto'
        unique_together = (('idpedido', 'nritem'),)


class Pedidoprodutocomissao(models.Model):
    idpedido = models.OneToOneField(Pedidoproduto, models.DO_NOTHING, db_column='IDPedido', primary_key=True)  # Field name made lowercase. The composite primary key (IDPedido, NrItem) found, that is not supported. The first column is selected.
    nritem = models.ForeignKey(Pedidoproduto, models.DO_NOTHING, db_column='NrItem', to_field='NrItem', related_name='pedidoprodutocomissao_nritem_set')  # Field name made lowercase.
    codvendedor = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='CodVendedor')  # Field name made lowercase.
    vlbase = models.DecimalField(db_column='VlBase', max_digits=19, decimal_places=4)  # Field name made lowercase.
    prcomissao = models.DecimalField(db_column='PrComissao', max_digits=7, decimal_places=3)  # Field name made lowercase.
    vlcomissao = models.DecimalField(db_column='VlComissao', max_digits=19, decimal_places=4)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PedidoProdutoComissao'
        unique_together = (('idpedido', 'nritem'),)


class Pedidoprodutopreco(models.Model):
    idpedido = models.OneToOneField(Pedidoproduto, models.DO_NOTHING, db_column='IDPedido', primary_key=True)  # Field name made lowercase. The composite primary key (IDPedido, NrItem, NrOrdem) found, that is not supported. The first column is selected.
    nritem = models.ForeignKey(Pedidoproduto, models.DO_NOTHING, db_column='NrItem', to_field='NrItem', related_name='pedidoprodutopreco_nritem_set')  # Field name made lowercase.
    nrordem = models.IntegerField(db_column='NrOrdem')  # Field name made lowercase.
    dsvalor = models.CharField(db_column='DsValor', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    vlvalor = models.DecimalField(db_column='VlValor', max_digits=19, decimal_places=6)  # Field name made lowercase.
    prvalor = models.DecimalField(db_column='PrValor', max_digits=7, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    precobase = models.CharField(db_column='PrecoBase', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PedidoProdutoPreco'
        unique_together = (('idpedido', 'nritem', 'nrordem'),)








class Produtoabc(models.Model):
    idproduto = models.OneToOneField(Produto, models.DO_NOTHING, db_column='IDProduto', primary_key=True)  # Field name made lowercase. The composite primary key (IDProduto, IDLocal) found, that is not supported. The first column is selected.
    idlocal = models.ForeignKey('LocalVenda', models.DO_NOTHING, db_column='IDLocal')  # Field name made lowercase.
    conceito = models.CharField(db_column='Conceito', max_length=2, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ProdutoABC'
        unique_together = (('idproduto', 'idlocal'),)


class Produtodata(models.Model):
    idproduto = models.OneToOneField(Produto, models.DO_NOTHING, db_column='IDProduto', primary_key=True)  # Field name made lowercase.
    datacadastro = models.DateTimeField(db_column='DataCadastro', blank=True, null=True)  # Field name made lowercase.
    dataatualiza = models.DateTimeField(db_column='DataAtualiza', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ProdutoData'


class Produtokit(models.Model):
    idproduto = models.OneToOneField(Produto, models.DO_NOTHING, db_column='IDProduto', primary_key=True)  # Field name made lowercase. The composite primary key (IDProduto, IDComponente) found, that is not supported. The first column is selected.
    idcomponente = models.IntegerField(db_column='IDComponente')  # Field name made lowercase.
    qtdcomponente = models.DecimalField(db_column='QtdComponente', max_digits=10, decimal_places=4)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ProdutoKit'
        unique_together = (('idproduto', 'idcomponente'),)





class Produtosaldo(models.Model):
    idlocal = models.IntegerField(db_column='IDLocal', primary_key=True)  # Field name made lowercase. The composite primary key (IDLocal, IDProduto) found, that is not supported. The first column is selected.
    idproduto = models.ForeignKey(Produto, models.DO_NOTHING, db_column='IDProduto')  # Field name made lowercase.
    dhsaldo = models.DateTimeField(db_column='DhSaldo', blank=True, null=True)  # Field name made lowercase.
    qtdisponivel = models.DecimalField(db_column='QtDisponivel', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    qtreserva = models.DecimalField(db_column='QtReserva', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    qtvenda = models.DecimalField(db_column='QtVenda', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    qtcompra = models.DecimalField(db_column='QtCompra', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    qtsaldo = models.DecimalField(db_column='QtSaldo', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ProdutoSaldo'
        unique_together = (('idlocal', 'idproduto'),)


class Produtotabelafiscal(models.Model):
    idproduto = models.IntegerField(db_column='IDProduto')  # Field name made lowercase.
    idempresa = models.IntegerField(db_column='IDEmpresa')  # Field name made lowercase.
    idtabelafiscal = models.IntegerField(db_column='IDTabelaFiscal')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ProdutoTabelaFiscal'


class Produtourl(models.Model):
    idproduto = models.OneToOneField(Produto, models.DO_NOTHING, db_column='IDProduto', primary_key=True)  # Field name made lowercase. The composite primary key (IDProduto, Url) found, that is not supported. The first column is selected.
    url = models.CharField(db_column='Url', max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ProdutoUrl'
        unique_together = (('idproduto', 'url'),)


class Rede(models.Model):
    idrede = models.AutoField(db_column='IDRede', primary_key=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    redeerp = models.IntegerField(db_column='RedeERP', blank=True, null=True)  # Field name made lowercase.
    situacao = models.CharField(db_column='Situacao', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Rede'


class Stag(models.Model):
    idstag = models.AutoField(db_column='IDSTAG', primary_key=True)  # Field name made lowercase.
    desstag = models.CharField(db_column='DesSTAG', max_length=60, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    situacao = models.CharField(db_column='Situacao', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'STAG'


class Substituto(models.Model):
    idproduto = models.IntegerField(db_column='IDProduto', primary_key=True)  # Field name made lowercase. The composite primary key (IDProduto, IDSubstituto) found, that is not supported. The first column is selected.
    idsubstituto = models.ForeignKey(Produto, models.DO_NOTHING, db_column='IDSubstituto')  # Field name made lowercase.
    prioridade = models.IntegerField(db_column='Prioridade')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Substituto'
        unique_together = (('idproduto', 'idsubstituto'),)


class Tag(models.Model):
    idtag = models.AutoField(db_column='IDTAG', primary_key=True)  # Field name made lowercase.
    destag = models.CharField(db_column='DesTAG', max_length=60, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    situacao = models.CharField(db_column='Situacao', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TAG'


class Tagstag(models.Model):
    idtag = models.OneToOneField(Tag, models.DO_NOTHING, db_column='IDTAG', primary_key=True)  # Field name made lowercase. The composite primary key (IDTAG, IDSTAG) found, that is not supported. The first column is selected.
    idstag = models.ForeignKey(Stag, models.DO_NOTHING, db_column='IDSTAG')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TAGSTAG'
        unique_together = (('idtag', 'idstag'),)


class Tempjson(models.Model):
    spid = models.IntegerField(db_column='SPID', blank=True, null=True)  # Field name made lowercase.
    texto = models.TextField(db_column='Texto', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TEMPJSON'


class Templistacliente(models.Model):
    spid = models.IntegerField(db_column='SPID', primary_key=True)  # Field name made lowercase. The composite primary key (SPID, IDCliente) found, that is not supported. The first column is selected.
    idcliente = models.IntegerField(db_column='IDCliente')  # Field name made lowercase.
    coderp = models.IntegerField(db_column='CodERP', blank=True, null=True)  # Field name made lowercase.
    cnpjcpf = models.CharField(db_column='CNPJCPF', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    razao = models.CharField(db_column='Razao', max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    fantasia = models.CharField(db_column='Fantasia', max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    situacao = models.CharField(db_column='Situacao', max_length=5, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TEMPListaCliente'
        unique_together = (('spid', 'idcliente'),)


class Temppedido(models.Model):
    spid = models.IntegerField()
    idpedido = models.IntegerField(db_column='IDPedido', blank=True, null=True)  # Field name made lowercase.
    idusuario = models.IntegerField(db_column='IDUsuario', blank=True, null=True)  # Field name made lowercase.
    idlocal = models.IntegerField(db_column='IDLocal', blank=True, null=True)  # Field name made lowercase.
    nrpedido = models.IntegerField(db_column='NrPedido', blank=True, null=True)  # Field name made lowercase.
    origemvenda = models.SmallIntegerField(db_column='OrigemVenda', blank=True, null=True)  # Field name made lowercase.
    dtpedido = models.DateTimeField(db_column='DtPedido', blank=True, null=True)  # Field name made lowercase.
    codvendedor = models.IntegerField(db_column='CodVendedor', blank=True, null=True)  # Field name made lowercase.
    codrepresentada = models.IntegerField(db_column='CodRepresentada', blank=True, null=True)  # Field name made lowercase.
    situacao = models.CharField(db_column='Situacao', max_length=2, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    dtorcamento = models.DateTimeField(db_column='DTOrcamento', blank=True, null=True)  # Field name made lowercase.
    dtvalidade = models.DateField(db_column='DtValidade', blank=True, null=True)  # Field name made lowercase.
    idpedidoerp = models.BigIntegerField(db_column='IDPedidoERP', blank=True, null=True)  # Field name made lowercase.
    idresponsavel = models.IntegerField(db_column='IDResponsavel', blank=True, null=True)  # Field name made lowercase.
    nroriginal = models.CharField(db_column='NrOriginal', max_length=60, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    idcliente = models.IntegerField(db_column='IDCliente', blank=True, null=True)  # Field name made lowercase.
    cnpjcpf = models.CharField(db_column='CNPJCPF', max_length=18, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    idcontato = models.IntegerField(db_column='IDContato', blank=True, null=True)  # Field name made lowercase.
    contato = models.CharField(db_column='Contato', max_length=60, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    telcelular = models.CharField(db_column='TelCelular', max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    whats = models.CharField(db_column='Whats', max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    idtipopedido = models.IntegerField(db_column='IDTipoPedido', blank=True, null=True)  # Field name made lowercase.
    idpreco = models.IntegerField(db_column='IDPreco', blank=True, null=True)  # Field name made lowercase.
    prazomedio = models.IntegerField(db_column='PrazoMedio', blank=True, null=True)  # Field name made lowercase.
    idpagamento = models.IntegerField(db_column='IDPagamento', blank=True, null=True)  # Field name made lowercase.
    idendereco = models.IntegerField(db_column='IDEndereco', blank=True, null=True)  # Field name made lowercase.
    pervolume = models.DecimalField(db_column='PerVolume', max_digits=6, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    perclientetabela = models.DecimalField(db_column='PerClienteTabela', max_digits=6, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    percascata1 = models.DecimalField(db_column='PerCascata1', max_digits=6, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    percascata2 = models.DecimalField(db_column='PerCascata2', max_digits=6, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    percascata3 = models.DecimalField(db_column='PerCascata3', max_digits=6, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    percascata4 = models.DecimalField(db_column='PerCascata4', max_digits=6, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    perdescfinal = models.DecimalField(db_column='PerDescFinal', max_digits=6, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    idcascata = models.IntegerField(db_column='IDCascata', blank=True, null=True)  # Field name made lowercase.
    idvolume = models.IntegerField(db_column='IDVolume', blank=True, null=True)  # Field name made lowercase.
    tipofrete = models.IntegerField(db_column='TipoFrete', blank=True, null=True)  # Field name made lowercase.
    idtransportador = models.IntegerField(db_column='IDTransportador', blank=True, null=True)  # Field name made lowercase.
    idtipotransporte = models.IntegerField(db_column='IDTipoTransporte', blank=True, null=True)  # Field name made lowercase.
    idredespacho = models.IntegerField(db_column='IDRedespacho', blank=True, null=True)  # Field name made lowercase.
    dtprogramacao = models.DateField(db_column='DtProgramacao', blank=True, null=True)  # Field name made lowercase.
    idcarimbo = models.IntegerField(db_column='IDCarimbo', blank=True, null=True)  # Field name made lowercase.
    idcodigovenda = models.IntegerField(db_column='IDCodigoVenda', blank=True, null=True)  # Field name made lowercase.
    usardescontovolume = models.CharField(db_column='UsarDescontoVolume', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    usardescontocascata = models.CharField(db_column='UsarDescontoCascata', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    habilitardescontovolume = models.CharField(db_column='HabilitarDescontoVolume', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    habilitardescontocliente = models.CharField(db_column='HabilitarDescontoCliente', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    habilitardescontocascata = models.CharField(db_column='HabilitarDescontoCascata', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    habilitardescontoadicional = models.CharField(db_column='HabilitarDescontoAdicional', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    visualizarsaldoestoque = models.CharField(db_column='VisualizarSaldoEstoque', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    usarpedidominimo = models.CharField(db_column='UsarPedidoMinimo', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    controlamargem = models.CharField(db_column='ControlaMargem', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    controlaestoque = models.CharField(db_column='ControlaEstoque', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    permaxvolume = models.DecimalField(db_column='PerMaxVolume', max_digits=6, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    permaxclientetabela = models.DecimalField(db_column='PerMaxClienteTabela', max_digits=6, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    sigla1 = models.CharField(db_column='Sigla1', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    permaxcascata1 = models.DecimalField(db_column='PerMaxCascata1', max_digits=6, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    sigla2 = models.CharField(db_column='Sigla2', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    permaxcascata2 = models.DecimalField(db_column='PerMaxCascata2', max_digits=6, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    sigla3 = models.CharField(db_column='Sigla3', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    permaxcascata3 = models.DecimalField(db_column='PerMaxCascata3', max_digits=6, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    sigla4 = models.CharField(db_column='Sigla4', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    permaxcascata4 = models.DecimalField(db_column='PerMaxCascata4', max_digits=6, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    idvolumefaixa = models.IntegerField(db_column='IDVolumeFaixa', blank=True, null=True)  # Field name made lowercase.
    idworkflow = models.IntegerField(db_column='IDWorkFlow', blank=True, null=True)  # Field name made lowercase.
    obsvendedor = models.CharField(db_column='ObsVendedor', max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    obspedido = models.CharField(db_column='ObsPedido', max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    obsnota = models.CharField(db_column='ObsNota', max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    pedidoconcluido = models.CharField(db_column='PedidoConcluido', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    vlfrete = models.DecimalField(db_column='VlFrete', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vldespesas = models.DecimalField(db_column='VlDespesas', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vlseguro = models.DecimalField(db_column='VlSeguro', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vloutras = models.DecimalField(db_column='VLOutras', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    alteroudespesa = models.CharField(db_column='AlterouDespesa', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    idenderecoentrega = models.IntegerField(db_column='IDEnderecoEntrega', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TEMPPedido'


class Temppedidoproduto(models.Model):
    spid = models.IntegerField()
    nritem = models.SmallIntegerField(db_column='NrItem', blank=True, null=True)  # Field name made lowercase.
    idproduto = models.IntegerField(db_column='IDProduto', blank=True, null=True)  # Field name made lowercase.
    codembalagem = models.IntegerField(db_column='CodEmbalagem', blank=True, null=True)  # Field name made lowercase.
    precooriginal = models.DecimalField(db_column='PrecoOriginal', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    precobase = models.DecimalField(db_column='PrecoBase', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    perdescanterior = models.DecimalField(db_column='PerDescAnterior', max_digits=7, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    perdescpedido = models.DecimalField(db_column='PerDescPedido', max_digits=7, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    perdescitem = models.DecimalField(db_column='PerDescItem', max_digits=7, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    vldesconto = models.DecimalField(db_column='VlDesconto', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vlliquido = models.DecimalField(db_column='VlLiquido', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    qtitem = models.DecimalField(db_column='QTItem', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    qtcortada = models.DecimalField(db_column='QTCortada', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vlmercadoria = models.DecimalField(db_column='VlMercadoria', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    observacao = models.CharField(db_column='Observacao', max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    alteroupreco = models.CharField(db_column='AlterouPreco', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    mensagem = models.CharField(db_column='Mensagem', max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    vlmargem = models.DecimalField(db_column='VLMargem', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    prmargem = models.DecimalField(db_column='PRMargem', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    vlfrete = models.DecimalField(db_column='VLFrete', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vlseguro = models.DecimalField(db_column='VLSeguro', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vldespesas = models.DecimalField(db_column='VLDespesas', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vloutras = models.DecimalField(db_column='VLOutras', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    ccfop = models.SmallIntegerField(db_column='cCFOP', blank=True, null=True)  # Field name made lowercase.
    vlbase = models.DecimalField(db_column='VLBase', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    idicmscst = models.CharField(db_column='IDICMSCST', max_length=4, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    idicmstipobase = models.CharField(db_column='IDICMSTipoBase', max_length=4, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    pricmsreducaobase = models.DecimalField(db_column='PRICMSReducaoBase', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    icmssomaipi = models.CharField(db_column='ICMSSomaIPI', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    vlicmsbase = models.DecimalField(db_column='VLICMSBase', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pricms = models.DecimalField(db_column='PRICMS', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    vlicms = models.DecimalField(db_column='VLICMS', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vlicmsbasefcp = models.DecimalField(db_column='VLICMSBaseFCP', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pricmsfcp = models.DecimalField(db_column='PRICMSFCP', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    vlicmsfcp = models.DecimalField(db_column='VLICMSFCP', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vlicmsbasefcpufdestino = models.DecimalField(db_column='VLICMSBaseFCPUFDestino', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pricmsfcpufdestino = models.DecimalField(db_column='PRICMSFCPUFDestino', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    vlicmsfcpufdestino = models.DecimalField(db_column='VLICMSFCPUFDestino', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vlicmsbasefcpst = models.DecimalField(db_column='VLICMSBaseFCPST', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pricmsfcpst = models.DecimalField(db_column='PRICMSFCPST', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    vlicmsfcpst = models.DecimalField(db_column='VLICMSFCPST', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vlicmsbasefcpretido = models.DecimalField(db_column='VLICMSBaseFCPRetido', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pricmsfcpretido = models.DecimalField(db_column='PRICMSFCPRetido', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    vlicmsfcpretido = models.DecimalField(db_column='VLICMSFCPRetido', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pricmsfcpdiferimento = models.DecimalField(db_column='PRICMSFCPDiferimento', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    vlicmsfcpdiferimento = models.DecimalField(db_column='VLICMSFCPDiferimento', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vlicmsfcpefetivo = models.DecimalField(db_column='VLICMSFCPEfetivo', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pricmsnaocomputado = models.DecimalField(db_column='PRICMSNaoComputado', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    pricmsdiferimento = models.DecimalField(db_column='PRICMSDiferimento', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    vlicmsdiferimentooperacao = models.DecimalField(db_column='VLICMSDiferimentoOperacao', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vlicmsdiferimento = models.DecimalField(db_column='VLICMSDiferimento', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vlicmsdiferido = models.DecimalField(db_column='VLICMSDiferido', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pricmsdesoneracao = models.DecimalField(db_column='PRICMSDesoneracao', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    vlicmsdesoneracao = models.DecimalField(db_column='VLICMSDesoneracao', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    idicmsmotivodesoneracao = models.IntegerField(db_column='IDICMSMotivoDesoneracao', blank=True, null=True)  # Field name made lowercase.
    idicmssttipobase = models.CharField(db_column='IDICMSSTTipoBase', max_length=4, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    vlicmsstbase = models.DecimalField(db_column='VLICMSSTBase', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pricmsstmva = models.DecimalField(db_column='PRICMSSTMVA', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    pricmsstreducao = models.DecimalField(db_column='PRICMSSTReducao', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    vlicmsstpauta = models.DecimalField(db_column='VLICMSSTPauta', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pricmsst = models.DecimalField(db_column='PRICMSST', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    vlicmsst = models.DecimalField(db_column='VLICMSST', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vlicmsstnaocomputado = models.DecimalField(db_column='VLICMSSTNaoComputado', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vlicmsstbasenaocomputado = models.DecimalField(db_column='VLICMSSTBaseNaoComputado', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    usaicmsstvalorreferencia = models.CharField(db_column='UsaICMSSTValorReferencia', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    vlicmsstreferencia = models.DecimalField(db_column='VLICMSSTReferencia', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pricmsstpauta = models.DecimalField(db_column='PRICMSSTPauta', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    idicmsstmotivodesoneracao = models.IntegerField(db_column='IDICMSSTMotivoDesoneracao', blank=True, null=True)  # Field name made lowercase.
    vlicmsstdesoneracao = models.DecimalField(db_column='VLICMSSTDesoneracao', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pricmsdifalpartilha = models.DecimalField(db_column='PRICMSDifalPartilha', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    pricmssimplescredito = models.DecimalField(db_column='PRICMSSimplesCredito', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    vlicmssimplescredito = models.DecimalField(db_column='VLICMSSimplesCredito', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vlicmsdifalbase = models.DecimalField(db_column='VLICMSDifalBase', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vlicmsdifalpartilhaorigem = models.DecimalField(db_column='VLICMSDifalPartilhaOrigem', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vlicmsdifalpartilhadestino = models.DecimalField(db_column='VLICMSDifalPartilhaDestino', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pricmsdifal = models.DecimalField(db_column='PRICMSDifal', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    vlicmsdifal = models.DecimalField(db_column='VLICMSDifal', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pricmsdifalinterno = models.DecimalField(db_column='PRICMSDifalInterno', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    pricmsdifalinterestadual = models.DecimalField(db_column='PRICMSDifalInterestadual', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    vlicmsisentas = models.DecimalField(db_column='VLICMSIsentas', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vlicmsoutras = models.DecimalField(db_column='VLICMSOutras', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vlicmsefetivobase = models.DecimalField(db_column='VLICMSEfetivoBase', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vlicmsefetivo = models.DecimalField(db_column='VLICMSEfetivo', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pricmsefetivo = models.DecimalField(db_column='PRICMSEfetivo', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    usaicmsefetivo = models.CharField(db_column='UsaICMSEfetivo', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    pricmsreducaobaseefetivo = models.DecimalField(db_column='PRICMSReducaoBaseEfetivo', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    pricmspautamaximo = models.DecimalField(db_column='PRICMSPautaMaximo', max_digits=20, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    vlicmssubstitutoretido = models.DecimalField(db_column='VLICMSSubstitutoRetido', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pricmsantecipacao = models.DecimalField(db_column='PRICMSAntecipacao', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    pricmsmvaantecipacao = models.DecimalField(db_column='PRICMSMVAAntecipacao', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    pricmsreducaoantecipacao = models.DecimalField(db_column='PRICMSReducaoAntecipacao', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    vlicmspautaantecipacao = models.DecimalField(db_column='VLICMSPautaAntecipacao', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    dtvencpautaantecipacao = models.DateField(db_column='DTVencPautaAntecipacao', blank=True, null=True)  # Field name made lowercase.
    idipicst = models.CharField(db_column='IDIPICST', max_length=4, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    idipicenq = models.CharField(db_column='IDIPICenq', max_length=4, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    vlipibase = models.DecimalField(db_column='VLIPIBase', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pripi = models.DecimalField(db_column='PRIPI', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    qtipiunidade = models.BigIntegerField(db_column='QTIPIUnidade', blank=True, null=True)  # Field name made lowercase.
    vlipiunidade = models.DecimalField(db_column='VLIPIUnidade', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vlipi = models.DecimalField(db_column='VLIPI', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vlipiisentas = models.DecimalField(db_column='VLIPIIsentas', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vlipioutras = models.DecimalField(db_column='VLIPIOutras', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vlipidevolucao = models.DecimalField(db_column='VLIPIDevolucao', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    idpiscst = models.CharField(db_column='IDPISCST', max_length=4, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    pissomaicms = models.CharField(db_column='PISSomaICMS', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    vlpisbase = models.DecimalField(db_column='VLPISBase', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    prpis = models.DecimalField(db_column='PRPIS', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    qtpisunidade = models.BigIntegerField(db_column='QTPISUnidade', blank=True, null=True)  # Field name made lowercase.
    vlpisunidade = models.DecimalField(db_column='VLPISUnidade', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vlpis = models.DecimalField(db_column='VLPIS', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vlpisstbase = models.DecimalField(db_column='VLPISSTBase', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    prpisst = models.DecimalField(db_column='PRPISST', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    qtpisstunidade = models.BigIntegerField(db_column='QTPISSTUnidade', blank=True, null=True)  # Field name made lowercase.
    vlpisstunidade = models.DecimalField(db_column='VLPISSTUnidade', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vlpisst = models.DecimalField(db_column='VLPISST', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    idcofinscst = models.CharField(db_column='IDCOFINSCST', max_length=4, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cofinssomaicms = models.CharField(db_column='COFINSSomaICMS', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    vlcofinsbase = models.DecimalField(db_column='VLCOFINSBase', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    prcofins = models.DecimalField(db_column='PRCOFINS', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    qtcofinsunidade = models.BigIntegerField(db_column='QTCOFINSUnidade', blank=True, null=True)  # Field name made lowercase.
    vlcofinsunidade = models.DecimalField(db_column='VLCOFINSUnidade', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vlcofins = models.DecimalField(db_column='VLCOFINS', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vlcofinsstbase = models.DecimalField(db_column='VLCOFINSSTBase', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    prcofinsst = models.DecimalField(db_column='PRCOFINSST', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    qtcofinsstunidade = models.BigIntegerField(db_column='QTCOFINSSTUnidade', blank=True, null=True)  # Field name made lowercase.
    vlcofinsstunidade = models.DecimalField(db_column='VLCOFINSSTUnidade', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vlcofinsst = models.DecimalField(db_column='VLCOFINSST', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    idconfiguracaofiscal = models.BigIntegerField(db_column='IDConfiguracaoFiscal', blank=True, null=True)  # Field name made lowercase.
    usachavenatural = models.CharField(db_column='UsaChaveNatural', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    vldescontodesoneracao = models.DecimalField(db_column='VLDescontoDesoneracao', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    descontardesoneracao = models.CharField(db_column='DescontarDesoneracao', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    idcbenef = models.BigIntegerField(db_column='IDcbenef', blank=True, null=True)  # Field name made lowercase.
    idchavenatural = models.CharField(db_column='IDChaveNatural', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    piscofinssomanota = models.CharField(db_column='PISCOFINSSomaNota', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    somaracrescimobase = models.CharField(db_column='SomarAcrescimoBase', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    tipogravacao = models.CharField(db_column='TipoGravacao', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    qtsaldo = models.DecimalField(db_column='QTsaldo', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vlcusto = models.DecimalField(db_column='VLcusto', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    usaoferta = models.CharField(db_column='UsaOferta', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    idoferta = models.IntegerField(db_column='IDOferta', blank=True, null=True)  # Field name made lowercase.
    cormargem = models.CharField(db_column='CorMargem', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    alterardesconto = models.CharField(db_column='AlterarDesconto', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    qtminimo = models.DecimalField(db_column='QTMinimo', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    qtmultiplo = models.DecimalField(db_column='QTMultiplo', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TEMPPedidoProduto'


class Temptabeladeprecos(models.Model):
    selecionado = models.CharField(db_column='Selecionado', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    codtabela = models.TextField(db_column='CodTabela', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    empresaerp = models.IntegerField(db_column='EmpresaERP', blank=True, null=True)  # Field name made lowercase.
    destabela = models.TextField(db_column='DesTabela', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    embtabela = models.IntegerField(db_column='EmbTabela', blank=True, null=True)  # Field name made lowercase.
    datainicial = models.DateTimeField(db_column='DataInicial', blank=True, null=True)  # Field name made lowercase.
    datafinal = models.DateTimeField(db_column='DataFinal', blank=True, null=True)  # Field name made lowercase.
    permargdesejavel = models.DecimalField(db_column='PerMargDesejavel', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    permargminima = models.DecimalField(db_column='PerMargMinima', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    tipofrete = models.IntegerField(db_column='TipoFrete', blank=True, null=True)  # Field name made lowercase.
    descomposto = models.DecimalField(db_column='DesComposto', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    perdesconto = models.DecimalField(db_column='PerDesconto', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    idprecoregra = models.IntegerField(db_column='IDPrecoRegra', blank=True, null=True)  # Field name made lowercase.
    idvolume = models.IntegerField(db_column='IDVolume', blank=True, null=True)  # Field name made lowercase.
    listalocal = models.TextField(db_column='ListaLocal', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    conexao_id = models.SmallIntegerField()
    idusuario = models.IntegerField(db_column='IDUsuario', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TEMPTabelaDePrecos'


class TsisAlteracaobancodados(models.Model):
    id_evento = models.CharField(primary_key=True, max_length=36)
    dh_evento = models.DateTimeField()
    tp_evento = models.CharField(max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    dh_publicacao = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    spid = models.IntegerField(blank=True, null=True)
    nm_servidor = models.CharField(max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    nm_login = models.CharField(max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    nm_usuario = models.CharField(max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    nm_base_dados = models.CharField(max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    nm_schema = models.CharField(max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    nm_objeto = models.CharField(max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    tp_objeto = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    comando_sql = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    xml_evento = models.TextField(blank=True, null=True)  # This field type is a guess.
    ds_hash = models.CharField(max_length=750, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TSIS_AlteracaoBancoDados'


class Tabelafiscal(models.Model):
    idtabelafiscal = models.AutoField(db_column='IDTabelaFiscal', primary_key=True)  # Field name made lowercase.
    desctabelafiscal = models.CharField(db_column='DescTabelaFiscal', max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    situacao = models.CharField(db_column='Situacao', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TabelaFiscal'


class Tabelafiscalicmspauta(models.Model):
    idicmspauta = models.IntegerField(db_column='IDICMSPauta')  # Field name made lowercase.
    idproduto = models.IntegerField(db_column='IDProduto', blank=True, null=True)  # Field name made lowercase.
    codigoncm = models.CharField(db_column='CodigoNCM', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    uforigem = models.CharField(db_column='UFOrigem', max_length=2, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ufdestino = models.CharField(db_column='UFDestino', max_length=2, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    dtvigenciainicio = models.DateField(db_column='DtVigenciaInicio', blank=True, null=True)  # Field name made lowercase.
    dtvigenciafim = models.DateField(db_column='DtVigenciaFim', blank=True, null=True)  # Field name made lowercase.
    vlpauta = models.DecimalField(db_column='VlPauta', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    situacao = models.CharField(db_column='Situacao', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    pricmsdestino = models.DecimalField(db_column='PrICMSDestino', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    desccarimbopauta = models.CharField(db_column='DescCarimboPauta', max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    prpautamaximo = models.DecimalField(db_column='PrPautaMaximo', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    vlreferencia = models.DecimalField(db_column='VlReferencia', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    dtvigenciainicioreferencia = models.DateField(db_column='DtVigenciaInicioReferencia', blank=True, null=True)  # Field name made lowercase.
    dtvigenciafimreferencia = models.DateField(db_column='DtVigenciaFimReferencia', blank=True, null=True)  # Field name made lowercase.
    desccarimboreferencia = models.CharField(db_column='DescCarimboReferencia', max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TabelaFiscalICMSPauta'


class Tabelafiscalpiscofinspauta(models.Model):
    idpiscofinspauta = models.IntegerField(db_column='IDPISCOFINSPauta')  # Field name made lowercase.
    idcstpiscofins = models.CharField(db_column='IDCSTPISCOFINS', max_length=2, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    idproduto = models.BigIntegerField(db_column='IDProduto', blank=True, null=True)  # Field name made lowercase.
    codigoncm = models.CharField(db_column='CodigoNCM', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    vlpis = models.DecimalField(db_column='VlPIS', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vlcofins = models.DecimalField(db_column='VlCOFINS', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    prpis = models.DecimalField(db_column='PRPIS', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    prcofins = models.DecimalField(db_column='PRCOFINS', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    dtvigenciainicio = models.DateField(db_column='DtVigenciaInicio', blank=True, null=True)  # Field name made lowercase.
    dtvigenciafim = models.DateField(db_column='DtVigenciaFim', blank=True, null=True)  # Field name made lowercase.
    situacao = models.IntegerField(db_column='Situacao')  # Field name made lowercase.
    prreducao = models.DecimalField(db_column='PRReducao', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    deduzbaseicms = models.CharField(db_column='DeduzBaseICMS', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TabelaFiscalPISCOFINSPauta'


class Tempbloqueio(models.Model):
    arquivo = models.CharField(db_column='Arquivo', primary_key=True, max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase. The composite primary key (Arquivo, BloqueioERP) found, that is not supported. The first column is selected.
    bloqueioerp = models.IntegerField(db_column='BloqueioERP')  # Field name made lowercase.
    clienteerp = models.IntegerField(db_column='ClienteERP')  # Field name made lowercase.
    empresaerp = models.IntegerField(db_column='EmpresaERP', blank=True, null=True)  # Field name made lowercase.
    tipobloqueio = models.CharField(db_column='TipoBloqueio', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    dtbloqueio = models.DateField(db_column='DtBloqueio')  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    dtliberacao = models.DateField(db_column='DtLiberacao', blank=True, null=True)  # Field name made lowercase.
    motivo = models.CharField(db_column='Motivo', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TempBloqueio'
        unique_together = (('arquivo', 'bloqueioerp'),)


class Tempcliente(models.Model):
    arquivo = models.CharField(db_column='Arquivo', primary_key=True, max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase. The composite primary key (Arquivo, CodERP) found, that is not supported. The first column is selected.
    coderp = models.IntegerField(db_column='CodERP')  # Field name made lowercase.
    cnpjcpf = models.CharField(db_column='CNPJCPF', max_length=18, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    razao = models.CharField(db_column='Razao', max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    fantasia = models.CharField(db_column='Fantasia', max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cidade = models.CharField(db_column='Cidade', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ufcliente = models.CharField(db_column='UFCliente', max_length=2, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    situacao = models.CharField(db_column='Situacao', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cep = models.CharField(db_column='CEP', max_length=8, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    logradouro = models.CharField(db_column='Logradouro', max_length=60, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    numero = models.CharField(db_column='Numero', max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    complemento = models.CharField(db_column='Complemento', max_length=60, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bairro = models.CharField(db_column='Bairro', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    codibge = models.IntegerField(db_column='CodIBGE', blank=True, null=True)  # Field name made lowercase.
    datafundacao = models.DateField(db_column='DataFundacao', blank=True, null=True)  # Field name made lowercase.
    telfixo = models.CharField(db_column='TelFixo', max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    telcelular = models.CharField(db_column='TelCelular', max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=60, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    datanascimento = models.DateField(db_column='DataNascimento', blank=True, null=True)  # Field name made lowercase.
    funcao = models.CharField(db_column='Funcao', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    departamento = models.CharField(db_column='Departamento', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    telfixo_1 = models.CharField(db_column='TelFixo_1', max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    telcelular_1 = models.CharField(db_column='TelCelular_1', max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    numwhats = models.CharField(db_column='NumWhats', max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    emailcorp = models.CharField(db_column='EmailCorp', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    pedidocorp = models.CharField(db_column='PedidoCorp', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    emailpessoal = models.CharField(db_column='EmailPessoal', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    pedidopessoal = models.CharField(db_column='PedidoPessoal', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cnaeprincipal = models.CharField(db_column='CNAEPrincipal', max_length=7, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    descnae = models.CharField(db_column='DesCnae', max_length=300, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    inscestadual = models.CharField(db_column='InscEstadual', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    inscmunicipal = models.CharField(db_column='InscMunicipal', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    natjuridica = models.IntegerField(db_column='NatJuridica', blank=True, null=True)  # Field name made lowercase.
    desnatjuridica = models.CharField(db_column='DesNatJuridica', max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    sitfiscal = models.IntegerField(db_column='SitFiscal', blank=True, null=True)  # Field name made lowercase.
    dessituacaofiscal = models.CharField(db_column='DesSituacaofiscal', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    destinacao = models.IntegerField(db_column='Destinacao', blank=True, null=True)  # Field name made lowercase.
    desdestinacao = models.CharField(db_column='DesDestinacao', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    presencacomprador = models.IntegerField(db_column='PresencaComprador', blank=True, null=True)  # Field name made lowercase.
    despresencacomprador = models.CharField(db_column='DesPresencaComprador', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    contribuinteicms = models.CharField(db_column='ContribuinteICMS', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    descotribuinteicms = models.CharField(db_column='DesCotribuinteICMS', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    orgaopublico = models.CharField(db_column='OrgaoPublico', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    regsuframa = models.CharField(db_column='RegSuframa', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    dataregsuframa = models.DateField(db_column='DataRegSuframa', blank=True, null=True)  # Field name made lowercase.
    datavalsuframa = models.DateField(db_column='DataValSuframa', blank=True, null=True)  # Field name made lowercase.
    regtare = models.CharField(db_column='RegTare', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    dataregtare = models.DateField(db_column='DataRegTare', blank=True, null=True)  # Field name made lowercase.
    datavaltare = models.DateField(db_column='DataValTare', blank=True, null=True)  # Field name made lowercase.
    carimbo = models.IntegerField(db_column='Carimbo', blank=True, null=True)  # Field name made lowercase.
    descricaocarimbo = models.CharField(db_column='DescricaoCarimbo', max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    tipocliente = models.IntegerField(db_column='TipoCliente', blank=True, null=True)  # Field name made lowercase.
    destipocliente = models.CharField(db_column='DesTipoCliente', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    grupoeco = models.IntegerField(db_column='GrupoEco', blank=True, null=True)  # Field name made lowercase.
    desgrupoeco = models.CharField(db_column='DesGrupoEco', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    rede = models.IntegerField(db_column='Rede', blank=True, null=True)  # Field name made lowercase.
    desrede = models.CharField(db_column='DesRede', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    tipopedido = models.IntegerField(db_column='TipoPedido', blank=True, null=True)  # Field name made lowercase.
    destipopedido = models.CharField(db_column='DesTipoPedido', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    regrapreco = models.IntegerField(db_column='RegraPreco', blank=True, null=True)  # Field name made lowercase.
    prazomedio = models.IntegerField(db_column='PrazoMedio', blank=True, null=True)  # Field name made lowercase.
    descomposto = models.CharField(db_column='DesComposto', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    perdesconto = models.DecimalField(db_column='PerDesconto', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    pedidominimo = models.CharField(db_column='PedidoMinimo', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    limitecredito = models.CharField(db_column='LimiteCredito', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    tipofrete = models.IntegerField(db_column='TipoFrete', blank=True, null=True)  # Field name made lowercase.
    destipofrete = models.CharField(db_column='DesTipoFrete', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    idtransportador = models.IntegerField(db_column='IDTransportador', blank=True, null=True)  # Field name made lowercase.
    idregiao = models.IntegerField(db_column='IDRegiao', blank=True, null=True)  # Field name made lowercase.
    descgeral = models.CharField(db_column='DescGeral', max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TempCliente'
        unique_together = (('arquivo', 'coderp'),)


class Tempdashboard(models.Model):
    spid = models.IntegerField(db_column='SPID')  # Field name made lowercase.
    iddashgrafico = models.IntegerField(db_column='IDDashGrafico')  # Field name made lowercase.
    ordemlinha = models.IntegerField(db_column='OrdemLinha')  # Field name made lowercase.
    coluna1 = models.CharField(db_column='Coluna1', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    coluna2 = models.CharField(db_column='Coluna2', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    coluna3 = models.CharField(db_column='Coluna3', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    coluna4 = models.CharField(db_column='Coluna4', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    coluna5 = models.CharField(db_column='Coluna5', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    coluna6 = models.CharField(db_column='Coluna6', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    coluna7 = models.CharField(db_column='Coluna7', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    coluna8 = models.CharField(db_column='Coluna8', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    coluna9 = models.CharField(db_column='Coluna9', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    coluna10 = models.CharField(db_column='Coluna10', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    coluna11 = models.CharField(db_column='Coluna11', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    coluna12 = models.CharField(db_column='Coluna12', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    coluna13 = models.CharField(db_column='Coluna13', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    coluna14 = models.CharField(db_column='Coluna14', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    coluna15 = models.CharField(db_column='Coluna15', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    coluna16 = models.CharField(db_column='Coluna16', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    coluna17 = models.CharField(db_column='Coluna17', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    coluna18 = models.CharField(db_column='Coluna18', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    coluna19 = models.CharField(db_column='Coluna19', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    coluna20 = models.CharField(db_column='Coluna20', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    coluna31 = models.CharField(db_column='Coluna31', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    coluna32 = models.CharField(db_column='Coluna32', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    coluna33 = models.CharField(db_column='Coluna33', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    coluna34 = models.CharField(db_column='Coluna34', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    coluna35 = models.CharField(db_column='Coluna35', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    coluna36 = models.CharField(db_column='Coluna36', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    coluna37 = models.CharField(db_column='Coluna37', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    coluna38 = models.CharField(db_column='Coluna38', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    coluna39 = models.CharField(db_column='Coluna39', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    coluna30 = models.CharField(db_column='Coluna30', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    coluna41 = models.CharField(db_column='Coluna41', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    coluna42 = models.CharField(db_column='Coluna42', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    coluna43 = models.CharField(db_column='Coluna43', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    coluna44 = models.CharField(db_column='Coluna44', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    coluna45 = models.CharField(db_column='Coluna45', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    coluna46 = models.CharField(db_column='Coluna46', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    coluna47 = models.CharField(db_column='Coluna47', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    coluna48 = models.CharField(db_column='Coluna48', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    coluna49 = models.CharField(db_column='Coluna49', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    coluna40 = models.CharField(db_column='Coluna40', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    coluna51 = models.CharField(db_column='Coluna51', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    coluna52 = models.CharField(db_column='Coluna52', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    coluna53 = models.CharField(db_column='Coluna53', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    coluna54 = models.CharField(db_column='Coluna54', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    coluna55 = models.CharField(db_column='Coluna55', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    coluna56 = models.CharField(db_column='Coluna56', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    coluna57 = models.CharField(db_column='Coluna57', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    coluna58 = models.CharField(db_column='Coluna58', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    coluna59 = models.CharField(db_column='Coluna59', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    coluna50 = models.CharField(db_column='Coluna50', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TempDashBoard'


class Tempdashboardcoluna(models.Model):
    spid = models.IntegerField(db_column='SPID')  # Field name made lowercase.
    iddashgrafico = models.IntegerField(db_column='IDDashGrafico')  # Field name made lowercase.
    coluna1 = models.CharField(db_column='Coluna1', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    coluna2 = models.CharField(db_column='Coluna2', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    coluna3 = models.CharField(db_column='Coluna3', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    coluna4 = models.CharField(db_column='Coluna4', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    coluna5 = models.CharField(db_column='Coluna5', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    coluna6 = models.CharField(db_column='Coluna6', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    coluna7 = models.CharField(db_column='Coluna7', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    coluna8 = models.CharField(db_column='Coluna8', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    coluna9 = models.CharField(db_column='Coluna9', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    coluna10 = models.CharField(db_column='Coluna10', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    coluna11 = models.CharField(db_column='Coluna11', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    coluna12 = models.CharField(db_column='Coluna12', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    coluna13 = models.CharField(db_column='Coluna13', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    coluna14 = models.CharField(db_column='Coluna14', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    coluna15 = models.CharField(db_column='Coluna15', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    coluna16 = models.CharField(db_column='Coluna16', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    coluna17 = models.CharField(db_column='Coluna17', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    coluna18 = models.CharField(db_column='Coluna18', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    coluna19 = models.CharField(db_column='Coluna19', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    coluna20 = models.CharField(db_column='Coluna20', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    coluna31 = models.CharField(db_column='Coluna31', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    coluna32 = models.CharField(db_column='Coluna32', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    coluna33 = models.CharField(db_column='Coluna33', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    coluna34 = models.CharField(db_column='Coluna34', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    coluna35 = models.CharField(db_column='Coluna35', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    coluna36 = models.CharField(db_column='Coluna36', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    coluna37 = models.CharField(db_column='Coluna37', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    coluna38 = models.CharField(db_column='Coluna38', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    coluna39 = models.CharField(db_column='Coluna39', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    coluna30 = models.CharField(db_column='Coluna30', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    coluna41 = models.CharField(db_column='Coluna41', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    coluna42 = models.CharField(db_column='Coluna42', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    coluna43 = models.CharField(db_column='Coluna43', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    coluna44 = models.CharField(db_column='Coluna44', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    coluna45 = models.CharField(db_column='Coluna45', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    coluna46 = models.CharField(db_column='Coluna46', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    coluna47 = models.CharField(db_column='Coluna47', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    coluna48 = models.CharField(db_column='Coluna48', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    coluna49 = models.CharField(db_column='Coluna49', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    coluna40 = models.CharField(db_column='Coluna40', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    coluna51 = models.CharField(db_column='Coluna51', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    coluna52 = models.CharField(db_column='Coluna52', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    coluna53 = models.CharField(db_column='Coluna53', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    coluna54 = models.CharField(db_column='Coluna54', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    coluna55 = models.CharField(db_column='Coluna55', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    coluna56 = models.CharField(db_column='Coluna56', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    coluna57 = models.CharField(db_column='Coluna57', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    coluna58 = models.CharField(db_column='Coluna58', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    coluna59 = models.CharField(db_column='Coluna59', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    coluna50 = models.CharField(db_column='Coluna50', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TempDashBoardColuna'


class Templocalvenda(models.Model):
    idrepresentada = models.IntegerField(db_column='IDRepresentada')  # Field name made lowercase.
    idlocalvenda = models.IntegerField(db_column='IDLocalVenda', blank=True, null=True)  # Field name made lowercase.
    cnpj = models.CharField(db_column='CNPJ', max_length=18, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    razao = models.CharField(db_column='Razao', max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    fantasia = models.CharField(db_column='Fantasia', max_length=40, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cep = models.CharField(db_column='CEP', max_length=8, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    logradouro = models.CharField(db_column='Logradouro', max_length=60, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    numero = models.CharField(db_column='Numero', max_length=8, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    complemento = models.CharField(db_column='Complemento', max_length=60, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bairro = models.CharField(db_column='Bairro', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    codibge = models.IntegerField(db_column='CodIBGE', blank=True, null=True)  # Field name made lowercase.
    coderp = models.IntegerField(db_column='CodERP', blank=True, null=True)  # Field name made lowercase.
    situacao = models.CharField(db_column='Situacao', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    localvendapadrao = models.CharField(db_column='LocalVendaPadrao', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cdusuario = models.IntegerField(db_column='CdUsuario')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TempLocalVenda'


class Tempprodutolocal(models.Model):
    idproduto = models.IntegerField(db_column='IDProduto', blank=True, null=True)  # Field name made lowercase.
    idlocal = models.IntegerField(db_column='IDLocal', blank=True, null=True)  # Field name made lowercase.
    multvenda = models.DecimalField(db_column='MultVenda', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    minvenda = models.DecimalField(db_column='MinVenda', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    estoqueminimo = models.DecimalField(db_column='EstoqueMinimo', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    estoquepadrao = models.DecimalField(db_column='EstoquePadrao', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    permitirsaldonegativo = models.CharField(db_column='PermitirSaldoNegativo', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    coderp = models.IntegerField(db_column='CodERP', blank=True, null=True)  # Field name made lowercase.
    cnpj = models.CharField(db_column='CNPJ', max_length=18, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    fantasia = models.CharField(db_column='Fantasia', max_length=40, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cdusuario = models.IntegerField(db_column='CdUsuario', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TempProdutoLocal'


class Tipofrete(models.Model):
    idtipofrete = models.AutoField(db_column='IDTipoFrete', primary_key=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=1000, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    tipofreteerp = models.IntegerField(db_column='TipoFreteERP', blank=True, null=True)  # Field name made lowercase.
    situacao = models.CharField(db_column='Situacao', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TipoFrete'





class Tipotransporte(models.Model):
    idtipotransporte = models.AutoField(db_column='IDTipoTransporte', primary_key=True)  # Field name made lowercase.
    dstipotransporte = models.CharField(db_column='DSTipoTransporte', max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    situacao = models.CharField(db_column='Situacao', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TipoTransporte'


class Transportador(models.Model):
    idtransportador = models.AutoField(db_column='IDTransportador', primary_key=True)  # Field name made lowercase.
    coderp = models.IntegerField(db_column='CodERP')  # Field name made lowercase.
    cnpjcpf = models.CharField(db_column='CNPJCPF', unique=True, max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    razao = models.CharField(db_column='Razao', max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    fantasia = models.CharField(db_column='Fantasia', max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    situacao = models.CharField(db_column='Situacao', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    telfixo = models.CharField(db_column='TelFixo', max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    telcelular = models.CharField(db_column='TelCelular', max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Transportador'


class Transportadorlocal(models.Model):
    idtransportador = models.BigIntegerField(db_column='IDTransportador', primary_key=True)  # Field name made lowercase. The composite primary key (IDTransportador, IDLocal) found, that is not supported. The first column is selected.
    idlocal = models.IntegerField(db_column='IDLocal')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TransportadorLocal'
        unique_together = (('idtransportador', 'idlocal'),)


class Ultimacompra(models.Model):
    idproduto = models.IntegerField(db_column='IDProduto')  # Field name made lowercase.
    dtultimacompra = models.DateField(db_column='DtUltimaCompra')  # Field name made lowercase.
    idlocal = models.IntegerField(db_column='IDLocal')  # Field name made lowercase.
    vlultimacompra = models.DecimalField(db_column='VlUltimaCompra', max_digits=19, decimal_places=4)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UltimaCompra'


class Usuarioacesso(models.Model):
    idusuarioacesso = models.AutoField(db_column='IDUsuarioAcesso', primary_key=True)  # Field name made lowercase.
    registro = models.BinaryField(db_column='Registro')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UsuarioAcesso'


class Usuariobo(models.Model):
    idusuario = models.OneToOneField(Usuario, models.DO_NOTHING, db_column='IDUsuario', primary_key=True)  # Field name made lowercase.
    idpermissao = models.IntegerField(db_column='IDPermissao')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UsuarioBO'


class Usuariolocal(models.Model):
    idusuario = models.OneToOneField(Usuario, models.DO_NOTHING, db_column='IDUsuario', primary_key=True)  # Field name made lowercase. The composite primary key (IDUsuario, IDLocalVenda) found, that is not supported. The first column is selected.
    idlocalvenda = models.ForeignKey('LocalVenda', models.DO_NOTHING, db_column='IDLocalVenda')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UsuarioLocal'
        unique_together = (('idusuario', 'idlocalvenda'),)


class Usuariomensagem(models.Model):
    idmensagem = models.AutoField(db_column='IDMensagem', primary_key=True)  # Field name made lowercase.
    idusuario = models.ForeignKey(Usuario, models.DO_NOTHING, db_column='IDUsuario')  # Field name made lowercase.
    mensagem = models.CharField(db_column='Mensagem', max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    dhensagem = models.DateTimeField(db_column='Dhensagem')  # Field name made lowercase.
    idlocal = models.IntegerField(db_column='IDLocal', blank=True, null=True)  # Field name made lowercase.
    idpedido = models.ForeignKey(Pedido, models.DO_NOTHING, db_column='IDPedido', blank=True, null=True)  # Field name made lowercase.
    origem = models.CharField(db_column='Origem', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    dhleitura = models.DateTimeField(db_column='DhLeitura', blank=True, null=True)  # Field name made lowercase.
    idpedidoerp = models.BigIntegerField(db_column='IDPedidoERP', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UsuarioMensagem'


class Usuariopdv(models.Model):
    idusuario = models.OneToOneField(Usuario, models.DO_NOTHING, db_column='IDUsuario', primary_key=True)  # Field name made lowercase.
    codpdv = models.IntegerField(db_column='CodPDV')  # Field name made lowercase.
    coderp = models.IntegerField(db_column='CodERP')  # Field name made lowercase.
    idpolcomissao = models.ForeignKey(Politicacomissao, models.DO_NOTHING, db_column='IDPolComissao', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UsuarioPDV'


class Vendedor(models.Model):
    idusuario = models.OneToOneField(Usuario, models.DO_NOTHING, db_column='IDUsuario', primary_key=True)  # Field name made lowercase.
    coderp = models.IntegerField(db_column='CodERP')  # Field name made lowercase.
    idpolcomissao = models.ForeignKey(Politicacomissao, models.DO_NOTHING, db_column='IDPolComissao', blank=True, null=True)  # Field name made lowercase.
    idequipe = models.ForeignKey(Equipevenda, models.DO_NOTHING, db_column='IDEquipe', blank=True, null=True)  # Field name made lowercase.
    idlinha = models.ForeignKey(Linhaproduto, models.DO_NOTHING, db_column='IDLinha', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Vendedor'


class Representadalinha(models.Model):
    idrepresentada = models.IntegerField(db_column='IDRepresentada', primary_key=True)  # Field name made lowercase. The composite primary key (IDRepresentada, IDLinha) found, that is not supported. The first column is selected.
    idlinha = models.ForeignKey(Linhaproduto, models.DO_NOTHING, db_column='IDLinha')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'representadaLinha'
        unique_together = (('idrepresentada', 'idlinha'),)


class Sysdiagrams(models.Model):
    name = models.CharField(max_length=128, db_collation='SQL_Latin1_General_CP1_CI_AS')
    principal_id = models.IntegerField()
    diagram_id = models.AutoField(primary_key=True)
    version = models.IntegerField(blank=True, null=True)
    definition = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sysdiagrams'
        unique_together = (('principal_id', 'name'),)
