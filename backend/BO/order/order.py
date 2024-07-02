from backoffice.models import TipoPedido, TempCarteiraPedido
from BO.helpers.database import create_columns_by_list, create_model_by_instance, search_all_fields, update_model_with_dict
from BO.helpers.utils import boolean_to_yes_or_no
from django.core.paginator import Paginator
from django.forms.models import model_to_dict
import json

class Order:
    def __init__(self, id=None):
        self.id = id
        self.response = {
            'status': True,
            'message': ''
        }
        
    def edit_single_order_type(self, infos):    
        infos = boolean_to_yes_or_no(infos)
        
        if self.id:
            order_type = TipoPedido.objects.get(idtipopedido=self.id)
            update_model_with_dict(order_type, infos)
        else:
            create_model_by_instance(TipoPedido, infos)
        
        self.response['message'] = 'Dados atualizados com sucesso'
        
        return self.response
      
    def get_single_order_book(self):
        try:
            order_book = TempCarteiraPedido.objects.get(idcarteirapedido=self.id)
        
            self.response['order_book'] = model_to_dict(order_book)
            
            self.response['message'] = 'Pedido Encontrado.'
            
        except TempCarteiraPedido.DoesNotExist:
            
            self.response['order_book'] = None
            
            self.response['message'] = 'Pedido não encontrado.'
            
        return self.response
        
    def get_single_order_type(self):
        order_type = TipoPedido.objects.get(idtipopedido=self.id)
        
        self.response['order_type'] = model_to_dict(order_type) #pega a linha referente a esse ID e tranforms em um dicionario em "order_type"
        
        return self.response    
    
    def list_order_book(self, page=0, rows=10, local_sale=None, client=None, seller=None, order_number=None, situation=None, initial_date=None, final_date=None):
        fields = ['fantasialocal', 'nomevendedor', 'nrpedido', 'fantasiacliente', 'dtpedido', 'vlpedido', 'situacaopedido']
        header_names = ['Local de Venda', 'Vendedor', 'Nr. Pedido', 'Cliente', 'Data Emissão', 'Vl. Pedido', 'Situação']
        
        order_book = TempCarteiraPedido.objects.filter(dtpedido__gte=initial_date, dtpedido__lte=final_date).order_by('idcarteirapedido')
        
        situation = json.loads(situation)
        
        if situation:
            situation_dict = { 'inPreparation': 'EM ELABORACAO', 'salesOrder': 'PEDIDO VENDA', 'invoiced': 'FATURADO', 'canceled': 'CANCELADO' }
            search_list = []
            for key, value in situation.items():
                if value:
                    search_list.append(situation_dict[key])
            if search_list:
                order_book = order_book.filter(situacaopedido__in=search_list)
            
        if local_sale:
            order_book = order_book.filter(idlocal=local_sale)
        if seller:
            order_book = order_book.filter(idvendedor=seller)
        if client:
            order_book = order_book.filter(idcliente=client)
        if order_number:
            order_book = order_book.filter(nrpedido=order_number)
                    
        p = Paginator(order_book, rows)
        
        self.response['total_size'] = p.count
        
        self.response['columns'] = create_columns_by_list(fields, header_names)
        
        order_book = p.page(int(page)+1).object_list
        
        self.response['order_book'] = list(p.page(int(page)+1).object_list.values())
        
        self.response['message'] = 'Carteiras de pedido listadas com sucesso'
        
        return self.response
    
    def list_order_type(self, page=0, rows=10, term='', status=None):
        fields = ['coderp', 'destipopedido', 'situacao']
        header_names = ['Código ERP', 'Descrição', 'Situação']
        
        order_type = TipoPedido.objects.all().order_by('idtipopedido')
        
        if term:
            order_type = search_all_fields(TipoPedido, order_type, term)
        if status:
            order_type = order_type.filter(situacao=status).distinct()
            
        p = Paginator(order_type, rows)
        
        self.response['total_size'] = p.count
        
        self.response['columns'] = create_columns_by_list(fields, header_names)
        
        self.response['order_type'] = list(p.page(int(page)+1).object_list.values())
        
        self.response['message'] = 'Tipos de emails listados com sucesso'
        
        return self.response