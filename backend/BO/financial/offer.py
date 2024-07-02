from backoffice.models import Oferta, OfertaEstrutura, OfertaLocal
from BO.helpers.database import create_columns_by_list, create_model_by_instance, search_all_fields, update_model_with_dict
from datetime import datetime
from django.db.models import F
from django.core.paginator import Paginator
from django.forms.models import model_to_dict


class Offer:
    def __init__(self, id=None):
        self.id = id
        self.response = {
            'status': True,
            'message': ''
        }
        
    def create_single_offer_localsale(self, localsale_id):
        infos = {
            'idoferta': self.id,
            'idlocal': localsale_id
        }
        
        try:
            OfertaLocal.objects.get(**infos)
            
            self.response['status'] = False
            self.response['message'] = 'Cadastro já existente'

            return self.response
        except:
            create_model_by_instance(OfertaLocal, infos)

            self.response['message'] = 'Dados criados com sucesso'
            
            return self.response

    def create_single_offer_structure(self, infos):
        infos['idoferta'] = self.id

        try:
            OfertaEstrutura.objects.get(**infos)

            self.response['status'] = False
            self.response['message'] = 'Cadastro já existente'

            return self.response
        except:
            fields_to_validate = ['desoferta', 'desoferta2', 'qtoferta', 'qtminima', 'qtmaxima']
            for field in fields_to_validate:
                if infos.get(field) is None:
                    infos[field] = 0
            create_model_by_instance(OfertaEstrutura, infos)

            self.response['message'] = 'Dados criados com sucesso'
            
            return self.response

    def delete_single_offer_localsale(self, localsale_id):
        OfertaLocal.objects.filter(idoferta=self.id, idlocal=localsale_id).delete()
        
        self.response['message'] = 'Dados deletados com sucesso'
        
        return self. response

    def delete_single_offer_structure(self, id):
        OfertaEstrutura.objects.get(idofertaestrutura=id).delete()
        
        self.response['message'] = 'Dados deletados com sucesso'
        
        return self. response

    def edit_single_offer(self, infos):
        if self.id:
            offers = Oferta.objects.get(idoferta=self.id)
            update_model_with_dict(offers, infos)

            self.response['message'] = 'Dados atualizados com sucesso'
        else:
            create_model_by_instance(Oferta, infos)

            self.response['message'] = 'Cadastro criado com sucesso'
            
        return self.response

    def get_single_offer(self):
        offer = Oferta.objects.get(idoferta=self.id)

        return model_to_dict(offer)

    def get_single_offer_structure(self, page=0, rows=10):
        fields = ['idproduto_id', 'idfamilia_id', 'idggrupo_id', 'idgrupo_id', 'idsgrupo_id', 'idmarca_id', 'idcategoria_id', 'idfabricante_id', 'idlinha_id', 'qtoferta', 'qtminima', 'qtmaxima', 'desoferta', 'desoferta2']
        header_names = ['Produto', 'Família', 'Grande Grupo', 'Grupo', 'Sub Grupo', 'Marca', 'Categoria', 'Fabricante', 'Linha', 'Qtd. Ofertada', 'Qtd. Mínima', 'Qtd. Mácima', 'Desconto (%)', 'Desconto 2 (%)']

        offers_structure = OfertaEstrutura.objects.filter(idoferta=self.id)

        p = Paginator(offers_structure, rows)

        offers_structure = p.page(int(page)+1).object_list

        self.response['total_size'] = p.count
        
        self.response['columns'] = create_columns_by_list(fields, header_names)

        self.response['offers_structure'] = list(p.page(int(page)+1).object_list.values())

        self.response['offers'] = self.get_single_offer()

        self.response['message'] = 'Informações retornadas com sucesso'
        
        return self.response

    def list_offers(self, page=0, rows=10, term='', isCurrent=None, isExpired=None):
        fields = ['idoferta', 'descricao', 'dtinicial', 'dtfinal']
        header_names = ['Código', 'Descrição da Oferta', 'Data Inicial', 'Data Final']

        today = datetime.now()

        offers = Oferta.objects.all().order_by('idoferta')

        if term:
            offers = search_all_fields(Oferta, offers, term).distinct()
        if isCurrent and not isExpired:
            offers = offers.filter(dtfinal__gte=today)
        elif not isCurrent and isExpired:
            offers = offers.filter(dtfinal__lte=today)

        p = Paginator(offers, rows)

        offers = p.page(int(page)+1).object_list

        self.response['total_size'] = p.count
        
        self.response['columns'] = create_columns_by_list(fields, header_names)

        self.response['offers'] = list(p.page(int(page)+1).object_list.values())

        self.response['message'] = 'Tabela retornada com sucesso'
        
        return self.response
    
    def list_offers_localsale(self, page=0, rows=10):
        fields = ['idoferta_id', 'idlocal_id']
        header_names = ['Oferta', 'Local de Venda']
        
        offers_localsale = OfertaLocal.objects.filter(idoferta=self.id)
        
        p = Paginator(offers_localsale, rows)

        offers_localsale = p.page(int(page)+1).object_list

        self.response['total_size'] = p.count
        
        self.response['columns'] = create_columns_by_list(fields, header_names)

        self.response['offers_localsale'] = list(p.page(int(page)+1).object_list.values())

        self.response['message'] = 'Tabela retornada com sucesso'
        
        return self.response
    
    @staticmethod
    def get_offer_options():
        return list(Oferta.objects.all().values('idoferta').annotate(value=F('idoferta'), label=F('descricao')))