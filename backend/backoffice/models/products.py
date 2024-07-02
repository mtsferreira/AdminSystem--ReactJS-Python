from django.db import models
from django.forms.models import model_to_dict


class EmbUnidade(models.Model):
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
        

class Produto(models.Model):
    idproduto = models.AutoField(db_column='IDProduto', primary_key=True)  # Field name made lowercase.
    sku = models.CharField(db_column='SKU', unique=True, max_length=60, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    coderp = models.CharField(db_column='CodERP', unique=True, max_length=60, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    deserp = models.CharField(db_column='DesERP', max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    unimedida = models.CharField(db_column='UniMedida', max_length=6, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    dessecundaria = models.CharField(db_column='DesSecundaria', max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    codsecundario = models.CharField(db_column='CodSecundario', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    fabricante = models.CharField(db_column='Fabricante', max_length=40, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    marca = models.CharField(db_column='Marca', max_length=40, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    situacao = models.CharField(db_column='Situacao', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Produto'
    
    def get_product_info(self):
        from backoffice.models import ProdutoInformacao
        try:
            product_information = ProdutoInformacao.objects.get(idproduto=self.idproduto)
        except:
            product_information = ProdutoInformacao(
                idproduto_id = self.idproduto
            )
            product_information.save()
            
        return model_to_dict(product_information)
    
    def get_product_structure(self):
        from backoffice.models import ProdutoDados
        from backoffice.serializers.product import ProdutoEstruturaSerializer

        data = ProdutoDados.objects.get(idproduto=self.idproduto)
        return ProdutoEstruturaSerializer(data, many=False).data
    
    
class ProdutoDados(models.Model):
    idproduto = models.OneToOneField(Produto, models.DO_NOTHING, db_column='IDProduto', primary_key=True)  # Field name made lowercase.
    desresumida = models.CharField(db_column='DesResumida', max_length=40, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ncm = models.CharField(db_column='NCM', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    origem = models.ForeignKey('Tabgeral', models.DO_NOTHING, db_column='Origem', blank=True, null=True)  # Field name made lowercase.
    tipoproduto = models.ForeignKey('Tabgeral', models.DO_NOTHING, db_column='TipoProduto', related_name='produtodados_tipoproduto_set', blank=True, null=True)  # Field name made lowercase.
    categoria = models.ForeignKey('Categoria', models.DO_NOTHING, db_column='Categoria', blank=True, null=True)  # Field name made lowercase.
    familia = models.ForeignKey('Familia', models.DO_NOTHING, db_column='Familia', blank=True, null=True)  # Field name made lowercase.
    ggrupo = models.ForeignKey('Grandegrupo', models.DO_NOTHING, db_column='Ggrupo', blank=True, null=True)  # Field name made lowercase.
    grupo = models.ForeignKey('Grupo', models.DO_NOTHING, db_column='Grupo', blank=True, null=True)  # Field name made lowercase.
    sgrupo = models.ForeignKey('Subgrupo', models.DO_NOTHING, db_column='Sgrupo', blank=True, null=True)  # Field name made lowercase.
    curvaabc = models.CharField(db_column='CurvaABC', max_length=2, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    percomissao = models.DecimalField(db_column='PerComissao', max_digits=7, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    perdescmaximo = models.DecimalField(db_column='PerDescMaximo', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ProdutoDados'       
        
        
class ProdutoInformacao(models.Model):
    idproduto = models.OneToOneField(Produto, models.DO_NOTHING, db_column='IDProduto', primary_key=True)  # Field name made lowercase.
    desaplicacao = models.TextField(db_column='DesAplicacao', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    destecnica = models.TextField(db_column='DesTecnica', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    mensagem1 = models.CharField(db_column='Mensagem1', max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    mensagem2 = models.CharField(db_column='Mensagem2', max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    mensagem3 = models.CharField(db_column='Mensagem3', max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ProdutoInformacao'
        

class ProdutoLocal(models.Model):
    idproduto = models.IntegerField(db_column='IDProduto')  # Field name made lowercase. The composite primary key (IDProduto, IDLocal) found, that is not supported. The first column is selected.
    idlocal = models.ForeignKey('Localvenda', models.DO_NOTHING, db_column='IDLocal')  # Field name made lowercase.
    multvenda = models.DecimalField(db_column='MultVenda', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    minvenda = models.DecimalField(db_column='MinVenda', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    estoqueminimo = models.DecimalField(db_column='EstoqueMinimo', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    estoquepadrao = models.DecimalField(db_column='EstoquePadrao', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    permitirsaldonegativo = models.CharField(db_column='PermitirSaldoNegativo', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    idprodutolocal = models.AutoField(db_column='IDProdutoLocal', primary_key=True)

    class Meta:
        managed = False
        db_table = 'ProdutoLocal'
        unique_together = (('idproduto', 'idlocal'),)
        
        
class ProdutoMarca(models.Model):
    idproduto = models.OneToOneField(Produto, models.DO_NOTHING, db_column='IDProduto', primary_key=True)  # Field name made lowercase. The composite primary key (IDProduto, IDFabricante, IDMarca) found, that is not supported. The first column is selected.
    idfabricante = models.ForeignKey('Fabricante', models.DO_NOTHING, db_column='IDFabricante')  # Field name made lowercase.
    idmarca = models.ForeignKey('Marca', models.DO_NOTHING, db_column='IDMarca')  # Field name made lowercase.
    codfabricante = models.CharField(db_column='CodFabricante', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    principal = models.CharField(db_column='Principal', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ProdutoMarca'
        unique_together = (('idproduto', 'idfabricante', 'idmarca'),)
        

class ProdutoMensagem(models.Model):
    idproduto = models.IntegerField(db_column='IDProduto')  # Field name made lowercase.
    idlocal = models.IntegerField(db_column='IDLocal')  # Field name made lowercase.
    mensagem1 = models.CharField(db_column='Mensagem1', max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    mensagem2 = models.CharField(db_column='Mensagem2', max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    mensagem3 = models.CharField(db_column='Mensagem3', max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    idprodutomensagem = models.AutoField(db_column='IDProdutoMensagem', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ProdutoMensagem'
        unique_together = (('idlocal', 'idproduto'),)
        
        
    def get_local_sale(self):
        from backoffice.models import LocalVenda
        from backoffice.serializers.localsale import LocalVendaSerializer
        local_sale = LocalVenda.objects.get(idlocalvenda=self.idlocal)
        return LocalVendaSerializer(local_sale, many=False).data


class Familia(models.Model):
    idfamilia = models.AutoField(db_column='IDFamilia', primary_key=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    familiaerp = models.IntegerField(db_column='FamiliaERP', blank=True, null=True)  # Field name made lowercase.
    situacao = models.CharField(db_column='Situacao', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Familia'
        
        
class GrandeGrupo(models.Model):
    idgrandegrupo = models.AutoField(db_column='IDGrandeGrupo', primary_key=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    grandegrupoerp = models.IntegerField(db_column='GrandeGrupoERP', blank=True, null=True)  # Field name made lowercase.
    situacao = models.CharField(db_column='Situacao', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GrandeGrupo'


class Grupo(models.Model):
    idgrupo = models.AutoField(db_column='IDGrupo', primary_key=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    grupoerp = models.IntegerField(db_column='GrupoERP', blank=True, null=True)  # Field name made lowercase.
    situacao = models.CharField(db_column='Situacao', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Grupo'
        
        
class SubGrupo(models.Model):
    idsubgrupo = models.AutoField(db_column='IDSubGrupo', primary_key=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    subgrupoerp = models.IntegerField(db_column='SubGrupoERP', blank=True, null=True)  # Field name made lowercase.
    situacao = models.CharField(db_column='Situacao', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SubGrupo'
        
        
class Marca(models.Model):
    idmarca = models.AutoField(db_column='IDMarca', primary_key=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    coderp = models.IntegerField(db_column='CodERP', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Marca'


class Fabricante(models.Model):
    idfabricante = models.AutoField(db_column='IDFabricante', primary_key=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    coderp = models.IntegerField(db_column='CodERP', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Fabricante'
        
        
class Categoria(models.Model):
    idcategoria = models.AutoField(db_column='IDCategoria', primary_key=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    categoriaerp = models.IntegerField(db_column='CategoriaERP', blank=True, null=True)  # Field name made lowercase.
    situacao = models.CharField(db_column='Situacao', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Categoria'
        
        
class LinhaProduto(models.Model):
    idlinha = models.AutoField(db_column='IDLinha', primary_key=True)  # Field name made lowercase.
    deslinha = models.CharField(db_column='DesLinha', max_length=40, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    estrutura = models.CharField(db_column='Estrutura', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    situacao = models.CharField(db_column='Situacao', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Linhaproduto'


class TabGeral(models.Model):
    idtabgeral = models.AutoField(db_column='IDTabGeral', primary_key=True)  # Field name made lowercase.
    identificador = models.CharField(db_column='Identificador', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    codidentificador = models.CharField(db_column='CodIdentificador', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    texto = models.CharField(db_column='Texto', max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    situacao = models.CharField(db_column='Situacao', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TabGeral'
        unique_together = (('idtabgeral', 'identificador', 'codidentificador'),)
        
        
class Margem(models.Model):
    idmargem = models.AutoField(db_column='IDMargem', primary_key=True)  # Field name made lowercase.
    desmargem = models.CharField(db_column='DesMargem', max_length=40, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    perminproduto = models.DecimalField(db_column='PerMinProduto', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    perminpedido = models.DecimalField(db_column='PerMinPedido', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    perdesproduto = models.DecimalField(db_column='PerDesProduto', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    perdespedido = models.DecimalField(db_column='PerDesPedido', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    cor1 = models.CharField(db_column='Cor1', max_length=8, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    cor2 = models.CharField(db_column='Cor2', max_length=8, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    cor3 = models.CharField(db_column='Cor3', max_length=8, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    situacao = models.CharField(db_column='Situacao', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    visivel = models.CharField(db_column='Visivel', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    valor = models.CharField(db_column='Valor', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Margem'
        
    
class MargemEstrutura(models.Model):
    idmarestrutura = models.AutoField(db_column='IDMarEstrutura', primary_key=True)  # Field name made lowercase. The composite primary key (IDMarEstrutura, IDMargem) found, that is not supported. The first column is selected.
    idmargem = models.ForeignKey(Margem, models.DO_NOTHING, db_column='IDMargem')  # Field name made lowercase.
    idproduto = models.ForeignKey('Produto', models.DO_NOTHING, db_column='IDProduto', blank=True, null=True)  # Field name made lowercase.
    linha = models.ForeignKey('Linhaproduto', models.DO_NOTHING, db_column='Linha', blank=True, null=True)  # Field name made lowercase.
    familia = models.ForeignKey('Familia', models.DO_NOTHING, db_column='Familia', blank=True, null=True)  # Field name made lowercase.
    ggrupo = models.ForeignKey('Grandegrupo', models.DO_NOTHING, db_column='GGrupo', blank=True, null=True)  # Field name made lowercase.
    grupo = models.ForeignKey('Grupo', models.DO_NOTHING, db_column='Grupo', blank=True, null=True)  # Field name made lowercase.
    sgrupo = models.ForeignKey('Subgrupo', models.DO_NOTHING, db_column='Sgrupo', blank=True, null=True)  # Field name made lowercase.
    marca = models.ForeignKey('Tabgeral', models.DO_NOTHING, db_column='Marca', blank=True, null=True)  # Field name made lowercase.
    categoria = models.ForeignKey('Categoria', models.DO_NOTHING, db_column='Categoria', blank=True, null=True)  # Field name made lowercase.
    fabricante = models.ForeignKey('Tabgeral', models.DO_NOTHING, db_column='Fabricante', related_name='margemestrutura_fabricante_set', blank=True, null=True)  # Field name made lowercase.
    origem = models.ForeignKey('Tabgeral', models.DO_NOTHING, db_column='Origem', related_name='margemestrutura_origem_set', blank=True, null=True)  # Field name made lowercase.
    perminimo = models.DecimalField(db_column='PerMinimo', max_digits=5, decimal_places=2)  # Field name made lowercase.
    permaximo = models.DecimalField(db_column='PerMaximo', max_digits=5, decimal_places=2)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MargemEstrutura'
        unique_together = (('idmarestrutura', 'idmargem'),)
        
        
class LinhaEstrutura(models.Model):
    idestrutura = models.AutoField(db_column='IDEstrutura', primary_key=True)  # Field name made lowercase.
    idlinha = models.ForeignKey('Linhaproduto', models.DO_NOTHING, db_column='IDLinha')  # Field name made lowercase.
    familia = models.ForeignKey('Familia', models.DO_NOTHING, db_column='Familia', blank=True, null=True)  # Field name made lowercase.
    ggrupo = models.ForeignKey('Grandegrupo', models.DO_NOTHING, db_column='GGrupo', blank=True, null=True)  # Field name made lowercase.
    grupo = models.ForeignKey('Grupo', models.DO_NOTHING, db_column='Grupo', blank=True, null=True)  # Field name made lowercase.
    sgrupo = models.ForeignKey('Subgrupo', models.DO_NOTHING, db_column='Sgrupo', blank=True, null=True)  # Field name made lowercase.
    marca = models.ForeignKey('Marca', models.DO_NOTHING, db_column='Marca', blank=True, null=True)  # Field name made lowercase.
    categoria = models.ForeignKey('Categoria', models.DO_NOTHING, db_column='Categoria', blank=True, null=True)  # Field name made lowercase.
    fabricante = models.ForeignKey('Fabricante', models.DO_NOTHING, db_column='Fabricante', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LinhaEstrutura'