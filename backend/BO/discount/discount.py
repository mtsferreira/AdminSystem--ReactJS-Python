from backoffice.models import Cascata, CascataFaixa, ComDesconto, ComFaixa, DescontoTipo, DescontoTipoEstrutura, Volume, VolumeFaixa
from BO.helpers.database import create_columns_by_list, create_model_by_instance, search_all_fields, update_model_with_dict
from datetime import datetime
from django.core.paginator import Paginator
from django.db.models import Q
from django.forms.models import model_to_dict


class Discount:
    def __init__(self, id=None):
        self.id = id
        self.response = {
            'status': True,
            'message': ''
        }

    def create_single_commission_discount_range(self, infos):
        infos['idcomdesconto'] = self.id

        try:
            ComFaixa.objects.get(**infos)

            self.response['status'] = False
            self.response['message'] = 'Cadastro já existente'

            return self.response
        except:
            create_model_by_instance(ComFaixa, infos)

            self.response['message'] = 'Dados criados com sucesso'
            
            return self.response

    def create_single_customer_type_discount_structure(self, infos):
        infos['iddescontotipo'] = self.id

        try:
            DescontoTipoEstrutura.objects.get(**infos)

            self.response['status'] = False
            self.response['message'] = 'Cadastro já existente'

            return self.response
        except:
            create_model_by_instance(DescontoTipoEstrutura, infos)

            self.response['message'] = 'Dados criados com sucesso'
            
            return self.response
        
    def create_single_volume_range_discount(self, infos):
        infos['idvolume'] = self.id

        try:
            exists = VolumeFaixa.objects.filter( # Verifica se exista uma informação igual e retorna true para exists caso ache
                idvolume=self.id,
            ).filter(
                Q(vlcomprasde__lt=infos['vlcomprasate'], vlcomprasate__gt=infos['vlcomprasde']) | 
                Q(vlcomprasde=infos['vlcomprasde'], vlcomprasate=infos['vlcomprasate']) 
            ).exists()

            if exists:
                self.response['status'] = False
                self.response['message'] = 'Já existe um registro abrangendo o intervalo informado.'
                return self.response
            else:
               
                create_model_by_instance(VolumeFaixa, infos)
                self.response['message'] = 'Dados criados com sucesso'
                return self.response

        except Exception as e:
            
            self.response['status'] = False
            self.response['message'] = f'Ocorreu um erro inesperado: {str(e)}'
            return self.response

    def delete_cascade_term(self, id=None):
        CascataFaixa.objects.get(idcascatafaixa=id).delete()

        self.response['message'] = 'Faixa excluida com sucesso'
        return self.response

    def delete_commission_discount_range(self, id):
        ComFaixa.objects.get(idcomfaixa=id).delete()

        self.response['message'] = 'Dados deletados com sucesso'
        
        return self. response

    def delete_customer_type_discount(self):
        DescontoTipo.objects.get(iddescontotipo=self.id).delete()

        self.response['message'] = 'Dados deletados com sucesso'
        
        return self. response

    def delete_customer_type_discount_structure(self, id):
        DescontoTipoEstrutura.objects.get(iddescontotipoestrutura=id).delete()

        self.response['message'] = 'Dados deletados com sucesso'
        
        return self. response

    def delete_volume_range_discount(self, id):
        VolumeFaixa.objects.get(idvolumefaixa=id).delete()

        self.response['message'] = 'Dados deletados com sucesso'
        
        return self. response

    def edit_cascade_discount(self, infos={}):
        discount = Cascata.objects.get(idcascata=self.id)

        update_model_with_dict(discount, infos)

        self.response['message'] = 'Desconto editado com sucesso'
        return self.response

    def edit_cascade_term(self, id=None, infos={}):
        if id:
            discount = CascataFaixa.objects.get(idcascatafaixa=id)
            update_model_with_dict(discount, infos)
            self.response['message'] = 'Cascata editada com sucesso'
        else:
            create_model_by_instance(CascataFaixa, infos)
            self.response['message'] = 'Cascata criada com sucesso'

        return self.response

    def edit_single_commission_discount(self, infos):
        if self.id:
            commission_discount = ComDesconto.objects.get(idcomdesconto=self.id)
            update_model_with_dict(commission_discount, infos)

            self.response['message'] = 'Dados atualizados com sucesso'
        else:
            create_model_by_instance(ComDesconto, infos)

            self.response['message'] = 'Cadastro criado com sucesso'
            
        return self.response

    def edit_single_customer_type_discount(self, infos):
        if self.id:
            customer_type_discount = DescontoTipo.objects.get(iddescontotipo=self.id)
            update_model_with_dict(customer_type_discount, infos)

            self.response['message'] = 'Dados atualizados com sucesso'
        else:
            create_model_by_instance(DescontoTipo, infos)

            self.response['message'] = 'Cadastro criado com sucesso'
            
        return self.response

    def edit_single_volume_discount(self, infos):
        if self.id:
            volume_discount = Volume.objects.get(idvolume=self.id)
            update_model_with_dict(volume_discount, infos)

            self.response['message'] = 'Dados atualizados com sucesso'
        else:
            create_model_by_instance(Volume, infos)

            self.response['message'] = 'Cadastro criado com sucesso'
            
        return self.response

    def get_single_cascade_discount(self):
        discount = Cascata.objects.get(idcascata=self.id)

        self.response['discount'] = model_to_dict(discount)
        self.response['message'] = 'Desconto obtido com sucesso'
        return self.response

    def get_single_commission_discount(self):
        commission_discount = ComDesconto.objects.get(idcomdesconto=self.id)

        return model_to_dict(commission_discount)

    def get_single_commission_discount_range(self, page=0, rows=10):
        fields = ['perdesconto', 'fatorcom']
        header_names = ['Faixa de Descontos Até (%)', 'Fator']

        commission_discount_range = ComFaixa.objects.filter(idcomdesconto=self.id)

        p = Paginator(commission_discount_range, rows)

        commission_discount_range = p.page(int(page)+1).object_list

        self.response['total_size'] = p.count
        
        self.response['columns'] = create_columns_by_list(fields, header_names)

        self.response['commission_discount_range'] = list(p.page(int(page)+1).object_list.values())

        self.response['commission_discount'] = self.get_single_commission_discount()

        self.response['message'] = 'Informações retornadas com sucesso'
        
        return self.response

    def get_single_customer_type_discount(self):
        customer_type_discount = DescontoTipo.objects.get(iddescontotipo=self.id)

        return model_to_dict(customer_type_discount)

    def get_single_customer_type_discount_structure(self, page=0, rows=10):
        fields = ['idproduto_id', 'idfamilia_id', 'idggrupo_id', 'idgrupo_id', 'idsgrupo_id', 'idmarca_id', 'idcategoria_id', 'idfabricante_id', 'idlinha_id', 'desconto']
        header_names = ['Produto', 'Família', 'Grande Grupo', 'Grupo', 'Sub Grupo', 'Marca', 'Categoria', 'Fabricante', 'Linha', 'Desconto (%)']

        customer_type_discount_structure = DescontoTipoEstrutura.objects.filter(iddescontotipo=self.id)

        p = Paginator(customer_type_discount_structure, rows)

        customer_type_discount_structure = p.page(int(page)+1).object_list

        self.response['total_size'] = p.count
        
        self.response['columns'] = create_columns_by_list(fields, header_names)

        self.response['customer_type_discount_structure'] = list(p.page(int(page)+1).object_list.values())

        self.response['customer_type_discount'] = self.get_single_customer_type_discount()

        self.response['message'] = 'Informações retornadas com sucesso'
        
        return self.response

    def get_single_volume_discount(self):
        volume_discount = Volume.objects.get(idvolume=self.id)

        return model_to_dict(volume_discount)

    def get_single_volume_range_discount(self, page=0, rows=10):
        fields = ['vlcomprasde', 'vlcomprasate', 'perdesconto']
        header_names = ['Compras de...', 'Até...', 'Desconto (%)']

        volume_range_discount = VolumeFaixa.objects.filter(idvolume=self.id)

        p = Paginator(volume_range_discount, rows)

        volume_range_discount = p.page(int(page)+1).object_list

        self.response['total_size'] = p.count
        
        self.response['columns'] = create_columns_by_list(fields, header_names)

        self.response['volume_range_discount'] = list(p.page(int(page)+1).object_list.values())

        self.response['volume_discount'] = self.get_single_volume_discount()

        self.response['message'] = 'Informações retornadas com sucesso'
        
        return self.response
        
    def list_cascade_discount(self, page=0, rows=10, term=''):
        fields = ['idcascata', 'descascata', 'situacao']
        header_names = ['ID', 'Descrição', 'Situação']
        
        self.response['columns'] = create_columns_by_list(fields, header_names)
        
        cascade = Cascata.objects.all().order_by('idcascata')
        
        if term:
            cascade = search_all_fields(Cascata, cascade, term, False)
            
        p = Paginator(cascade, rows)
        
        self.response['total_size'] = p.count
        self.response['discount'] = list(p.page(int(page)+1).object_list.values())
        self.response['message'] = 'Descontos listados com sucesso'
        
        return self.response

    def list_cascade_term_discount(self, page=0, rows=10):
        fields = ['idcascatafaixa', 'sigla', 'permaximo', 'tipocascata']
        header_names = ['ID', 'Sigla', 'Desconto Máximo (%)', 'Tipo Cascata']
        
        self.response['columns'] = create_columns_by_list(fields, header_names)
        
        cascade = CascataFaixa.objects.all().order_by('idcascatafaixa')
            
        p = Paginator(cascade, rows)
        
        self.response['total_size'] = p.count
        self.response['cascade'] = list(p.page(int(page)+1).object_list.values())
        self.response['message'] = 'Descontos listados com sucesso'
        
        return self.response

    def list_commission_discount(self, page=0, rows=10, term='', code=None):
        fields = ['idcomdesconto', 'descomissaodesc']
        header_names = ['Código', 'Descrição']

        commission_discount = ComDesconto.objects.all().order_by('idcomdesconto')

        if term:
            commission_discount = search_all_fields(ComDesconto, commission_discount, term).distinct()
        if code:
            commission_discount = commission_discount.filter(idcomdesconto=code).distinct()

        p = Paginator(commission_discount, rows)

        commission_discount = p.page(int(page)+1).object_list

        self.response['total_size'] = p.count
        
        self.response['columns'] = create_columns_by_list(fields, header_names)

        self.response['commission_discount'] = list(p.page(int(page)+1).object_list.values())

        self.response['message'] = 'Tabela retornada com sucesso'
        
        return self.response

    def list_customer_type_discount(self, page=0, rows=10, term='', isCurrent=None, isExpired=None):
        fields = ['iddescontotipo', 'tipocliente_id', 'dtinicial', 'dtfinal']
        header_names = ['Código', 'Tipo de Cliente', 'Data Inicial', 'Data Final']
        
        today = datetime.now()
        
        customer_type_discount = DescontoTipo.objects.all().order_by('iddescontotipo')
        
        if term:
            customer_type_discount = customer_type_discount.filter(tipocliente_id=term)
        if isCurrent and not isExpired:
            customer_type_discount = customer_type_discount.filter(dtfinal__gte=today)
        elif not isCurrent and isExpired:
            customer_type_discount = customer_type_discount.filter(dtfinal__lte=today)
            
        p = Paginator(customer_type_discount, rows)
        
        customer_type_discount = p.page(int(page)+1).object_list
        
        self.response['total_size'] = p.count
        
        self.response['columns'] = create_columns_by_list(fields, header_names)
        
        self.response['customer_type_discount'] = list(p.page(int(page)+1).object_list.values())
        
        self.response['message'] = 'Tabela retornada com sucesso'
        
        return self.response
    
    def list_volume_discount(self, page=0, rows=10, term='', code=None, isCurrent=None, isExpired=None):
        fields = ['idvolume', 'desvolume', 'datainicial', 'datafinal', 'situacao']
        header_names = ['Código', 'Descrição', 'Data Inicial', 'Data Final', 'Situção']

        today = datetime.now()

        volume_discount = Volume.objects.all().order_by('idvolume')

        if term:
            volume_discount = search_all_fields(Volume, volume_discount, term).distinct()
        if code:
            volume_discount = volume_discount.filter(idvolume=code).distinct()
        if isCurrent and not isExpired:
            volume_discount = volume_discount.filter(datafinal__gte=today)
        elif not isCurrent and isExpired:
            volume_discount = volume_discount.filter(datafinal__lte=today)
            
        p = Paginator(volume_discount, rows)

        volume_discount = p.page(int(page)+1).object_list

        self.response['total_size'] = p.count
        
        self.response['columns'] = create_columns_by_list(fields, header_names)

        self.response['volume_discount'] = list(p.page(int(page)+1).object_list.values())

        self.response['message'] = 'Tabela retornada com sucesso'
        
        return self.response