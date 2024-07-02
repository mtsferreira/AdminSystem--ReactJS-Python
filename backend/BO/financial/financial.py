from backoffice.models import PoliticaComissao, PrazoFaixa, PrazoFinanceiro
from BO.helpers.database import create_columns_by_list, create_model_by_instance, search_all_fields, update_model_with_dict
from django.core.paginator import Paginator
from django.forms.models import model_to_dict

class Financial:
    def __init__(self, id=None):
        self.id = id
        self.response = {
            'status': True,
            'message': ''
        }

    def create_single_commission_policies(self, infos):
        try:
            create_model_by_instance(PoliticaComissao, infos)

            self.response['message'] = 'Dados criados com sucesso'
            
            return self.response
        
        except Exception as e:
            print("Ocorreu um erro:", e)

            self.response['status'] = False
            self.response['message'] = 'Ocorreu um erro na criação.'

            return self.response

    def delete_range_term(self, id=None):
        term = PrazoFaixa.objects.get(idprazofaixa=id)

        term.situacao = 'X'
        term.save()

        self.response['message'] = 'Prazo inativado com sucesso'
        return self.response
    
    def edit_financial_commission_policies(self, infos):
        infos.pop('idpolcomissao', None)
        
        try:
            comission_policies = PoliticaComissao.objects.get(idpolcomissao=self.id)
            update_model_with_dict(comission_policies, infos)
            self.response['message'] = 'Dados atualizados com sucesso'
            
        except:
            create_model_by_instance(PoliticaComissao, infos)
            self.response['message'] = 'Dados criados com sucesso'

        return self.response

    def edit_financial_term(self, infos={}):
        term = PrazoFinanceiro.objects.get(idprazofinanceiro=self.id)

        update_model_with_dict(term, infos)

        self.response['message'] = 'Prazo editado com sucesso'
        return self.response
    
    def edit_term_range(self, infos={}):
        infos['situacao'] = 'A'
        infos['idprazofinanceiro'] = self.id
        create_model_by_instance(PrazoFaixa, infos)

        self.response['message'] = 'Prazo criado com sucesso'
        return self.response
    
    def get_single_financial_term(self):
        term = PrazoFinanceiro.objects.get(idprazofinanceiro=self.id)

        self.response['term'] = model_to_dict(term)
        self.response['message'] = 'Prazo obtido com sucesso'
        return self.response

    def list_financial_commission_policies(self, page=0, rows=10, term='', status=None, code=None):
        fields = ['idpolcomissao', 'despolitica', 'percomissao', 'percomnovos', 'situacao']
        header_names = ['Código', 'Descrição da Política', 'Comissão Carteira (%)', 'Comissão Novos (%)', 'Situação']

        commission_policies = PoliticaComissao.objects.all().order_by('idpolcomissao')

        if term:
            commission_policies = search_all_fields(PoliticaComissao, commission_policies, term).distinct()
        if status:
            commission_policies = commission_policies.filter(situacao=status).distinct()
        if code:
            commission_policies = commission_policies.filter(idpolcomissao=code)

        p = Paginator(commission_policies, rows)

        commission_policies = p.page(int(page)+1).object_list

        self.response['total_size'] = p.count
        
        self.response['columns'] = create_columns_by_list(fields, header_names)

        self.response['commission_policies'] = list(p.page(int(page)+1).object_list.values())

        self.response['message'] = 'Tabela retornada com sucesso'
        
        return self.response

    def list_financial_terms(self, page=0, rows=10, term='', status=None):
        fields = ['idprazofinanceiro', 'descprazo', 'datainicial', 'datafinal', 'situacao']
        header_names = ['ID', 'Descrição de Variação', 'Data Inicial', 'Data Final', 'Situação']
        
        self.response['columns'] = create_columns_by_list(fields, header_names)
        
        financial_term = PrazoFinanceiro.objects.all().order_by('idprazofinanceiro')
        
        if term:
            financial_term = search_all_fields(PrazoFinanceiro, financial_term, term)
        if status:
            financial_term = financial_term.filter(situacao=status)
            
        p = Paginator(financial_term, rows)
        
        self.response['total_size'] = p.count
        self.response['financial'] = list(p.page(int(page)+1).object_list.values())
        self.response['message'] = 'Pagamentos listados com sucesso'
        
        return self.response
    
    def list_range_terms(self, page=0, rows=10):
        fields = ['prazodias', 'perdesconto', 'peracrescimo', 'vlminimo', 'situacao']
        header_names = ['Prazo', 'Desconto (%)', 'Acrescimo (%)', 'Valor Mínimo', 'Situação']
        
        self.response['columns'] = create_columns_by_list(fields, header_names)
        
        range_term = PrazoFaixa.objects.filter(idprazofinanceiro=self.id).order_by('idprazofinanceiro', 'situacao')
            
        p = Paginator(range_term, rows)
        
        self.response['total_size'] = p.count
        self.response['financial'] = list(p.page(int(page)+1).object_list.values())
        self.response['message'] = 'Pagamentos listados com sucesso'

        return self.response