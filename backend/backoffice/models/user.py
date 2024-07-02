from django.db import models


class AcessoPerfil(models.Model):
    idperfil = models.AutoField(db_column='IDPerfil', primary_key=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    situacao = models.CharField(db_column='Situacao', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Acessoperfil'

    def get_menu(self):
        from backoffice.models.user import AcessoPerfilMenu
        from backoffice.models.layout import Menu
        from backoffice.serializers.layout import MenuSerializer

        menu_profile = AcessoPerfilMenu.objects.filter(idperfil=self.idperfil).values_list('idmenu', flat=True)
        menu = Menu.objects.filter(idmenu__in=menu_profile)
        
        return MenuSerializer(menu, many=True).data


    def get_user(self):
        from backoffice.models.user import AcessoPerfilUsuario, Usuario
        from backoffice.serializers.user import UsuarioSerializer

        user_profile = AcessoPerfilUsuario.objects.filter(idperfil=self.idperfil).values_list('idusuario', flat=True)
        user = Usuario.objects.filter(idusuario__in=user_profile)
        
        return UsuarioSerializer(user, many=True).data


class AcessoPerfilMenu(models.Model):
    idperfilmenu = models.AutoField(db_column='IDPerfilMenu', primary_key=True)
    idmenu = models.ForeignKey('Menu', models.DO_NOTHING, db_column='IDMenu', blank=True, null=True)
    idperfil = models.ForeignKey('AcessoPerfil', models.DO_NOTHING, db_column='IDPerfil', blank=True, null=True)

    class Meta:
        db_table = 'AcessoPerfilMenu'


class AcessoPerfilUsuario(models.Model):
    idperfilusuario = models.AutoField(db_column='IDPerfilUsuario', primary_key=True)
    idperfil = models.ForeignKey('AcessoPerfil', models.DO_NOTHING, db_column='IDPerfil', blank=True, null=True)
    idusuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='IDUsuario', blank=True, null=True)

    class Meta:
        db_table = 'AcessoPerfilUsuario'
        
        
class Organograma(models.Model):
    idorganograma = models.AutoField(db_column='IDOrganograma', primary_key=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    nivel = models.IntegerField(db_column='Nivel')  # Field name made lowercase.
    idpai = models.ForeignKey('self', models.DO_NOTHING, db_column='IDPai', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Organograma'


class Usuario(models.Model):
    idusuario = models.AutoField(db_column='IDUsuario', primary_key=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    tipousuario = models.ForeignKey('TipoUsuario', models.DO_NOTHING, db_column='TipoUsuario', blank=True, null=True)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    sobrenome = models.CharField(db_column='Sobrenome', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    telcelular = models.CharField(db_column='TelCelular', max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    situacao = models.CharField(db_column='Situacao', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    classecomercial = models.ForeignKey('Tabgeral', models.DO_NOTHING, db_column='ClasseComercial', blank=True, null=True)  # Field name made lowercase.
    idlocal = models.IntegerField(db_column='IDLocal')  # Field name made lowercase.
    datacadastro = models.DateTimeField(db_column='DataCadastro')  # Field name made lowercase.
    dataatualiza = models.DateTimeField(db_column='DataAtualiza')  # Field name made lowercase.
    senha = models.CharField(db_column='Senha', max_length=32, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    foto = models.BinaryField(db_column='Foto', blank=True, null=True)  # Field name made lowercase.
    cpfcnpj = models.CharField(db_column='CPFCNPJ', max_length=18, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    usuarioerp = models.IntegerField(db_column='UsuarioERP', blank=True, null=True)  # Field name made lowercase.
    coderp = models.IntegerField(db_column='CodERP', blank=True, null=True)  # Field name made lowercase.
    idperfil = models.ForeignKey('Acessoperfil', models.DO_NOTHING, db_column='IDPerfil', blank=True, null=True)  # Field name made lowercase.
    idcliente = models.ForeignKey('Cliente', models.DO_NOTHING, db_column='IDCliente', blank=True, null=True)  # Field name made lowercase.
    idrepresentada = models.ForeignKey('Representada', models.DO_NOTHING, db_column='IDRepresentada', blank=True, null=True)  # Field name made lowercase.
    usarbackoffice = models.CharField(db_column='UsarBackOffice', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    usarorcamento = models.CharField(db_column='UsarOrcamento', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    idorganograma = models.ForeignKey('Organograma', models.DO_NOTHING, db_column='IDOrganograma', blank=True, null=True)  # Field name made lowercase.
    idusuariopai = models.ForeignKey('self', models.DO_NOTHING, db_column='IDUsuarioPai', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Usuario'


class TipoUsuario(models.Model):
    idtipousuario = models.IntegerField(db_column='IDTipoUsuario', primary_key=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    situacao = models.CharField(db_column='Situacao', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    tipo = models.CharField(db_column='Tipo', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TipoUsuario'