from backoffice.forms.decorator import validate_form
from BO.order.order import Order
from rest_framework import status
from rest_framework.decorators import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

class OrderTypeSearchView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        try:
            response = Order().list_order_type(page=request.query_params['page'], term=request.query_params['term'], status=request.query_params['status'])
            
            return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
        except:
            return Response({'status': False, 'message': 'Erro interno ao executar função'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
class OrderTypeSingleView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        try:
            response = Order(id=request.query_params['id']).get_single_order_type()
        
            return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
        except:
            return Response({'status': False, 'message': 'Erro interno ao executar função'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    @validate_form('OrderTypeSingleFormPost')
    def post(self, request):
        try:
            response = Order(id=request.data.get('id')).edit_single_order_type(infos=request.data['orderType'])
            
            return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
        except:
            return Response({'status': False, 'message': 'Erro interno ao executar função'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
class OrderBookSearchView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        try:
            response = Order().list_order_book(page=request.query_params['page'], local_sale=request.query_params['localSale'], client=request.query_params['client'], seller=request.query_params['seller'], order_number=request.query_params['orderNumber'], situation=request.query_params['situation'], initial_date=request.query_params['initialDate'], final_date=request.query_params['finalDate'])
            
            return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
        except:
            return Response({'status': False, 'message': 'Erro interno ao executar função'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
class OrderBookSingleView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        try:
            response = Order(id=request.query_params['id']).get_single_order_book()
            
            return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
        except:
            return Response({'status': False, 'message': 'Erro interno ao executar função'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)