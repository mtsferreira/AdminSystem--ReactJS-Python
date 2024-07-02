from backoffice.forms.decorator import validate_form
from BO.salesregion.salesregion import SalesRegion
from rest_framework import status
from rest_framework.decorators import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class SalesRegionSearchView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        try:
            response = SalesRegion().list_sale_regions(page=request.query_params['page'], term=request.query_params['term'], regionid=request.query_params['regionid'])
            
            return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
        except:
            return Response({'status': False, 'message': 'Erro interno ao executar função'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def post(self,request):
        try:
            response = SalesRegion().create_sale_Regions(infos=request.data['infos'])
            
            return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
        except:
            return Response({'status': False, 'message': 'Erro interno ao executar função'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
class SalesRegionSingleView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        try:
            response = SalesRegion(id=request.query_params['id']).get_single_sale_regions_uf_city(page=request.query_params['page'])
            
            return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
        except:
            return Response({'status': False, 'message': 'Erro interno ao executar função'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    @validate_form('SalesRegionSingleFormPost')
    def post(self, request):
        try:
            if request.data['type'] == 'updateDescription':
                response = SalesRegion(id=request.data['id']).edit_single_sale_regions(infos=request.data['salesRegion'])
                
            elif request.data['type'] == 'addUfCity':
                response = SalesRegion(id=request.data['id']).create_single_sale_regions_uf_city(infos=request.data['infos'])
        
            return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
        except:
            return Response({'status': False, 'message': 'Erro interno ao executar função'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def delete(self, request):
        try:
            response = SalesRegion().delete_single_sale_regions_uf_city(id=request.query_params['id'])
            
            return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
        except:
            return Response({'status': False, 'message': 'Erro interno ao executar função'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class SalesRegionSellersView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        try:
            response = SalesRegion(id=request.query_params['id']).get_single_sale_regions_seller(page=request.query_params['page'])
            
            return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
        except:
            return Response({'status': False, 'message': 'Erro interno ao executar função'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class SalesRegionRepresentedView(APIView):
     permission_classes = [IsAuthenticated]
     
     def get(self, request):
        try:
            response = SalesRegion(id=request.query_params['id']).get_single_sale_regions_represented(page=request.query_params['page'])
                
            return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
        except:
            return Response({'status': False, 'message': 'Erro interno ao executar função'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)