from backoffice.forms.decorator import validate_form
from BO.shippingcif.shippingcif import ShippingCif
from rest_framework import status
from rest_framework.decorators import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

class ShippingCifSearchView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            response = ShippingCif().list_shipping_cif(page=request.query_params['page'], term=request.query_params['term'], status=request.query_params['status'], isCurrent=request.query_params['isCurrent'], isExpired=request.query_params['isExpired'])

            return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
        except:
            return Response({'status': False, 'message': 'Erro interno ao executar função'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
class ShippingCifSingleView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            response = ShippingCif(id=request.query_params['id']).get_single_shipping_cif_location(page=request.query_params['page'])

            return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
        except:
            return Response({'status': False, 'message': 'Erro interno ao executar função'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    @validate_form('ShippingCifSingleFormPost')
    def post(self, request):
        try:
            if request.data['type'] == 'updateOrCreate':
                response = ShippingCif(id=request.data.get('id')).edit_single_shipping_cif(infos=request.data['shippingCif'])

            elif request.data['type'] == 'addLocation':
                response = ShippingCif(id=request.data.get('id')).create_single_shipping_cif_location(infos=request.data['shippingCifLocation'])

            return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
        except:
            return Response({'status': False, 'message': 'Erro interno ao executar função'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def delete(self, request):
        try:
            response = ShippingCif().delete_single_shipping_cif_location(id=request.query_params['id'])

            return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
        except:
            return Response({'status': False, 'message': 'Erro interno ao executar função'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)