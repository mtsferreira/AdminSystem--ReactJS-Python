from backoffice.models import Categoria, EmbUnidade, Fabricante, Familia, GrandeGrupo, Grupo, LinhaEstrutura, LinhaProduto, Marca, Margem, MargemEstrutura, Produto, ProdutoDados, ProdutoInformacao, ProdutoLocal, ProdutoMarca, ProdutoMensagem, SubGrupo, TabGeral
from backoffice.serializers.product import ProdutoEstruturaSerializer, ProdutoLocalSerializer, ProdutoMarcaSerializer, ProdutoMensagemSerializer, ProdutoSerializer
from BO.helpers.database import create_columns_by_list, create_model_by_instance, update_model_with_dict, search_all_fields 
from BO.helpers.utils import boolean_to_yes_or_no
from django.core.paginator import Paginator
from django.db.models import F
from django.forms.models import model_to_dict


class Product:
    def __init__(self, id=None):
        self.id = id
        self.response = {
            'status': True,
            'message': ''
        }
        
        
    def create_product_lines(self, infos):
        create_model_by_instance(LinhaProduto, infos)
        
        self.response['message'] = 'Linha de Produto criada com sucesso'  
        
        return self.response
        
    def create_single_product_lines_structure(self, infos):
        infos['idlinha'] = self.id
        
        try:
            LinhaEstrutura.objects.get(**infos)
            
            self.response['status'] = False
            self.response['message'] = 'Cadastro já existente'
            
            return self.response
        except:
            create_model_by_instance(LinhaEstrutura, infos)
        
            self.response['message'] = 'Dados criados com sucesso'
            
            return self.response
    
    def create_single_product_margin_structure(self, infos):
        infos['idmargem'] = self.id
        
        try:
            MargemEstrutura.objects.get(**infos)
            
            self.response['status'] = False
            self.response['message'] = 'Cadastro já existente'
            
            return self.response
        except:
            create_model_by_instance(MargemEstrutura, infos)
        
            self.response['message'] = 'Dados criados com sucesso'
            
            return self.response
    
    def delete_single_product_lines_structure(self, id):
        LinhaEstrutura.objects.get(idestrutura=id).delete()
        
        self.response['message'] = 'Dados deletados com sucesso'
        
        return self. response
    
    def delete_single_product_margin_structure(self, id):
        MargemEstrutura.objects.get(idmarestrutura=id).delete()
        
        self.response['message'] = 'Informação deletada com sucesso'
        
        return self.response
    
    def edit_single_product(self, infos):
        product = Produto.objects.get(idproduto=self.id)
        product_informacao = ProdutoInformacao.objects.get(idproduto=self.id)
        update_model_with_dict(product, infos)
        update_model_with_dict(product_informacao, infos['informacao'])
        
        self.response['message'] = 'Dados atualizados com sucesso'
        
        return self.response
    
    def edit_single_product_lines(self, infos):
        product_lines = LinhaProduto.objects.get(idlinha=self.id)
        
        update_model_with_dict(product_lines, infos)
        
        self.response['message'] = 'Dados atualizados com sucesso'
         
        return self.response
    
    def edit_singel_product_local(self, product_local_id, infos):
        product_local= ProdutoLocal.objects.get(idprodutolocal=product_local_id)
        
        update_model_with_dict(product_local, infos)
        
        self.response['message'] = 'Dados atualizados com sucesso'
         
        return self.response
    
    def edit_single_product_margin(self, infos):
        infos = boolean_to_yes_or_no(infos)
        
        if self.id:
            margins = Margem.objects.get(idmargem=self.id)
            update_model_with_dict(margins, infos)
            
            self.response['message'] = 'Dados atualizados com sucesso'
        else:
            create_model_by_instance(Margem, infos)
            
            self.response['message'] = 'Cadastro criado com sucesso'
            
        return self.response
    
    def edit_single_product_message(self, infos):
        product_message = ProdutoMensagem.objects.get(idprodutomensagem=self.id)
        
        update_model_with_dict(product_message, infos)
        
        self.response['message'] = 'Dados atualizados com sucesso'
         
        return self.response
    
    def edit_single_product_structure(self, infos):
        infos['familia'] = infos['familia']['idfamilia']
        infos['ggrupo'] = infos['ggrupo']['idgrandegrupo']
        infos['grupo'] = infos['grupo']['idgrupo']
        infos['sgrupo'] = infos['sgrupo']['idsubgrupo']
        infos['origem'] = infos['origem']['idtabgeral']
        infos['tipoproduto'] = infos['tipoproduto']['idtabgeral']
        
        product_structure = ProdutoDados.objects.get(idproduto=self.id)
        
        update_model_with_dict(product_structure, infos)
        
        self.response['message'] = 'Dados atualizados com sucesso'
        
        return self.response
        
    def get_single_product(self):
        product = Produto.objects.get(idproduto=self.id)
        
        self.response['product'] = ProdutoSerializer(product, many=False).data # Um objeto (linha da tabela)
        
        self.response['message'] = 'Dados do produto retornados com sucesso'
        
        return self.response
    
    def get_single_product_brands_manufacturers(self, page=0, rows=10):
        fields = ['idfabricante', 'fabricante.descricao', 'idmarca', 'marca.descricao', 'principal']
        header_names = ['Fabricante', 'Nome do Fabricante', 'Marca', 'Descrição da Marca', 'Principal']
        
        self.response['columns'] = create_columns_by_list(fields, header_names)
        
        product_brands_manufacturers = ProdutoMarca.objects.filter(idproduto=self.id)
        
        p = Paginator(product_brands_manufacturers, rows)
        
        self.response['total_size'] = p.num_pages
        
        product_brands_manufacturers = p.page(int(page)+1).object_list
        
        self.response['product_brands_manufacturers'] = ProdutoMarcaSerializer(product_brands_manufacturers, many=True).data
        
        self.response['message'] = 'Tabela retornada com sucesso'
        
        return self.response
    
    def get_single_product_dimensions(self, page=0, rows=10):
        fields = ['unidade', 'pesobruto', 'pesoliquido', 'largura', 'altura', 'comprimento', 'codgtin', 'qtcaixa']
        header_names = ['Unidade', 'Peso Bruto (K)', 'Peso Líquido (KG)', 'Largura (CM)', 'Altura (CM)', 'Comprimento (CM)', 'Código de Barras', 'Na Caixa']
        
        self.response['columns'] = create_columns_by_list(fields, header_names)
        
        product_dimensions = EmbUnidade.objects.filter(idproduto=self.id)
        
        p = Paginator(product_dimensions, rows)
        
        self.response['total_size'] = p.num_pages
        
        product_dimensions = p.page(int(page)+1).object_list
        
        self.response['product_dimensions'] = list(p.page(int(page)+1).object_list.values())
        
        self.response['message'] = 'Dimensões do produto listadas com sucesso'
        
        return self.response
    
    def get_single_product_lines(self):
        product_lines = LinhaProduto.objects.get(idlinha=self.id)
        
        return model_to_dict(product_lines)
    
    def get_single_product_lines_structure(self, page=0, rows=10):
        fields = ['familia_id', 'ggrupo_id', 'grupo_id', 'sgrupo_id', 'marca_id', 'categoria_id', 'fabricante_id']
        header_names = ['Familia', 'Grande grupo', 'Grupo', 'Sub Grupo', 'Marca', 'Categoria', 'Fabricante']
        
        product_lines_structure = LinhaEstrutura.objects.filter(idlinha=self.id)
        
        p = Paginator(product_lines_structure, rows)
        
        product_lines_structure = p.page(int(page)+1).object_list
        
        self.response['total_size'] = p.count
        
        self.response['columns'] = create_columns_by_list(fields, header_names)
        
        self.response['product_lines_structure'] = list(p.page(int(page)+1).object_list.values())
        
        self.response['product_lines'] = self.get_single_product_lines()
        
        self.response['message'] = 'Informações retornadas com sucesso'
        
        return self.response
    
    def get_single_product_local(self, page=0, rows=10):
        fields = ['local.coderp', 'local.cnpj', 'local.fantasia', 'multvenda', 'estoquepadrao', 'estoqueminimo', 'minvenda', 'permitirsaldonegativo']
        header_names = ['Código ERP', 'CNPJ', 'Fantasia', 'Qtd Múltiplo', 'Estoque Pad.', 'Estoque Min.', 'Qtd Mínima', 'Permitir Saldo Negativo']
        
        self.response['columns'] = create_columns_by_list(fields, header_names)
        
        product_local = ProdutoLocal.objects.filter(idproduto=self.id)
        
        p = Paginator(product_local, rows)
        
        self.response['total_size'] = p.num_pages
        
        product_local = p.page(int(page)+1).object_list
        
        self.response['product_local'] = ProdutoLocalSerializer(product_local, many=True).data
        
        self.response['message'] = 'Locais do produto retornados com sucesso'
        
        return self.response
    
    def get_single_product_margin(self):
        margins = Margem.objects.get(idmargem=self.id)
        
        self.response['margins'] = model_to_dict(margins)
        
        self.response['message'] = 'Informações retornadas com sucesso'
        
        return self.response
    
    def get_single_product_margin_structure(self, page=0, rows=10):
        fields = ['idproduto_id', 'familia_id', 'ggrupo_id', 'grupo_id', 'sgrupo_id', 'marca_id', 'categoria_id', 'fabricante_id', 'origem_id', 'linha_id', 'perminimo', 'permaximo']
        header_names = ['Produto', 'Familia', 'Grande grupo', 'Grupo', 'Sub Grupo', 'Marca', 'Categoria', 'Fabricante', 'Origem', 'Linha', 'Mínimo (%)', 'Máximo (%)']
    
        margin_structure = MargemEstrutura.objects.filter(idmargem=self.id)
        
        p = Paginator(margin_structure, rows)
        
        margin_structure = p.page(int(page)+1).object_list
        
        self.response['total_size'] = p.count
        
        self.response['columns'] = create_columns_by_list(fields, header_names)
        
        self.response['margin_structure'] = list(p.page(int(page)+1).object_list.values())
        
        self.response['message'] = 'Tabela retornada com sucesso'
        
        return self.response
    
    def get_single_product_message(self, page=0, rows=10):
        fields = ['local.coderp', 'local.fantasia', 'mensagem1', 'mensagem2', 'mensagem3']
        header_names = ['Código ERP', 'Fantasia', 'Mensagem 1', 'Mensagem 2', 'Mensagem 3']
        
        self.response['columns'] = create_columns_by_list(fields, header_names)
        
        product_message = ProdutoMensagem.objects.filter(idproduto=self.id)
        
        p = Paginator(product_message, rows)
        
        self.response['total_size'] = p.num_pages
        
        product_message = p.page(int(page)+1).object_list
        
        self.response['product_message'] = ProdutoMensagemSerializer(product_message, many=True).data
        
        self.response['message'] = 'Tabela retornada com sucesso'
        
        return self.response
    
    def get_single_product_structure(self):
        product_structure = ProdutoDados.objects.get(idproduto=self.id)
        
        self.response['product_structure'] = ProdutoEstruturaSerializer(product_structure, many=False).data
        
        self.response['message'] = 'Dados da estrutura do produto retornados com sucesso'
        
        return self.response
        
    def list_product(self, page=0, rows=10, term=''):
        fields = ['sku', 'coderp', 'deserp', 'unimedida', 'fabricante', 'marca', 'situacao']
        header_names = ['SKU', 'Código ERP', 'Descrição', 'UM', 'Fabricante', 'Marca', 'Situacao']
        
        self.response['columns'] = create_columns_by_list(fields, header_names)
        
        product = Produto.objects.all().order_by('idproduto')
        
        if term:
            product = search_all_fields(Produto, product, term)
            
        p = Paginator(product, rows)
        
        self.response['total_size'] = p.num_pages
        
        product = p.page(int(page)+1).object_list
        
        self.response['product'] = ProdutoSerializer(product, many=True).data # Uma lista (filter, all) = True,  objeto único (get) = False
        
        self.response['message'] = 'Tabela retornada com sucesso'
        
        return self.response
    
    def list_product_lines(self, page=0, rows=10, term='', productlinescode='', status=None):
        fields = ['idlinha', 'deslinha', 'estrutura', 'situacao']
        header_names = ['Código', 'Descrição da Linha', 'Estrutura', 'Situacao']
        
        product_line = LinhaProduto.objects.all().order_by('idlinha')
        
        if term:
            product_line = search_all_fields(LinhaProduto, product_line, term)
        if productlinescode:
            product_line = product_line.filter(idlinha=productlinescode).distinct()
        if status:
            product_line = product_line.filter(situacao=status).distinct()
            
        p = Paginator(product_line, rows)
        
        self.response['total_size'] = p.count
        
        self.response['columns'] = create_columns_by_list(fields, header_names)
        
        self.response['product_lines'] = list(p.page(int(page)+1).object_list.values())
        
        self.response['message'] = 'Tabela retornada com sucesso'
        
        return self.response
    
    def list_product_margins(self, page=0, rows=10, term='', marginscode='', status=None):
        fields = ['idmargem', 'desmargem', 'situacao', 'cor1', 'cor2', 'cor3', 'perminproduto', 'perdesproduto', 'perminpedido', 'perdespedido']
        header_names = ['Código', 'Descrição', 'Situação', 'Desejável', 'Acima do Desejável', 'Abaixo do Desejável', 'Mínimo Produto (%)', 'Desejável Produto (%)', 'Mínimo Pedido (%)', 'Desejável Pedido (%)']
        
        margins = Margem.objects.all().order_by('idmargem')
        
        if term:
            margins = search_all_fields(Margem, margins, term)
        if marginscode:
            margins = margins.filter(idmargem=marginscode).distinct()
        if status:
            margins = margins.filter(situacao=status).distinct()
            
        p = Paginator(margins, rows)
        
        self.response['total_size'] = p.count
        
        self.response['columns'] = create_columns_by_list(fields, header_names)
        
        self.response['margins'] = list(p.page(int(page)+1).object_list.values())
        
        self.response['message'] = 'Tabela retornada com sucesso'
        
        return self.response
    
    
    @staticmethod
    def get_big_group_options():
        return list(GrandeGrupo.objects.all().values('idgrandegrupo').annotate(value=F('idgrandegrupo'), label=F('descricao')))
    
    @staticmethod
    def get_brand_options():
        return list(Marca.objects.all().values('idmarca').annotate(value=F('idmarca'), label=F('descricao')))
    
    @staticmethod
    def get_category_options():
        return list(Categoria.objects.all().values('idcategoria').annotate(value=F('idcategoria'), label=F('descricao')))
    
    @staticmethod
    def get_family_options():
        return list(Familia.objects.all().values('idfamilia').annotate(value=F('idfamilia'), label=F('descricao')))
    
    @staticmethod
    def get_group_options():
        return list(Grupo.objects.all().values('idgrupo').annotate(value=F('idgrupo'), label=F('descricao')))
    
    @staticmethod
    def get_manufacturer_options():
        return list(Fabricante.objects.all().values('idfabricante').annotate(value=F('idfabricante'), label=F('descricao')))
    
    @staticmethod
    def get_origin_options():
        return list(TabGeral.objects.all().values('idtabgeral').annotate(value=F('idtabgeral'), label=F('descricao')))
    
    @staticmethod
    def get_product_line_options():
        return list(LinhaProduto.objects.filter(situacao='A').values('idlinha').annotate(value=F('idlinha'), label=F('deslinha')))
    
    @staticmethod
    def get_product_options():
        return list(Produto.objects.filter(situacao='A').values('idproduto').annotate(value=F('idproduto'), label=F('deserp')))
    
    @staticmethod
    def get_sub_group_options():
        return list(SubGrupo.objects.all().values('idsubgrupo').annotate(value=F('idsubgrupo'), label=F('descricao')))
    
    
    