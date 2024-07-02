from backoffice.models import Representada, RepresentadaLocal, RepresentadaRegiao, Representante
from backoffice.serializers.represented import RepresentadaSerializer
from BO.helpers.database import create_columns_by_list, search_all_fields
from BO.localsale.localsale import LocalSale
from BO.salesregion.salesregion import SalesRegion
from BO.user.user import User
from django.core.paginator import Paginator
from django.db import IntegrityError
from django.forms.models import model_to_dict


class Represented:
    def __init__(self, id=None):
        self.id = id
        self.response = {
            'status': True,
            'message': ''
        }

    def change_main_represented_local_sale(self, local_sale_id):
        RepresentadaLocal.objects.filter(idrepresentada=self.id).update(localpadrao='N')
        represented = RepresentadaLocal.objects.get(idrepresentada=self.id, idlocal=local_sale_id)
        represented.localpadrao = 'S'
        represented.save()

        self.response['message'] = 'Local padrão atualizado com sucesso'

        return self.response

    def create_represented_local_sale(self, local_sale_id):
        try:
            represented = RepresentadaLocal(idrepresentada_id=self.id, idlocal_id=local_sale_id, localpadrao='N')
            represented.save()
            self.response['message'] = 'Vínculo criado com sucesso'
        except IntegrityError:
            self.response['status'] = False
            self.response['message'] = 'Vínculo ja existente'

        return self.response
    
    def create_represented_sales_region(self, region_id):
        try:
            represented = RepresentadaRegiao(idrepresentada_id=self.id, idregiao_id=region_id)
            represented.save()
            self.response['message'] = 'Vínculo criado com sucesso'
        except IntegrityError:
            self.response['status'] = False
            self.response['message'] = 'Vínculo ja existente'
            
        return self.response
    
    def delete_represented_local_sale(self, local_sale_id):
        RepresentadaLocal.objects.get(idrepresentada=self.id, idlocal=local_sale_id).delete()
        
        self.response['message'] = 'Vínculo excluido com sucesso'
        return self.response
    
    def delete_represented_sales_region(self, region_id):
        represented = RepresentadaRegiao.objects.get(idrepresentada=self.id, idregiao=region_id).delete()
        
        self.response['message'] = 'Vínculo excluido com sucesso'
        return self.response

    def edit_status(self, status):
        represented = Representada.objects.get(idrepresentada=self.id)

        represented.situacao = status
        represented.save()

        self.response['message'] = 'Situação alterada com sucesso'
        return self.response
    
    def get_represented_local_sale(self, page=0, rows=10):
        fields = ['idlocalvenda', 'cnpj', 'fantasia']
        header_names = ['Código', 'CNPJ', 'Fantasia']

        self.response['columns'] = create_columns_by_list(fields, header_names)

        local_list = RepresentadaLocal.objects.filter(idrepresentada_id=self.id).values_list('idlocal', flat=True)

        local_sale = LocalSale().get_local_sale_by_ids(id_list=local_list)

        p = Paginator(local_sale, rows)

        self.response['local_sale'] = list(p.page(int(page)+1).object_list.values(*fields))
        self.response['message'] = 'Locais de venda listados com sucesso'

        main_local_sale = RepresentadaLocal.objects.filter(idrepresentada=self.id, localpadrao='S').values_list('idlocal', flat=True)
        main_local_sale = LocalSale().get_local_sale_by_ids(id_list=main_local_sale)
        self.response['main_local_sale'] = model_to_dict(main_local_sale[0]) if main_local_sale else None

        main_local_sale_options = []
        for ls in local_sale:
            main_local_sale_options.append({'value': ls.idlocalvenda, 'label': ls.fantasia})
        self.response['main_local_sale_option'] = main_local_sale_options

        return self.response
    
    def get_represented_sales_region(self, page=0, rows=10):
        fields = ['desregiao', 'situacao']
        header_names = ['Nome Região', 'Situação']

        self.response['columns'] = create_columns_by_list(fields, header_names)

        region_list = RepresentadaRegiao.objects.filter(idrepresentada_id=self.id).values_list('idregiao', flat=True)

        sales_region = SalesRegion().get_sales_region_by_id_list(id_list=region_list)

        p = Paginator(sales_region, rows)

        self.response['local_sale'] = list(p.page(int(page)+1).object_list.values(*fields))
        self.response['message'] = 'Regiões de venda listadas com sucesso'

        return self.response
    
    def get_single_represented(self):
        represented = Representada.objects.get(idrepresentada=self.id)

        self.response['represented'] = model_to_dict(represented)
        self.response['message'] = 'Dados obtidos com sucesso'

        return self.response
    
    def list_representatives(self, page=0, rows=10):
        fields = ['nome', 'sobrenome', 'telcelular', 'email']
        header_names = ['Nome', 'Sobrenome', 'Telefone', 'Email']

        self.response['columns'] = create_columns_by_list(fields, header_names)

        user_id_list = Representante.objects.filter(idrepresentada=self.id).values_list('idusuario', flat=True)
        user = User().list_user_by_id_list(id_list=user_id_list)

        p = Paginator(user, rows)

        self.response['total_size'] = p.count

        fields.append('idusuario')

        self.response['representative'] = list(p.page(int(page)+1).object_list.values(*fields))
        self.response['message'] = 'Representantes listados com sucesso'

        return self.response

    def list_represented(self, page=0, rows=10, term='', status=None):
        fields = ['idrepresentada', 'coderp', 'cnpj', 'razao', 'fantasia', 'cidade', 'situacao']
        header_names = ['ID', 'Código ERP', 'CNPJ', 'Razão', 'Fantasia', 'Cidade', 'Situação']

        self.response['columns'] = create_columns_by_list(fields, header_names)

        represented = Representada.objects.all().order_by('idrepresentada')

        if term:
            represented = search_all_fields(Representada, represented, term)
        if status:
            represented = represented.filter(situacao=status)

        p = Paginator(represented, rows)

        self.response['total_size'] = p.count

        represented = p.page(int(page)+1).object_list

        self.response['represented'] = RepresentadaSerializer(represented, many=True).data
        self.response['message'] = 'Representadas listadas com sucesso'

        return self.response