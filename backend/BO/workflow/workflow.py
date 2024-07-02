from backoffice.models import PedidoWF, WorkFlow
from backoffice.serializers.workflow import WorkFlowSerializer
from BO.helpers.database import create_columns_by_list, create_model_by_instance, update_model_with_dict, search_all_fields 
from django.core.paginator import Paginator
from django.db.models import Case, When, Value, CharField, F

class Workflow:
    def __init__(self, id=None):
        self.id = id
        self.response = {
            'status': True,
            'message': ''
        }

    def create_workflow(self, infos):
        create_model_by_instance(WorkFlow, infos)
        
        self.response['message'] = 'Workflow criado com sucesso'  
        
        return self.response    
        
    def delete_workflow(self):
        WorkFlow.objects.get(idworkflow=self.id).delete()

        self.response['message'] = 'Dados deletados com sucesso'

        return self.response
    
    def edit_order_workflow(self, workflow_id=None):
        if workflow_id == '9999':
            workflow_id = None
        order = PedidoWF.objects.get(idpedido=self.id)
        order.idworkflow_id = workflow_id
        order.save()

        self.response['message'] = 'Workflow alterado com sucesso'
        return self.response

    def edit_single_workflow(self, infos):
        workflow = WorkFlow.objects.get(idworkflow=self.id)
        update_model_with_dict(workflow, infos)
        
        self.response['message'] = 'Dados atualizados com sucesso'
        
        return self.response
    
    def get_orders(self, start_date=None, end_date=None, local_sale_id=None):

        queryset = PedidoWF.objects.select_related('idpedido', 'idpedido__pedidoresumo', 'idpedido__idlocal', 'idpedido__idcliente').annotate(
            nrpedido=F('idpedido__nrpedido'),
            dtorcamento=F('idpedido__dtorcamento'),
            vlorcamento=F('idpedido__pedidoresumo__vlorcamento'),
            razao=F('idpedido__idcliente__razao'),
            contato=F('idpedido__contato'),
            idlocalvenda=F('idpedido__idlocal__idlocalvenda'),
            telefone=Case(
                When(idpedido__telcelular__exact='', then='idpedido__whats'),
                default='idpedido__telcelular',
                output_field=CharField()
            )
        )
        # ).filter(idworkflow__isnull=False)

        if start_date and end_date:
            queryset = queryset.filter(idpedido__dtorcamento__range=[start_date, end_date])

        if local_sale_id:
            queryset = queryset.filter(idpedido__idlocal_id=local_sale_id)

        self.response['order'] = queryset.values()
        self.response['message'] = 'Pedidos listados com sucesso'

        return self.response

    def get_workflow_list(self, page=0, rows=10, no_pagination=False):
        fields = ['idworkflow', 'desworkflow', 'idlistacor_id', 'ordem', 'situacao']
        header_names = ['Código', 'Descrição', 'Cor', 'Ordem', 'Situação']
        
        self.response['columns'] = create_columns_by_list(fields, header_names)
        
        workflow = WorkFlow.objects.all().order_by('ordem')

        if no_pagination:

            self.response['workflow'] = WorkFlowSerializer(workflow, many=True).data
            return self.response
        
        p = Paginator(workflow, rows)
        
        self.response['total_size'] = p.count
        
        workflow = p.page(int(page)+1).object_list
        
        self.response['workflow'] = list(p.page(int(page)+1).object_list.values())
        
        self.response['message'] = 'Tabela retornada com sucesso'
        
        return self.response
        
        