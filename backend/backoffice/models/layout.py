from django.db import models


class DashGrafico(models.Model):
    iddashgrafico = models.AutoField(db_column='IDDashGrafico', primary_key=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    iddashtipografico = models.ForeignKey('Dashtipografico', models.DO_NOTHING, db_column='IDDashTipoGrafico')  # Field name made lowercase.
    titulo = models.CharField(db_column='Titulo', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    iddashgrafico_grupo = models.IntegerField(db_column='IDDashGrafico_Grupo', blank=True, null=True)  # Field name made lowercase.
    situacao = models.CharField(db_column='Situacao', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DashGrafico'


class DashGraficoDados(models.Model):
    iddashgraficodados = models.AutoField(db_column='IDDashGraficoDados', primary_key=True)  # Field name made lowercase.
    iddashgrafico = models.ForeignKey('DashGrafico', models.DO_NOTHING, db_column='IDDashGrafico')  # Field name made lowercase.
    idlocal = models.ForeignKey('LocalVenda', models.DO_NOTHING, db_column='IDLocal')  # Field name made lowercase.
    ordemlinha = models.IntegerField(db_column='OrdemLinha')  # Field name made lowercase.
    ordemcoluna = models.IntegerField(db_column='OrdemColuna')  # Field name made lowercase.
    linha = models.CharField(db_column='Linha', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    coluna = models.CharField(db_column='Coluna', max_length=25, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    vlgrafico = models.CharField(db_column='VlGrafico', max_length=25, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    grafico = models.CharField(db_column='Grafico', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DashGraficoDados'


class DashTipoGrafico(models.Model):
    iddashtipografico = models.AutoField(db_column='IDDashTipoGrafico', primary_key=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DashTipoGrafico'


class Menu(models.Model):
    idmenu = models.AutoField(db_column='IDMenu', primary_key=True)  # Field name made lowercase.
    descmenu = models.CharField(db_column='DescMenu', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    idmenupai = models.ForeignKey('self', models.DO_NOTHING, db_column='IDMenuPai', blank=True, null=True)  # Field name made lowercase.
    nivel = models.IntegerField(db_column='Nivel')  # Field name made lowercase.
    ordem = models.IntegerField(db_column='Ordem')  # Field name made lowercase.
    icone = models.CharField(db_column='Icone', max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    url_redirect = models.CharField(db_column='Url_Redirect', max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Menu'


class MenuFavorito(models.Model):
    idfavorito = models.AutoField(db_column='IDFavorito', primary_key=True)
    idusuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='IDUsuario', blank=True, null=True)
    idmenu = models.ForeignKey('Menu', models.DO_NOTHING, db_column='IDMenu', blank=True, null=True)

    class Meta:
        db_table = 'MenuFavorito'