from backoffice.forms.decorator import validate_form
from BO.layout.graphics import Graphics
from BO.layout.menu import Menu
from rest_framework import status
from rest_framework.decorators import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class GraphicsGrouperView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        response = Graphics().list_groupers(page=request.query_params['page'])

        return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)

    @validate_form('GraphicsGrouperFormPost')
    def post(self, request):
        response = Graphics().create_grouper(infos=request.data['grouper'])

        return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request):
        response = Graphics().delete_grouper(id=request.query_params['id'])
        
        return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
    

class MenuListView(APIView):

    def get(self, request):
        try:
            response = Menu.list_all_modules(user_id=request.query_params.get('userId'))

            return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
        except:
            return Response({'status': False, 'message': 'Erro interno ao executar função'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class MenuFavoriteView(APIView):

    def get(self, request):
        try:
            response = Menu(menu_id=request.query_params['menuId']).get_favorite(user_id=request.query_params['userId'])

            return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
        except:
            return Response({'status': False, 'message': 'Erro interno ao executar função'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def post(self, request):
        try:
            response = Menu(menu_id=request.data['menuId']).save_favorite(user_id=request.data['userId'])

            return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
        except:
            return Response({'status': False, 'message': 'Erro interno ao executar função'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request):
        try:
            response = Menu(menu_id=request.query_params['menuId']).delete_favorite(user_id=request.query_params['userId'])

            return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
        except:
            return Response({'status': False, 'message': 'Erro interno ao executar função'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class MenuFavoriteListView(APIView):

    def get(self, request):
        try:
            response = Menu.list_all_favorites(user_id=request.query_params['userId'])

            return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
        except:
            return Response({'status': False, 'message': 'Erro interno ao executar função'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)