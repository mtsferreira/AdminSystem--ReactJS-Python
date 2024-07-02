from django.db import models


class RegiaoUf(models.Model):
    idregiaouf = models.AutoField(db_column='IDRegiaoUF', primary_key=True)  # Field name made lowercase. The composite primary key (IDRegiaoUF, IDRegiao) found, that is not supported. The first column is selected.
    idregiao = models.ForeignKey('Regiaovenda', models.DO_NOTHING, db_column='IDRegiao')  # Field name made lowercase.
    uf = models.CharField(db_column='UF', max_length=2, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    cidade = models.CharField(db_column='Cidade', max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RegiaoUF'
        unique_together = (('idregiaouf', 'idregiao'),)


class RegiaoVenda(models.Model):
    idregiao = models.AutoField(db_column='IDRegiao', primary_key=True)  # Field name made lowercase.
    desregiao = models.CharField(db_column='DesRegiao', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    situacao = models.CharField(db_column='Situacao', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    coderp = models.IntegerField(db_column='CodERP', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RegiaoVenda'
        
          
class RegiaoVendedor(models.Model):
    idregiao = models.OneToOneField('Regiaovenda', models.DO_NOTHING, db_column='IDRegiao', primary_key=True)  # Field name made lowercase. The composite primary key (IDRegiao, IDUsuario) found, that is not supported. The first column is selected.
    idusuario = models.IntegerField(db_column='IDUsuario')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RegiaoVendedor'
        unique_together = (('idregiao', 'idusuario'),)
        
    def get_users(self):
        from backoffice.models import Usuario
        from backoffice.serializers.user import UsuarioSerializer
        sale_regions_seller = Usuario.objects.filter(idusuario=self.idusuario)
        return UsuarioSerializer(sale_regions_seller, many=True).data