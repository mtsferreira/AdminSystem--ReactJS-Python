from backoffice.models import AcessoPerfil, AcessoPerfilMenu, AcessoPerfilUsuario, Usuario
from backoffice.serializers.user import AcessoPerfilSerializer
from BO.helpers.database import call_stored_procedure, create_columns_by_list, create_model_by_instance, search_all_fields, update_model_with_dict
from django.contrib.auth.models import User as UserModel
from django.core.paginator import Paginator
from django.db.models import CharField, F, Value, Q
from django.db.models.functions import Concat
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken


class AccessProfile:
    def __init__(self, id=None):
        self.id = id
        self.response = {
            'status': True,
            'message': ''
        }

    def delete_relation(self, type=None, relationId=None):
        if type == 'menu':
            AcessoPerfilMenu.objects.get(idperfil=self.id, idmenu=relationId).delete()
        else:
            AcessoPerfilUsuario.objects.get(idperfil=self.id, idusuario=relationId).delete()

        self.response['message'] = 'Vínculo excluido com sucesso'
        return self.response

    def edit_access_profile(self, infos={}):
        if not self.id:
            profile = create_model_by_instance(AcessoPerfil, infos)
            self.response['message'] = 'Perfil criado com sucesso'
        else:
            profile = AcessoPerfil.objects.get(idperfil=self.id)
            update_model_with_dict(profile, infos)

            self.response['message'] = 'Perfil editado com sucesso'

            if 'menus' in infos:
                AcessoPerfilMenu.objects.filter(idperfil=self.id).delete()
                for menu_id in infos['menus']:
                    AcessoPerfilMenu(
                        idperfil_id=self.id,
                        idmenu_id=menu_id
                    ).save()
                    self.response['message'] = 'Menus incluidos com sucesso'

            if 'users' in infos:
                AcessoPerfilUsuario.objects.filter(idperfil=self.id).delete()
                for user_id in infos['users']:
                    AcessoPerfilUsuario(
                        idperfil_id=self.id,
                        idusuario_id=user_id
                    ).save()
                    self.response['message'] = 'Usuarios incluidos com sucesso'
            
        return self.response

    def get_single_access_profile(self):

        profile = AcessoPerfil.objects.get(idperfil=self.id)

        self.response['profile'] = AcessoPerfilSerializer(profile).data
        self.response['message'] = 'Perfil obtido com sucesso'
        return self.response

    def list_access_profile(self, page=0, search_term='', rows=15):

        fields = ['idperfil', 'descricao', 'situacao']
        header_names = ['ID', 'Descrição Grupo', 'Situação']

        customers = AcessoPerfil.objects.all().order_by('idperfil')

        if search_term:
            customers = search_all_fields(AcessoPerfil, customers, search_term)

        p = Paginator(customers, rows)

        self.response['total_size'] = p.count

        self.response['columns'] = create_columns_by_list(fields, header_names)

        self.response['access_group'] = list(p.page(int(page)+1).object_list.values())

        return self.response
    
    def get_access_profile_by_user(self, user_id):

        groups = AcessoPerfilUsuario.objects.filter(idusuario=user_id).values_list('idperfil', flat=True)

        menus = AcessoPerfilMenu.objects.filter(idperfil__in=groups).distinct().values_list('idmenu', flat=True)

        return menus
    

class AuthUser:

    def __init__(self, email=None, password=None, id=None):
        self.id = id
        self.email = email
        self.password = password

    def create_authtoken(self):
        try:
            user = UserModel.objects.get(email=self.email)
        except:
            user = UserModel(username=self.email, email=self.email, password=self.password, id=self.id)
            user.save()
            
        refresh = RefreshToken.for_user(user)

        return refresh
    
    def verify_token(self, token=None):
        try:
            token = AccessToken(token)
            user_id = token.payload['user_id']
            user = UserModel.objects.get(id=user_id)
            user_info = User().load_user_info(user.email, user.password)
            return {
                'status': True,
                'message': 'Sessão autenticada com sucesso',
                'user': user_info
            }
        except:
            return {
                'status': False,
                'message': 'Sessão expirada, realize login novamente'
            }
    

class User:
    def __init__(self, id=None, coderp=None):
        self.id = id
        self.coderp = coderp
        self.response = {
            'status': True,
            'message': ''
        }

    def check_login(self, email, password):
        body = {
            "IDUsuario": None,
            "Email": email,
            "Senha": password,
            "Origem": "O"
        }

        response = call_stored_procedure('PAFV_AutenticacaoUsuario', body, ['Usuario'])
        print(response)

        if response['status']:
            auth_user_token = AuthUser(email=email, password=password, id=response['data']['Usuario']['IDUsuario']).create_authtoken()
            response['token'] = str(auth_user_token.access_token)
            return response

        else:
            return response
        
    def get_user_info(self, user_type=[]):
        user = Usuario.objects.filter(pk=self.id)

        if user_type:
            user.filter(tipousuario__in=user_type)
        
        try:
            return user.first()
        except:
            return {}
        
    def get_user_image(self):
        foto = Usuario.objects.get(idusuario=self.id).foto

        self.response['foto'] = foto.hex() if foto else None

        self.response['message'] = 'Imagem retornada com sucesso.'
        
        return self.response

    def get_user_type(self):
        user = Usuario.objects.get(idusuario=self.id)
        return user.tipousuario
    
    def list_user_by_id_list(self, id_list):
        return Usuario.objects.filter(idusuario__in=id_list)
        
    def load_user_info(self, email, password):
        body = {
            "IDUsuario": None,
            "Email": email,
            "Senha": password,
            "Origem": "O"
        }

        response = call_stored_procedure('PAFV_AutenticacaoUsuario', body, ['Usuario'])

        if response['status']:
            return response['data']['Usuario']

        else:
            return response
         
    
    @staticmethod
    def get_user_id_name_options():
        return list(Usuario.objects.filter(situacao='A').values('idusuario').annotate(value=F('idusuario'), label=Concat('idusuario', Value(' - '), 'nome', output_field=CharField())))
    
    @staticmethod
    def get_user_name_surname_options(search_term=None):
        queryset = Usuario.objects.filter(situacao='A')

        if search_term:
            queryset = queryset.filter(
                Q(nome__icontains=search_term) | Q(sobrenome__icontains=search_term)
            )

        usuarios = queryset.values('idusuario').annotate(
            value=F('idusuario'), 
            label=Concat('nome', Value(' '), 'sobrenome', output_field=CharField())
        )
        return list(usuarios)
    
    @staticmethod
    def get_user_options():
        return list(Usuario.objects.filter(situacao='A').values('idusuario').annotate(value=F('idusuario'), label=F('nome')))