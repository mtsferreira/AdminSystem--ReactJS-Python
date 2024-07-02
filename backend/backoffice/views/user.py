from BO.user.user import AccessProfile, AuthUser, User
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.decorators import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken


class AccessProfileView(APIView):

    def get(self, request):
        response = AccessProfile(id=request.query_params['id']).get_single_access_profile()
        return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def post(self, request):
        response = AccessProfile(id=request.data.get('id')).edit_access_profile(infos=request.data['profile'])
        return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def delete(self, request):
        response = AccessProfile(id=request.query_params['id']).delete_relation(type=request.query_params['type'], relationId=request.query_params['relationId'])
        return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)


class AccessProfileSearchView(APIView):

    def get(self, request):
        response = AccessProfile().list_access_profile(page=request.query_params['page'], search_term=request.query_params.get('term'))
        return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
    

class LoginView(APIView):

    def get(self, request):
        try:
            response = User().check_login(request.query_params['email'], request.query_params['password'])
            return Response(response, status=response['http_status'])
        except:
            return Response({'status': False, 'message': 'Erro interno ao executar função'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            token = request.data['token']
            token = RefreshToken(token)
            token.blacklist()
            return Response({'status': True, 'message': 'Logout Realizado com Sucesso'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'status': False, 'message': 'Erro ao Realizar Logout'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class UserImageView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            response = User(id=request.query_params['id']).get_user_image()
            return Response(response, content_type='application/octet-stream')
        except:
            return Response({'status': False, 'message': 'Erro ao Obter Imagem'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class UserSearchView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            response = User.get_user_name_surname_options(search_term=request.query_params.get('term'))
            return Response({'status': True, 'message': 'Usuários listados com sucesso', 'userList': response}, status=status.HTTP_200_OK)
        except:
            return Response({'status': False, 'message': 'Erro ao listar usuários'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class VerifyView(APIView):

    def get(self, request):
        try:
            response = AuthUser().verify_token(request.query_params['token'])
            
            return Response(response, status=(status.HTTP_200_OK if response['status'] else status.HTTP_401_UNAUTHORIZED))
        except:
            return Response({'status': False, 'message': 'Erro interno ao executar função'}, status=(status.HTTP_500_INTERNAL_SERVER_ERROR))
