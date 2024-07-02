from backoffice.models import PortalMensagem
from backoffice.serializers.messages import PortalMensagemSerializer
from BO.helpers.database import create_columns_by_list, search_all_fields, update_model_with_dict
from BO.helpers.utils import boolean_to_yes_or_no
from datetime import datetime
from django.core.paginator import Paginator
from django.forms.models import model_to_dict


class Message:
    def __init__(self, id=None):
        self.id = id
        self.response = {
            'status': True,
            'message': ''
        }
        
    
    def edit_single_portal_message(self, infos):
        if self.id:
            portal_message = PortalMensagem.objects.get(idportalmensagem=self.id)
            
        else:
            mensagem = infos.get('mensagem')
            
            if not mensagem:  
                self.response['status'] = False
                self.response['message'] = 'Mensagem inválida'
                return self.response
            else:
                portal_message = PortalMensagem() 

        infos = boolean_to_yes_or_no(infos)
        
        update_model_with_dict(portal_message, infos)

        self.response['message'] = 'Alteração salva com sucesso'
        
        return self.response
    
    def get_single_portal_message(self):
        portal_message = PortalMensagem.objects.get(idportalmensagem=self.id)
        
        self.response['portal_message'] = model_to_dict(portal_message)
        
        self.response['message'] = 'Informações retornadas com sucesso'
        
        return self.response
    
    def list_portal_message(self, page=0, rows=10, term='', messageCode='', isCurrent=None, isExpired=None):
        fields = ['idportalmensagem', 'datainicial', 'datafinal', 'mensagem']
        header_names = ['Código', 'Data Inicial', 'Data Final', 'Menssagem']
        
        today = datetime.now()
        
        portal_message = PortalMensagem.objects.all().order_by('idportalmensagem')
        
        if term:
            portal_message = search_all_fields(PortalMensagem, portal_message, term)
        if messageCode:
            portal_message = portal_message.filter(idportalmensagem=messageCode)
        if isCurrent and not isExpired:
            portal_message = portal_message.filter(datafinal__gte=today)
        elif not isCurrent and isExpired:
            portal_message = portal_message.filter(datafinal__lte=today)
            
        p = Paginator(portal_message, rows)
        
        portal_message = p.page(int(page)+1).object_list
        
        self.response['total_size'] = p.count
        
        self.response['columns'] = create_columns_by_list(fields, header_names)
        
        self.response['portal_message'] = PortalMensagemSerializer(portal_message, many=True).data
        
        self.response['message'] = 'Tabela retornada com sucesso'
        
        return self.response
        
        