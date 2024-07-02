from backoffice.models import DashGrafico, DashTipoGrafico
from BO.helpers.database import create_columns_by_list, create_model_by_instance
from django.core.paginator import Paginator
from django.db.models import F


class Graphics:
    def __init__(self):
        self.response = {
            'status': True,
            'message': ''
        }

    def create_grouper(self, infos):
        create_model_by_instance(DashGrafico, infos)
        self.response['message'] = 'Agrupador criado com sucesso'
        return self.response

    def delete_grouper(self, id):
        grouper = DashGrafico.objects.get(iddashgrafico=id)
        grouper.situacao = 'X'
        grouper.save()

        self.response['message'] = 'Agrupador inativado com sucesso'
        return self.response

    def list_groupers(self, page=0, rows=10):
        fields = ['iddashgrafico', 'titulo', 'descricao', 'iddashtipografico_id', 'situacao']
        header_names = ['ID', 'Título', 'Descrição', 'Tipo do Gráfico', 'Situação']

        self.response['columns'] = create_columns_by_list(fields, header_names)

        groupers = DashGrafico.objects.all()
        
        p = Paginator(groupers, rows)
        
        self.response['groupers'] = list(p.page(int(page)+1).object_list.values())
        self.response['total_size'] = p.count                                           
        self.response['message'] = 'Agrupamentos listados com sucesso'

        return self.response
    
    @staticmethod
    def list_groupers_options():
        return list(DashGrafico.objects.filter(situacao='A').values('iddashgrafico').annotate(value=F('iddashgrafico'), label=F('titulo')))
    
    @staticmethod
    def list_type_options():
        return list(DashTipoGrafico.objects.all().values('iddashtipografico').annotate(value=F('iddashtipografico'), label=F('descricao')))
