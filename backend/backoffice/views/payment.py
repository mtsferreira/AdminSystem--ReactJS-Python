from backoffice.forms.decorator import validate_form
from BO.financial.payment import Payment
from rest_framework import status
from rest_framework.decorators import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

class PaymentView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        try:
            response = Payment().list_payments(page=request.query_params['page'], term=request.query_params['term'], status=request.query_params['status'])
            return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
        except:
            return Response({'status': False, 'message': 'Erro interno ao executar função'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def post(self, request):
        try:
            response = Payment().create_payment(infos=request.data['infos'])
            return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
        except:
            return Response({'status': False, 'message': 'Erro interno ao executar função'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    
class PaymentSingleView(APIView):
    permission_classes = [IsAuthenticated]
    
    @validate_form('PaymentSingleFormPost')
    def post(self, request):
        response = Payment(id=request.data.get('id')).edit_payment(infos=request.data['infos'])
        return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def delete(self, request):
        response = Payment(id=request.query_params['id']).delete_payment()
        return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)