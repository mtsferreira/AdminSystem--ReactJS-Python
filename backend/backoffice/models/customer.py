# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.forms.models import model_to_dict

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

    def get_customer_address(self):
        from backoffice.models import ClienteEndereco

        address = ClienteEndereco.objects.filter(idcliente=self.idcliente)[:10]

        return list(address.values())

    def get_customer_data(self):
        from backoffice.models import ClienteDado
        from backoffice.serializers.customer import ClienteDadoSerializer

        customer = ClienteDado.objects.get(idcliente=self.idcliente)
        serializer = ClienteDadoSerializer(customer)

        return serializer.data
    
    def get_customer_fiscal(self):
        from backoffice.models import ClienteFiscal
        from backoffice.serializers.customer import ClienteFiscalSerializer

        customer = ClienteFiscal.objects.get(idcliente=self.idcliente)
        serializer = ClienteFiscalSerializer(customer)

        return serializer.data
    
    def get_customer_profile(self):
        from backoffice.models import ClientePerfil
        from backoffice.serializers.customer import ClientePerfilSerializer

        profile = ClientePerfil.objects.get(idcliente=self.idcliente)
        serializer = ClientePerfilSerializer(profile)

        return serializer.data
    
    def get_customer_stamp(self):
        from backoffice.models import Carimbo, ClienteEspecial

        try:
            customer = ClienteEspecial.objects.get(idcliente=self.idcliente)

            customer = model_to_dict(customer)

            if customer and customer['carimbo']:
                stamp = Carimbo.objects.get(idcarimbo=customer.carimbo)
                customer['descricao_carimbo'] = stamp.descricao

            return customer

        except:
            return {}
    

class ClienteB2B(models.Model):
    idusuario = models.OneToOneField('Usuario', models.DO_NOTHING, db_column='IDUsuario', primary_key=True)  # Field name made lowercase.
    cnpjcliente = models.CharField(db_column='CNPJCliente', max_length=18, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    codvendedor = models.IntegerField(db_column='CodVendedor')  # Field name made lowercase.
    perdesconto = models.DecimalField(db_column='PerDesconto', max_digits=4, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    percomissao = models.DecimalField(db_column='PerComissao', max_digits=4, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ClienteB2B'


class ClienteContato(models.Model):
    idcontato = models.AutoField(db_column='IDContato', primary_key=True)  # Field name made lowercase.
    idcliente = models.ForeignKey('Cliente', models.DO_NOTHING, db_column='IDCliente')  # Field name made lowercase.
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


class ClienteDado(models.Model):
    idcliente = models.OneToOneField('Cliente', models.DO_NOTHING, db_column='IDCliente', primary_key=True)  # Field name made lowercase.
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


class ClienteEndereco(models.Model):
    idendereco = models.AutoField(db_column='IDEndereco', primary_key=True)  # Field name made lowercase.
    idcliente = models.ForeignKey('Cliente', models.DO_NOTHING, db_column='IDCliente')  # Field name made lowercase.
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


class ClienteEspecial(models.Model):
    idcliente = models.OneToOneField('Cliente', models.DO_NOTHING, db_column='IDCliente', primary_key=True)  # Field name made lowercase.
    regsuframa = models.CharField(db_column='RegSuframa', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    dataregsuframa = models.DateField(db_column='DataRegSuframa', blank=True, null=True)  # Field name made lowercase.
    datavalsuframa = models.DateField(db_column='DataValSuframa', blank=True, null=True)  # Field name made lowercase.
    regtare = models.CharField(db_column='RegTare', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    dataregtare = models.DateField(db_column='DataRegTare', blank=True, null=True)  # Field name made lowercase.
    datavaltare = models.DateField(db_column='DataValTare', blank=True, null=True)  # Field name made lowercase.
    carimbo = models.ForeignKey('Carimbo', models.DO_NOTHING, db_column='Carimbo', blank=True, null=True)  # Field name made lowercase.
    descricaocarimbo = models.CharField(db_column='DescricaoCarimbo', max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ClienteEspecial'


class ClienteFiscal(models.Model):
    idcliente = models.OneToOneField('Cliente', models.DO_NOTHING, db_column='IDCliente', primary_key=True)  # Field name made lowercase.
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


class ClientePerfil(models.Model):
    idcliente = models.OneToOneField('Cliente', models.DO_NOTHING, db_column='IDCliente', primary_key=True)  # Field name made lowercase.
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


class ClienteTipo(models.Model):
    idclientetipo = models.AutoField(db_column='IDClienteTipo', primary_key=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    clientetipoerp = models.IntegerField(db_column='ClienteTipoERP', blank=True, null=True)  # Field name made lowercase.
    situacao = models.CharField(db_column='Situacao', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ClienteTipo'


class ClienteVendedor(models.Model):
    idclientevendedor = models.AutoField(db_column='IDClienteVendedor', primary_key=True)  # Field name made lowercase.
    idcliente = models.ForeignKey('Cliente', models.DO_NOTHING, db_column='IDCliente')  # Field name made lowercase.
    idusuario = models.IntegerField(db_column='IDUsuario')  # Field name made lowercase.
    tipousuario = models.CharField(db_column='TipoUsuario', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    idcascata = models.ForeignKey('Cascata', models.DO_NOTHING, db_column='IDCascata', blank=True, null=True)  # Field name made lowercase.
    idvolume = models.ForeignKey('Volume', models.DO_NOTHING, db_column='IDVolume', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ClienteVendedor'
        unique_together = (('idcliente', 'idusuario', 'tipousuario'),)

    def get_seller_user_info(self):
        from BO.user.user import User

        user = User(id=self.idusuario).get_user_info(user_type=[1,6,7])
        if user:
            return model_to_dict(user)
        else:
            return {}


class ClienteVisita(models.Model):
    idclientevendedor = models.OneToOneField(ClienteVendedor, models.DO_NOTHING, db_column='IDClienteVendedor', primary_key=True)  # Field name made lowercase.
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


