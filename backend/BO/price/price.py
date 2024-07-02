from backoffice.models import (
    Preco,
    PrecoEstrutura,
    PrecoFaixa,
    PrecoPrazo,
    PrecoProduto,
    PrecoRegra
)
from backoffice.serializers.price import PrecoProdutoSerializer, PrecoRegraSerializer
from BO.helpers.database import create_columns_by_list, create_model_by_instance, search_all_fields, update_model_with_dict
from BO.helpers.utils import boolean_to_yes_or_no
from datetime import datetime
from django.core.paginator import Paginator
from django.db import IntegrityError
from django.db.models import F
from django.forms.models import model_to_dict

from datetime import datetime

class Price:
    def __init__(self, id=None):
        self.id = id
        self.response = {
            'status': True,
            'message': ''
        }

    def create_price_term(self, days):
        try:
            term = PrecoPrazo(idpreco_id=self.id, prazodias=days)
            term.save()
            self.response['message'] = 'Prazo criado com sucesso'
        except IntegrityError:
            self.response['status'] = False
            self.response['message'] = 'Prazo ja existente'

        return self.response
    
    def create_single_price_structure_composition(self, infos):
        infos['idprecoestrutura'] = self.id

        try:
            PrecoFaixa.objects.get(**infos)

            self.response['status'] = False
            self.response['message'] = 'Cadastro já existente'

            return self.response
        except:
            create_model_by_instance(PrecoFaixa, infos)

            self.response['message'] = 'Dados criados com sucesso'
            
            return self.response

    def delete_price(self):
        Preco.objects.get(idpreco=self.id).delete()

        self.response['message'] = 'Preço excluido com sucesso'
        return self.response
    
    def delete_price_structure_composition(self, id):
        PrecoFaixa.objects.get(idprecofaixa=id).delete()

        self.response['message'] = 'Dados deletados com sucesso'
        
        return self. response

    def delete_price_term(self, id):
        try:
            term = PrecoPrazo.objects.get(idprecoprazo=id)
            term.delete()

            self.response['message'] = 'Prazo excluido com sucesso'
        except:
            self.response['status'] = False
            self.response['message'] = 'Erro ao excluir prazo'

        return self.response
    
    def edit_price(self, infos):
        price = Preco.objects.get(idpreco=self.id)

        update_model_with_dict(price, infos)
        if infos['tipofrete'] == 2:
            infos['tipofrete'] = None 
        price.tipofrete_id = infos['tipofrete']
        price.save()

        self.response['message'] = 'Preço editado com sucesso'
        return self.response
    
    def edit_single_price_rules(self, infos):
        if self.id:
            price_rules = PrecoRegra.objects.get(idprecoregra=self.id)
            
        else:
            price_rules = PrecoRegra() 

        infos = boolean_to_yes_or_no(infos)
        
        update_model_with_dict(price_rules, infos)

        self.response['message'] = 'Alteração salva com sucesso'
        
        return self.response
    
    def edit_single_price_structure(self, infos):
        if self.id:
            price_structure = PrecoEstrutura.objects.get(idprecoestrutura=self.id)
            update_model_with_dict(price_structure, infos)

            self.response['message'] = 'Dados atualizados com sucesso'
        else:
            create_model_by_instance(PrecoEstrutura, infos)

            self.response['message'] = 'Cadastro criado com sucesso'
            
        return self.response

    def get_price_products(self, page=0, rows=10):
        fields = ['produto.sku', 'produto.deserp', 'produto.unimedida', 'produto.estrutura.familia.descricao', 'produto.estrutura.ggrupo.descricao', 'produto.estrutura.grupo.descricao', 'produto.estrutura.sgrupo.descricao', 'precobase', 'perdescmaximo', 'situacao']
        header_names = ['SKU', 'Descrição', 'UM', 'Família', 'Grande Grupo', 'Grupo', 'Sub Grupo', 'Preço Base', 'Desc. Máximo (%)', 'Situação']

        self.response['columns'] = create_columns_by_list(fields, header_names)

        product_price = PrecoProduto.objects.filter(idpreco=self.id).order_by('idpreco')

        p = Paginator(product_price, rows)

        self.response['total_size'] = p.count

        product_price = p.page(int(page)+1).object_list
        self.response['product_price'] = PrecoProdutoSerializer(product_price, many=True).data
        self.response['message'] = 'Produtos listados com sucesso'

        return self.response

    def get_single_price(self):
        price = Preco.objects.get(idpreco=self.id)

        self.response['price'] = model_to_dict(price)
        self.response['message'] = 'Preço obtido com sucesso'

        return self.response
    
    def get_single_price_rules(self):
        price_rules = PrecoRegra.objects.get(idprecoregra=self.id)
        
        self.response['price_rules'] = model_to_dict(price_rules)
        
        self.response['message'] = 'Informações retornadas com sucesso'
        
        return self.response
    
    def get_single_price_structure(self):
        price_structure = PrecoEstrutura.objects.get(idprecoestrutura=self.id)

        return model_to_dict(price_structure)

    def get_single_price_structure_composition(self, page=0, rows=10):
        fields = ['familia_id', 'ggrupo_id', 'grupo_id', 'sgrupo_id', 'marca_id', 'categoria_id', 'fabricante_id', 'origem_id', 'idlinha_id', 'pervariacao', 'tipovariacao']
        header_names = ['Família', 'Grande Grupo', 'Grupo', 'Sub Grupo', 'Marca', 'Categoria', 'Fabricante', 'Origem', 'Linha', 'Variação (%)', 'Tipo de Variação']

        price_structure_composition = PrecoFaixa.objects.filter(idprecoestrutura=self.id)

        p = Paginator(price_structure_composition, rows)

        price_structure_composition = p.page(int(page)+1).object_list

        self.response['total_size'] = p.count
        
        self.response['columns'] = create_columns_by_list(fields, header_names)

        self.response['price_structure_composition'] = list(p.page(int(page)+1).object_list.values())

        self.response['price_structure'] = self.get_single_price_structure()

        self.response['message'] = 'Informações retornadas com sucesso'
        
        return self.response

    def get_single_price_term(self, page=0, rows=10):
        fields = ['prazodias']
        header_names = ['Prazo Médio (dias)']

        self.response['columns'] = create_columns_by_list(fields, header_names)

        term = PrecoPrazo.objects.filter(idpreco=self.id).order_by('idprecoprazo')

        p = Paginator(term, rows)

        self.response['total_size'] = p.count
        self.response['term'] = list(p.page(int(page)+1).object_list.values())
        self.response['message'] = 'Prazos listados com sucesso'
        
        return self.response

    def list_prices(self, page=0, rows=10, term='', current=False, expired=False):
        fields = ['codtabela', 'destabela', 'embtabela', 'datainicial', 'datafinal', 'permargdesejavel', 'permargminima', 'dtatualizacao', 'perdesconto']
        header_names = ['Código ERP', 'Descrição', 'Embalagem', 'Data Inicial', 'Data Final', 'M. Desejável (%)', 'M. Mínima (%)', 'Data Atualização', 'Desconto (%)']

        self.response['columns'] = create_columns_by_list(fields, header_names)

        prices = Preco.objects.all().order_by('idpreco')

        if term:
            prices = search_all_fields(Preco, prices, term)
        if current and not expired:
            prices = prices.filter(datafinal__gte=datetime.now())
        elif not current and expired:
            prices = prices.filter(datafinal__lte=datetime.now())

        p = Paginator(prices, rows)

        self.response['total_size'] = p.count
        self.response['price'] = list(p.page(int(page)+1).object_list.values())
        self.response['message'] = 'Preços listados com sucesso'

        return self.response

    def list_price_rules(self, page=0, rows=10, term='', priceRulesCode='', isCurrent=None, isExpired=None):
        fields = ['idprecoregra', 'desregra', 'peracrescimo', 'perdesconto', 'datainicial', 'datafinal']
        header_names = ['Código', 'Descrição da Regra', 'Acréscimo (%)', 'Redução (%)', 'Data Inicial', 'Data Final']
        
        today = datetime.now()
        
        price_rules = PrecoRegra.objects.all().order_by('idprecoregra')
        
        if term:
            price_rules = search_all_fields(PrecoRegra, price_rules, term)
        if priceRulesCode:
            price_rules = price_rules.filter(idprecoregra=priceRulesCode)
        if isCurrent and not isExpired:
            price_rules = price_rules.filter(datafinal__gte=today)
        elif not isCurrent and isExpired:
            price_rules = price_rules.filter(datafinal__lte=today)
            
        p = Paginator(price_rules, rows)
        
        price_rules = p.page(int(page)+1).object_list
        
        self.response['total_size'] = p.count
        
        self.response['columns'] = create_columns_by_list(fields, header_names)
        
        self.response['price_rules'] = PrecoRegraSerializer(price_rules, many=True).data
        
        self.response['message'] = 'Tabela retornada com sucesso'
        
        return self.response
        
    def list_price_structure(self, page=0, rows=10, term='', code=None, isCurrent=None, isExpired=None):
        fields = ['idprecoestrutura', 'descprecoestrutura', 'datainicial', 'datafinal']
        header_names = ['Código', 'Descrição da Variação', 'Data Inicial', 'Data Final']

        today = datetime.now()

        price_structure = PrecoEstrutura.objects.all().order_by('idprecoestrutura')

        if term:
            price_structure = search_all_fields(PrecoEstrutura, price_structure, term).distinct()
        if code:
            price_structure = price_structure.filter(idprecoestrutura=code).distinct()
        if isCurrent and not isExpired:
            price_structure = price_structure.filter(datafinal__gte=today)
        elif not isCurrent and isExpired:
            price_structure = price_structure.filter(datafinal__lte=today)

        p = Paginator(price_structure, rows)

        price_structure = p.page(int(page)+1).object_list

        self.response['total_size'] = p.count
        
        self.response['columns'] = create_columns_by_list(fields, header_names)

        self.response['price_structure'] = list(p.page(int(page)+1).object_list.values())

        self.response['message'] = 'Tabela retornada com sucesso'
        
        return self.response
    
    
    @staticmethod
    def get_price_options():
        today = datetime.now()
        return list(Preco.objects.filter(datainicial__lte=today, datafinal__gte=today).values('idpreco').annotate(value=F('idpreco'), label=F('destabela')))
    
    @staticmethod
    def get_price_rules_options():
        return list(PrecoRegra.objects.values('idprecoregra').annotate(value=F('idprecoregra'), label=F('desregra')))
    
    @staticmethod
    def get_structure_price_options():
        today = datetime.now()
        return list(PrecoEstrutura.objects.filter(datainicial__lte=today, datafinal__gte=today).values('idprecoestrutura').annotate(value=F('idprecoestrutura'), label=F('descprecoestrutura')))