from BO.utilities.utilities import Utilities
from BO.layout.general import City
from rest_framework import status
from rest_framework.decorators import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

class ListOptionsView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        try:
            response = Utilities().list_genereic_options(option_list=request.query_params['optionList'])
            
            return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
        except:
            return Response({'status': False, 'message': 'Erro interno ao executar função'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class ListCityOptionsView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        try:
            response = City(uf=request.query_params['uf']).get_city_options_by_uf()
            
            return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
        except:
            return Response({'status': False, 'message': 'Erro interno ao executar função'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)