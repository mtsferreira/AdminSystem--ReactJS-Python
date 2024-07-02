from backoffice.models import Cascata, Cliente, ClienteContato, ClienteEndereco, ClientePerfil, ClienteTipo, ClienteVendedor, ClienteVisita, Transportador, Volume
from backoffice.models.rawquery.customer import CUSTOMER_SELLER_QUERY
from backoffice.serializers.customer import ClienteSerializer
from BO.helpers.database import call_raw_query, create_columns_by_list, create_columns_by_model, create_model_by_instance, search_all_fields, update_model_with_dict
from BO.helpers.utils import boolean_to_yes_or_no
from BO.layout.general import GrupoEconomico, Rede, OrderType, TabGeral, TipoFrete
from BO.price.price import Price
from BO.salesregion.salesregion import SalesRegion
from BO.user.user import User
from django.core.paginator import Paginator
from django.db.models import CharField, F, Value
from django.db.models.functions import Concat
from django.forms.models import model_to_dict


class Customer:
    def __init__(self, id=None):
        self.id = id
        self.response = {
            'status': True,
            'message': ''
        }

    def delete_address(self, address_id):
        response = {
            'status': True,
            'message': 'Endereço excluído com sucesso'
        }

        try:
            contact = ClienteEndereco.objects.get(idendereco=address_id)
            contact.situacao = 'X'
            contact.save()
        
        except:
            response['status'] = False
            response['message'] = 'Erro ao excluir o endereço'
        
        return response

    def delete_contact(self, contact_id):
        response = {
            'status': True,
            'message': 'Contato excluído com sucesso'
        }

        try:
            contact = ClienteContato.objects.get(idcontato=contact_id)
            contact.situacao = 'X'
            contact.save()
        
        except:
            response['status'] = False
            response['message'] = 'Erro ao excluir o contato'
        
        return response
    
    def delete_single_seller(self, customer_seller_id):
        response = {
            'status': True,
            'message': 'Vinculo com vendedor excluído com sucesso'
        }

        try:
            ClienteVisita.objects.get(idclientevendedor=customer_seller_id).delete()
            ClienteVendedor.objects.get(idclientevendedor=customer_seller_id).delete()
        except:
            response['status'] = False
            response['message'] = 'Vínculo não encontrado no sistema'

        return response

    def edit_contact(self, contact_id=None, infos=None):
        response = {
            'status': True,
            'message': 'Contato editado com sucesso'
        }

        infos.pop('idcontato', None)
        infos['idcliente'] = self.id

        infos['idcliente_id'] = infos.pop('idcliente')
        infos['datanascimento'] = infos['datanascimento'][0:10]

        try:
            contact = ClienteContato.objects.get(idcontato=contact_id)
            try:
                update_model_with_dict(contact, infos)
            except:
                response['status'] = False
                response['message'] = 'Erro ao editar o contato'
        except:
            try:
                contact = ClienteContato(**infos)
                contact.save()
            except:
                response['status'] = False
                response['message'] = 'Erro ao criar o contato'

        return response
    
    def edit_customer_profile(self, infos={}):
        profile = ClientePerfil.objects.get(idcliente=self.id)
        
        boolean_to_yes_or_no(infos)
        
        update_model_with_dict(profile, infos)

        self.response['message'] = 'Perfil político atualizado com sucesso'
        
        return self.response
    
    def edit_single_seller(self, customer_seller_id=None, user_id=None, infos=None):
        response = {
            'status': True,
            'message': 'Contato editado com sucesso'
        }

        infos['visit'] = boolean_to_yes_or_no(dict=infos['visit'])

        if not customer_seller_id:
            user_type = User(id=user_id).get_user_type()
            customer_seller = ClienteVendedor(idcliente_id=self.id, idusuario=user_id, tipousuario='V' if user_type == 1 else 'R')
            try:
                customer_seller.save()
            except:
                response['status'] = False
                response['message'] = 'Registro ja existente'
                
                return response

            
            infos['visit']['idclientevendedor_id'] = customer_seller.idclientevendedor
            create_model_by_instance(ClienteVisita, infos['visit'])
            
        else:
            customer_seller_visit = ClienteVisita.objects.get(idclientevendedor_id=customer_seller_id)
            customer_seller = ClienteVendedor.objects.get(idclientevendedor=customer_seller_id)

            update_model_with_dict(customer_seller_visit, infos['visit'])
        
        customer_seller.idcascata_id = infos['idcascata']
        customer_seller.idvolume_id = infos['idvolume']
        customer_seller.save()

        return response

    def get_address(self, page=0, rows=10):
        response = {
            'status': True,
            'message': 'Informações obtidas com sucesso',
            'address': None,
            'columns': [],
            'total_size': 0
        }

        fields = ['idendereco', 'cep', 'logradouro', 'numero', 'complemento', 'bairro', 'codibge', 'tipoendereco', 'situacao']
        header_names = ['ID Endereço', 'CEP', 'Logradouro', 'Número', 'Complemento', 'Bairro', 'Código IBGE', 'Tipo Endereço', 'Situação']

        response['columns'] = create_columns_by_model(ClienteEndereco(), fields, header_names)

        address = ClienteEndereco.objects.filter(idcliente=self.id).order_by('idendereco')

        p = Paginator(address, rows)

        response['total_size'] = p.count
        response['address'] = list(p.page(int(page)+1).object_list.values())

        return response
    
    def get_contacts(self, page=0, rows=10):
        response = {
            'status': True,
            'message': 'Informações obtidas com sucesso',
            'contact': None,
            'columns': [],
            'total_size': 0
        }

        fields = ['idcontato', 'nome', 'datanascimento', 'funcao', 'departamento', 'telfixo', 'telcelular', 'numwhats', 'emailcorp', 'emailpessoal', 'situacao']
        header_names = ['ID Contato', 'Nome', 'Data Nascimento', 'Função', 'Departamento', 'Telefone Fixo', 'Telefone Celular', 'Número Whatsapp', 'Email Corporativo', 'Email Pessoal', 'Situação']

        response['columns'] = create_columns_by_model(ClienteContato(), fields, header_names)

        contact = ClienteContato.objects.filter(idcliente=self.id).order_by('idcontato')

        p = Paginator(contact, rows)

        response['total_size'] = p.count
        response['contact'] = list(p.page(int(page)+1).object_list.values(*fields))

        return response

    def get_infos(self):
        response = {
            'status': True,
            'message': 'Informações obtidas com sucesso',
            'customer': None,
            'options_destination': TabGeral.get_destination_options(),
            'options_customer_type': Customer.get_customer_type_options(),
            'options_economic_group': GrupoEconomico.get_economic_group_options(),
            'options_legal_nature': TabGeral.get_legal_nature_options(),
            'options_fiscal_status': TabGeral.get_fiscal_status_options(),
            'options_network': Rede.get_network_options(),
            'options_order_type': OrderType.get_order_type_options(),
            'options_rules_price': Price.get_price_rules_options(),
            'options_shipping_type': TipoFrete.get_shipping_type_options(),
            'options_shipping': Customer.get_shipping_options(),
            'options_selling_area': SalesRegion.get_sale_regions_options(),
            'comercial_discount_options': Customer.get_comercial_discount_options(),
            'volume_discount_options': Customer.get_volume_discount_options(),
            'user_options': User.get_user_options()
        }

        customer = Cliente.objects.get(idcliente=self.id)
        serializer = ClienteSerializer(customer)

        response['customer'] = serializer.data

        return response
    
    def get_seller(self, page=0, rows=10):
        response = {
            'status': True,
            'message': 'Informações obtidas com sucesso',
            'seller': None,
            'columns': [],
            'total_size': 0
        }

        fields = ['idclientevendedor', 'coderp', 'nome', 'tipousuario', 'equipe', 'descontocomercial', 'descontovolume']
        header_names = ['ID', 'Código ERP', 'Nome', 'Tipo Usuário', 'Equipe', 'Desconto Comercial', 'Desconto Volume']

        response['columns'] = create_columns_by_list(fields, header_names)

        seller = call_raw_query(CUSTOMER_SELLER_QUERY, [self.id])

        p = Paginator(seller, rows)

        response['total_size'] = p.count
        current_page = p.get_page(page)
        response['seller'] = [dict(row) for row in current_page]

        return response
    
    def get_single_seller(self, customer_seller_id=None):
        response = {
            'status': True,
            'message': 'Cliente listados com sucesso',
            'customer_seller': None,
        }

        customer_seller = model_to_dict(ClienteVendedor.objects.get(idclientevendedor=customer_seller_id))

        try:
            customer_seller_visit = ClienteVisita.objects.get(idclientevendedor_id=customer_seller_id)
        except:
            customer_seller_visit = ClienteVisita(
                idclientevendedor_id=customer_seller_id,
                seg='N',
                ter='N',
                qua='N',
                qui='N',
                sex='N',
                sab='N',
                dom='N',
                hora1=None,
                hora2=None
            )
            customer_seller_visit.save()

        customer_seller['visit'] = model_to_dict(customer_seller_visit)
        response['customer_seller'] = customer_seller
        return response

    def list_customer(self, page=0, rows=10, search_term=None):
        response = {
            'status': True,
            'message': 'Clientes listados com sucesso',
            'columns': [],
            'customers': [],
            'total_size': 0
        }

        fields = ['idcliente', 'coderp', 'cnpjcpf', 'razao', 'fantasia', 'cidade', 'ufcliente', 'situacao']
        header_names = ['ID Cliente', 'Código ERP', 'CNPJ/CPF', 'Razão Social', 'Nome Fantasia', 'Cidade', 'UF', 'Situação']

        response['columns'] = create_columns_by_model(Cliente(), fields, header_names)

        customers = Cliente.objects.all().order_by('idcliente')

        if search_term:
            customers = search_all_fields(Cliente, customers, search_term)

        p = Paginator(customers, rows)

        response['total_size'] = p.count
        response['customers'] = list(p.page(int(page)+1).object_list.values())

        return response
    
    @staticmethod
    def get_comercial_discount_options():
        return list(Cascata.objects.filter(situacao='A').values('idcascata').annotate(value=F('idcascata'), label=F('descascata')))

    @staticmethod
    def get_customer_by_corporate_reason_options():
        return list(Cliente.objects.filter(situacao='A').values('idcliente').annotate(value=F('idcliente'), label=F('razao')))
    
    @staticmethod
    def get_customer_by_coderp_fantasy_options():
        return list(Cliente.objects.filter(situacao='A').values('idcliente').annotate(value=F('idcliente'), label=Concat('coderp', Value(' - '), 'fantasia', output_field=CharField())))
    
    @staticmethod
    def get_customer_type_options():
        return list(ClienteTipo.objects.filter(situacao='A').values('idclientetipo').annotate(value=F('idclientetipo'), label=F('descricao')))
    
    @staticmethod
    def get_shipping_options():
        return list(Transportador.objects.filter(situacao='A').values('idtransportador').annotate(value=F('idtransportador'), label=F('razao')))
    
    @staticmethod
    def get_volume_discount_options():
        return list(Volume.objects.filter(situacao='A').values('idvolume').annotate(value=F('idvolume'), label=F('desvolume')))