from django.db import models

class Representada(models.Model):
    idrepresentada = models.AutoField(db_column='IDRepresentada', primary_key=True)  # Field name made lowercase.
    cnpj = models.CharField(db_column='CNPJ', max_length=18, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    razao = models.CharField(db_column='Razao', max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    fantasia = models.CharField(db_column='Fantasia', max_length=40, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    cep = models.CharField(db_column='CEP', max_length=8, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    numero = models.CharField(db_column='Numero', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    complemento = models.CharField(db_column='Complemento', max_length=60, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bairro = models.CharField(db_column='Bairro', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    codibge = models.ForeignKey('Cidade', models.DO_NOTHING, db_column='CodIBGE')  # Field name made lowercase.
    datafundacao = models.DateField(db_column='DataFundacao', blank=True, null=True)  # Field name made lowercase.
    inscestadual = models.CharField(db_column='InscEstadual', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    inscmunicipal = models.CharField(db_column='InscMunicipal', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    telfixo = models.CharField(db_column='TelFixo', max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    telcelular = models.CharField(db_column='TelCelular', max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    whatsapp = models.CharField(db_column='Whatsapp', max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    idpolcomissao = models.ForeignKey('PoliticaComissao', models.DO_NOTHING, db_column='IDPolComissao', blank=True, null=True)  # Field name made lowercase.
    coderp = models.IntegerField(db_column='CodERP')  # Field name made lowercase.
    idlinha = models.ForeignKey('LinhaProduto', models.DO_NOTHING, db_column='IDLinha', blank=True, null=True)  # Field name made lowercase.
    situacao = models.CharField(db_column='Situacao', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    logradouro = models.CharField(db_column='Logradouro', max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    idequipe = models.ForeignKey('EquipeVenda', models.DO_NOTHING, db_column='IDEquipe', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Representada'

    def get_city(self):
        from backoffice.models import Cidade
        try:
            return Cidade.objects.get(codibge=self.codibge_id).descidade
        except:
            return ''
        
    def get_status_description(self):
        return 'ATIVO' if self.situacao == 'A' else 'CANCELADO'

class RepresentadaDoc(models.Model):
    idrepresentada = models.OneToOneField(Representada, models.DO_NOTHING, db_column='IDRepresentada', primary_key=True)  # Field name made lowercase. The composite primary key (IDRepresentada, IDDocumento) found, that is not supported. The first column is selected.
    iddocumento = models.IntegerField(db_column='IDDocumento')  # Field name made lowercase.
    dtinclusao = models.DateField(db_column='DtInclusao')  # Field name made lowercase.
    documento = models.CharField(db_column='Documento', max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    dtrevisao = models.DateField(db_column='DtRevisao', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RepresentadaDoc'
        unique_together = (('idrepresentada', 'iddocumento'),)


class RepresDoc(models.Model):
    iddoc = models.AutoField(db_column='IDDoc', primary_key=True)  # Field name made lowercase.
    idrepresentada = models.ForeignKey('Representada', models.DO_NOTHING, db_column='IDRepresentada')  # Field name made lowercase.
    datainclusao = models.DateField(db_column='DataInclusao')  # Field name made lowercase.
    documento = models.TextField(db_column='Documento', db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase. This field type is a guess.
    datarevisao = models.DateField(db_column='DataRevisao', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RepresDoc'


class RepresentadaLocal(models.Model):
    idrepresentada = models.ForeignKey('Representada', models.DO_NOTHING, db_column='IDRepresentada')  # Field name made lowercase.
    idlocal = models.ForeignKey('Localvenda', models.DO_NOTHING, db_column='IDLocal')  # Field name made lowercase.
    localpadrao = models.CharField(db_column='LocalPadrao', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    idrepresentadalocal = models.AutoField(db_column='IDRepresentadaLocal', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RepresentadaLocal'


class RepresentadaRegiao(models.Model):
    idrepresentada = models.ForeignKey('Representada', models.DO_NOTHING, db_column='IDRepresentada')  # Field name made lowercase.
    idregiao = models.ForeignKey('Regiaovenda', models.DO_NOTHING, db_column='IDRegiao')  # Field name made lowercase.
    idrepresentadaregiao = models.AutoField(db_column='IDRepresentadaRegiao', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RepresentadaRegiao'
        unique_together = (('idrepresentada', 'idregiao'),)


class Representante(models.Model):
    idusuario = models.OneToOneField('Usuario', models.DO_NOTHING, db_column='IDUsuario', primary_key=True)  # Field name made lowercase.
    idrepresentada = models.ForeignKey('Representada', models.DO_NOTHING, db_column='IDRepresentada')  # Field name made lowercase.
    pedidos = models.CharField(db_column='Pedidos', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    preco = models.CharField(db_column='Preco', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Representante'