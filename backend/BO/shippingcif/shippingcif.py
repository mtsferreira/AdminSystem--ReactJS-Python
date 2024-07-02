from backoffice.models import FreteCif, FreteUf
from BO.helpers.database import create_columns_by_list, create_model_by_instance, search_all_fields, update_model_with_dict
from datetime import datetime
from django.core.paginator import Paginator
from django.forms.models import model_to_dict


class ShippingCif:
    def __init__(self, id=None):
        self.id = id
        self.response = {
            'status': True,
            'message': ''
        }

    def create_single_shipping_cif_location(self, infos):
        infos['idfretecif'] = self.id

        fields_to_check = {
            'idfretecif': infos['idfretecif'],
            'uforigem': infos['uforigem'],
            'codibgeorigem_id': infos['codibgeorigem'],
            'ufdestino': infos['ufdestino'],
            'codibgedestino_id': infos['codibgedestino']
        }

        try:
            FreteUf.objects.get(**fields_to_check)
            
            self.response['status'] = False
            self.response['message'] = 'Origem e Destinos já cadastrados'
            return self.response
        except:
            create_model_by_instance(FreteUf, infos)
        
            self.response['message'] = 'Dados criados com sucesso'
            return self.response    

    def delete_single_shipping_cif_location(self, id):
        FreteUf.objects.get(idfreteuf=id).delete()
        
        self.response['message'] = 'Dados deletados com sucesso'
        
        return self. response

    def edit_single_shipping_cif(self, infos):
        if self.id:
            shipping_cif = FreteCif.objects.get(idfretecif=self.id)
            update_model_with_dict(shipping_cif, infos)

            self.response['message'] = 'Dados atualizados com sucesso'
        else:
            create_model_by_instance(FreteCif, infos)

            self.response['message'] = 'Cadastro criado com sucesso'
            
        return self.response

    def get_single_shipping_cif(self):
        shipping_cif = FreteCif.objects.get(idfretecif=self.id)

        return model_to_dict(shipping_cif)
    
    def get_single_shipping_cif_location(self, page=0, rows=10):
        fields = ['uforigem', 'codibgeorigem_id', 'ufdestino', 'codibgedestino_id', 'vlminimo', 'peracrescimo', 'perdesconto']
        header_names = ['UF Origem', 'Cidade Origem', 'UF Destino', 'Cidade Destino', 'Vl. Mínimo', 'Acrescimo (%)', 'Desconto (%)']

        shipping_cif_location = FreteUf.objects.filter(idfretecif=self.id)

        p = Paginator(shipping_cif_location, rows)
        
        shipping_cif_location = p.page(int(page)+1).object_list

        self.response['total_size'] = p.count
        
        self.response['columns'] = create_columns_by_list(fields, header_names)

        self.response['shipping_cif_location'] = list(p.page(int(page)+1).object_list.values())

        self.response['shipping_cif'] = self.get_single_shipping_cif()

        self.response['message'] = 'Informações retornadas com sucesso'
        
        return self.response

    def list_shipping_cif(self, page=0, rows=10, term='', status='', isCurrent=None, isExpired=None):
        fields = ['idfretecif', 'desfretecif', 'datainicial', 'datafinal', 'perdesconto1', 'perdesconto2', 'situacao']
        header_names = ['Código', 'Descrição da Tabela', 'Data Inicial', 'Data Final', 'Desconto 1 (%)', 'Desconto 2 (%)', 'Situação']

        today = datetime.now()

        shipping_cif = FreteCif.objects.all().order_by('idfretecif')

        if term:
            shipping_cif = search_all_fields(FreteCif, shipping_cif, term)
        if status:
            shipping_cif = shipping_cif.filter(situacao=status).distinct()
        if isCurrent and not isExpired:
            shipping_cif = shipping_cif.filter(datafinal__gte=today)
        elif not isCurrent and isExpired:
            shipping_cif = shipping_cif.filter(datafinal__lte=today)

        p = Paginator(shipping_cif, rows)
        
        shipping_cif = p.page(int(page)+1).object_list

        self.response['total_size'] = p.count
        
        self.response['columns'] = create_columns_by_list(fields, header_names)

        self.response['shipping_cif'] = list(p.page(int(page)+1).object_list.values())

        self.response['message'] = 'Tabela retornada com sucesso'
        
        return self.response