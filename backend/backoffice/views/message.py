from backoffice.forms.decorator import validate_form
from BO.message.message import Message 
from rest_framework import status
from rest_framework.decorators import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class MessagePortalView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        try:
            response = Message().list_portal_message(page=request.query_params['page'], term=request.query_params['term'], messageCode=request.query_params['messageCode'], isCurrent=request.query_params['isCurrent'], isExpired=request.query_params['isExpired'])
            
            return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
        except:
            return Response({'status': False, 'message': 'Erro interno ao executar função'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
class MessagePortalSingleView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        try:
            response = Message(id=request.query_params['id']).get_single_portal_message()
            
            return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
        except:
            return Response({'status': False, 'message': 'Erro interno ao executar função'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    @validate_form('MessagePortalSingleFormPost')
    def post(self, request):
        try:
            response = Message(id=request.data.get('id')).edit_single_portal_message(infos=request.data['portalMessage'])
            
            return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
        except:
            return Response({'status': False, 'message': 'Erro interno ao executar função'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)