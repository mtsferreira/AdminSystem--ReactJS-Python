from backoffice.models import Pagamento
from BO.helpers.database import create_columns_by_list, create_model_by_instance, search_all_fields, update_model_with_dict
from django.core.paginator import Paginator

class Payment:
    def __init__(self, id=None):
        self.id = id
        self.response = {
            'status': True,
            'message': ''
        }

    def create_payment(self, infos):
        try:
            create_model_by_instance(Pagamento, infos)

            self.response['message'] = 'Dados criados com sucesso'
            
            return self.response
        
        except Exception as e:
            print("Ocorreu um erro:", e)

            self.response['status'] = False
            self.response['message'] = 'Ocorreu um erro na criação.'

            return self.response

    def delete_payment(self): 
        try:
            Pagamento.objects.get(idpagamento=self.id).delete()
            
            self.response['message'] = 'Pagamento excluido com sucesso.'
            
            return self.response
        
        except:
            self.response['status'] = False
            self.response['message'] = 'Erro ao realizar exclusão.'
            
            return self.response

    def edit_payment(self, infos={}):
        try:
            payment = Pagamento.objects.get(idpagamento=self.id)
            update_model_with_dict(payment, infos)
            self.response['message'] = 'Pagamento atualizado com sucesso'
            
        except:
            create_model_by_instance(Pagamento, infos)
            self.response['message'] = 'Pagamento criado com sucesso'

        return self.response

    def list_payments(self, page=0, rows=10, term='', status=None):
        fields = ['coderp', 'descpagamento', 'prazodias', 'qparcela', 'situacao']
        header_names = ['Código ERP', 'Descrição', 'Prazo Médio', 'Qtd. Parcelas', 'Situação']
        
        self.response['columns'] = create_columns_by_list(fields, header_names)
        
        payment = Pagamento.objects.all().order_by('idpagamento')
        
        if term:
            payment = search_all_fields(Pagamento, payment, term)
        if status:
            payment = payment.filter(situacao=status)
            
        p = Paginator(payment, rows)
        
        self.response['total_size'] = p.count
        self.response['payment'] = list(p.page(int(page)+1).object_list.values())
        self.response['message'] = 'Pagamentos listados com sucesso'
        
        return self.response

    