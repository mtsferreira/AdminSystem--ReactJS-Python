from backoffice.models import RegiaoUf, RegiaoVenda, RegiaoVendedor, RepresentadaRegiao
from backoffice.serializers.user import UsuarioSerializer
from backoffice.serializers.saleregions import RegiaoRepresentadaSerializer
from BO.helpers.database import create_columns_by_list, create_model_by_instance, search_all_fields, update_model_with_dict
from BO.layout.general import City
from BO.user.user import User
from django.core.paginator import Paginator
from django.db.models import F
from django.forms.models import model_to_dict


class SalesRegion:
    def __init__(self, id=None):
        self.id = id
        self.response = {
            'status': True,
            'message': ''
        }
        
    
    def create_sale_Regions(self, infos):
        
        create_model_by_instance(RegiaoVenda, infos)
        
        self.response['message'] = 'Região de venda criada com sucesso'  
        
        return self.response  
    
    def create_single_sale_regions_uf_city(self, infos):
        infos['idregiao'] = self.id
        
        infos['cidade'] = City(codibge=infos['cidade']).get_city_name_by_code()
        
        try:
            RegiaoUf.objects.get(idregiao=self.id, cidade=infos['cidade'])
            
            self.response['status'] = False
            self.response['message'] = 'UF/Cidade já cadastrados'
            
        except:
            create_model_by_instance(RegiaoUf, infos)
        
            self.response['message'] = 'Dados criados com sucesso'

        return self.response    
            
    def delete_single_sale_regions_uf_city(self, id):
        
        RegiaoUf.objects.get(idregiaouf=id).delete()
        
        self.response['message'] = 'UF/Cidade deletados com sucesso'
        
        return self.response
            
    def edit_single_sale_regions(self, infos):
        
        sale_regions = RegiaoVenda.objects.get(idregiao=self.id)
        
        update_model_with_dict(sale_regions, infos)
        
        self.response['message'] = 'Dados atualizados com sucesso'
         
        return self.response
        
    def get_single_sale_regions(self):
        
        sale_regions = RegiaoVenda.objects.get(idregiao=self.id)
        
        return model_to_dict(sale_regions)
        
    def get_single_sale_regions_represented(self, page=0, rows=10):
        fields = ['representada.coderp', 'representada.cnpj', 'representada.razao']
        header_names = ['Código ERP', 'CNPJ', 'Razão Social']
        
        sale_regions_represented = RepresentadaRegiao.objects.filter(idregiao=self.id)
        
        p = Paginator(sale_regions_represented, rows)
        
        sale_regions_represented = p.page(int(page)+1).object_list
        
        self.response['total_size'] = p.count
        
        self.response['columns'] = create_columns_by_list(fields, header_names)
        
        self.response['represented'] = RegiaoRepresentadaSerializer(sale_regions_represented, many=True).data
        
        self.response['message'] = 'Tabela retornada com sucesso'
        
        return self.response
    
    def get_single_sale_regions_seller(self, page=0, rows=10):
        
        fields = ['coderp', 'nome', 'tipousuario.descricao']
        header_names = ['Código ERP', 'Razão Social', 'Tipo de Usuário']
        
        sale_regions_seller_list = RegiaoVendedor.objects.filter(idregiao=self.id).values_list('idusuario', flat=True)
        
        sellers = User().list_user_by_id_list(sale_regions_seller_list)
        
        p = Paginator(sellers, rows)
        
        sellers = p.page(int(page)+1).object_list
        
        self.response['total_size'] = p.count
        
        self.response['columns'] = create_columns_by_list(fields, header_names)
        
        self.response['sellers'] = UsuarioSerializer(sellers, many=True).data
        
        self.response['message'] = 'Tabela retornada com sucesso'
        
        return self.response
    
    def get_single_sale_regions_uf_city(self, page=0, rows=10):
        
        fields = ['cidade', 'uf']
        header_names = ['Cidade', 'UF']
        
        sale_regions_uf_city = RegiaoUf.objects.filter(idregiao=self.id)
        
        p = Paginator(sale_regions_uf_city, rows)
        
        sale_regions_uf_city = p.page(int(page)+1).object_list
        
        self.response['total_size'] = p.count
        
        self.response['columns'] = create_columns_by_list(fields, header_names)
        
        self.response['sale_regions_uf_city'] = list(p.page(int(page)+1).object_list.values())
        
        self.response['sale_regions'] = self.get_single_sale_regions()
        
        self.response['message'] = 'Região de venda retornada com sucesso'
        
        return self.response
         
    def list_sale_regions(self, page=0, rows=10, term='', regionid=''):
        
        fields = ['idregiao', 'desregiao', 'situacao']
        header_names = ['Código', 'Descrição', 'Situação']
        
        self.response['columns'] = create_columns_by_list(fields, header_names)
        
        sale_regions = RegiaoVenda.objects.all().order_by('idregiao')
        
        if term:
            sale_regions = search_all_fields(RegiaoVenda, sale_regions, term)
        if regionid:
            sale_regions = sale_regions.filter(idregiao=regionid).distinct()
            
        p = Paginator(sale_regions, rows)
        
        self.response['total_size'] = p.count
        
        sale_regions = p.page(int(page)+1).object_list
        
        self.response['sale_regions'] = list(p.page(int(page)+1).object_list.values())
        
        self.response['message'] = 'Regiões de venda listadas com sucesso'
        
        return self.response
    
    
    @staticmethod
    def get_sale_regions_options():
        return list(RegiaoVenda.objects.filter(situacao='A').values('idregiao').annotate(value=F('idregiao'), label=F('desregiao')))