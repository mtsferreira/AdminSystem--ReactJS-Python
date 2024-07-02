from backoffice.models import Empresa, LocalVenda, LocalConfig, LocalEmail, TabGeral
from backoffice.serializers.localsale import LocalVendaSerializer
from BO.helpers.database import create_columns_by_list, search_all_fields, update_model_with_dict, create_model_by_instance
from BO.helpers.utils import boolean_to_yes_or_no
from BO.layout.general import City, Cascade, ComissionDiscount, ShippingCif, VolumeClass, OrderType
from BO.price.price import Price
from django.core.paginator import Paginator
from django.db import IntegrityError, ProgrammingError
from django.db.models import CharField, F, Value
from django.db.models.functions import Concat
from django.forms.models import model_to_dict

import binascii


class Company:
    def __init__(self, id=None):
        self.id = id
        self.response = {
            'status': True,
            'message': ''
        }

    def edit_company(self, infos):
        company = Empresa.objects.get(idempresa=self.id)

        try:
            update_model_with_dict(company, infos)

            self.response['message'] = 'Empresa salva com sucesso'
        except ProgrammingError as e:
            if 'String or binary data would be truncated' in str(e):
                self.response['status'] = False
                self.response['message'] = 'Imagem muito grande'

        return self.response

    def get_company(self, cnpj=None):
        company = Empresa.objects.all()
        if cnpj:
            company = company.filter(cnpj=cnpj)
        
        self.response['company'] = model_to_dict(company.first()) if company.first() else None
        self.response['message'] = 'Empresa listada com sucesso'

        return self.response
    

class LocalSale:
    def __init__(self, id=None):
        self.id = id
        self.response = {
            'status': True,
            'message': ''
        }
    
    def delete_local_sale_email(self):
        
        try:
            LocalEmail.objects.get(idlocalemail=self.id).delete()
        except:
            self.response['message'] = 'Vínculo com local de venda não encontrado'
            
        self.response['message'] = 'Email excluído com sucesso'
        
        return self.response
    
    def edit_config_single_local_sale(self, infos):
        
        local_sale_config = LocalConfig.objects.get(idlocal=self.id)
        
        infos = boolean_to_yes_or_no(infos)
        
        update_model_with_dict(local_sale_config, infos)
        
        self.response['message'] = 'Configuração salva com sucesso'
        
        return self.response
    
    def edit_local_sale_email(self, infos):
    
        local_venda_instance = LocalVenda.objects.get(idlocalvenda=self.id)
        tab_geral_instance = TabGeral.objects.get(idtabgeral=infos['idtipoemail_id'])

        local_sale_email, created = LocalEmail.objects.get_or_create(
            idlocal=local_venda_instance,  
            idtipoemail=tab_geral_instance,
            defaults={
                'emailresposta': infos['emailresposta'],
                'assunto': infos['assunto'],
                'corpo': infos['corpo'],
                'assinatura': infos['assinatura'],
            }
        )

        if created:
    
            self.response['message'] = 'Email criado com sucesso.'
            self.response['status'] = True
        else:
    
            self.response['message'] = 'Já existe um email com esse tipo.'
            self.response['status'] = False
    
        return self.response
    
    def edit_single_local_sale(self, infos): 
        
        if self.id:
            local_sale = LocalVenda.objects.get(idlocalvenda=self.id)
        else:
            local_sale = LocalVenda()
        
        infos['codibge_id'] = infos['codibge']
        infos['foto'] = binascii.unhexlify(infos['foto']) if infos['foto'] else None
        
        update_model_with_dict(local_sale, infos)
        
        self.response['message'] = 'Dados atualizados com sucesso'
        
        return self.response
    
    def get_local_sale_by_ids(self, id_list=[]):
        
        return LocalVenda.objects.filter(idlocalvenda__in=id_list)

    def get_local_sale_email(self, page=0, rows=10):
        
        fields = ['idtipoemail_id', 'emailresposta', 'assunto']
        header_names = ['Tipo Email', 'Email Resposta', 'Assunto']
        
        self.response['columns'] = create_columns_by_list(fields, header_names)
        
        local_sale_email = LocalEmail.objects.filter(idlocal=self.id)
        
        p = Paginator(local_sale_email, rows)
        
        self.response['local_sale_email'] = list(p.page(int(page)+1).object_list.values())  # Invés do serializer
        self.response['total_size'] = p.count                                           
        self.response['message'] = 'Lista de Email retornada com sucesso'
        
        return self.response
    
    def get_single_local_sale(self):
        
        local_sale = LocalVenda.objects.get(idlocalvenda=self.id) # pega um único objeto com esse ID específico
        
        self.response['config'] = self.get_single_local_sale_config()
        
        self.response['local_sale'] = model_to_dict(local_sale) #pega a linha referente a esse ID e tranforms em um dicionario em "loca_sale"
        
        self.response['local_sale']['foto'] = local_sale.foto.hex() if local_sale.foto else None
        self.response['message'] = 'Local de venda retornado com sucesso'
        
        return self.response
    
    def get_single_local_sale_config(self):
        
        try:
            local_sale_config = LocalConfig.objects.get(idlocal=self.id)
        except:
            local_sale_config = LocalConfig(
                idlocal=self.id,
                desccooperado=0,
                desclocal=0,
                deslimite=0,
                prazomedio=0,
                preco=0
                )
            local_sale_config.save()
            
        return model_to_dict(local_sale_config)
    
    def list_local_sale(self, page=10, rows=10, term='', status=''):
        
        fields = ['idlocalvenda', 'coderp', 'cnpj', 'razao', 'fantasia', 'situacao']
        header_names = ['ID', 'Código ERP', 'CNPJ', 'Razão', 'Fantasia', 'Situação']
        
        local_sale = LocalVenda.objects.all().order_by('idlocalvenda')
        
        if term:
            local_sale = search_all_fields(LocalVenda, local_sale, term)
        if status:
            local_sale = local_sale.filter(situacao=status)
            
        p = Paginator(local_sale, rows)
        
        local_sale = p.page(int(page)+1).object_list
        
        self.response['total_size'] = p.count
        
        self.response['columns'] = create_columns_by_list(fields, header_names)
        
        self.response['local_sale'] = LocalVendaSerializer(local_sale, many=True).data
        
        self.response['message'] = 'Locais de venda listados com sucesso'
        
        return self.response
    
    @staticmethod
    def get_local_sale_options():
        return list(LocalVenda.objects.all().values('idlocalvenda').annotate(value=F('idlocalvenda'), label=F('fantasia')))