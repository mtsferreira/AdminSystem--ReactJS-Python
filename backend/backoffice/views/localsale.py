from backoffice.forms.decorator import validate_form
from BO.localsale.localsale import Company, LocalSale
from rest_framework import status
from rest_framework.decorators import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class CompanyView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        response = Company().get_company(cnpj=request.query_params.get('cnpj'))

        return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    @validate_form('CompanyFormPost')
    def post(self, request):
        response = Company(id=request.data['companyId']).edit_company(infos=request.data['company'])

        return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)

class LocalSaleSearchView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        try:
            response = LocalSale().list_local_sale(page=request.query_params['page'], term=request.query_params['term'], status=request.query_params['status'])
            
            return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
        except:
            return Response({'status': False, 'message': 'Erro interno ao executar função'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class LocalSaleSingleView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        try:
            response = LocalSale(id=request.query_params['id']).get_single_local_sale()
            
            return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
        except:
            return Response({'status': False, 'message': 'Erro interno ao executar função'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    @validate_form('LocalSaleSingleFormPost')
    def post(self, request): 
        try:
            response = LocalSale(id=request.data.get('id')).edit_single_local_sale(infos=request.data['localSale'])
            
            return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
        except:
            return Response({'status': False, 'message': 'Erro interno ao executar função'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class LocalSaleConfigSingleView(APIView):
    permission_classes = [IsAuthenticated]
    
    @validate_form('LocalSaleConfigSingleFormPost')
    def post(self, request):
        try:
            response = LocalSale(id=request.data['id']).edit_config_single_local_sale(infos=request.data['config'])
            
            return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
        except:
            return Response({'status': False, 'message': 'Erro interno ao executar função'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class LocalSaleEmailView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        try:
            response = LocalSale(id=request.query_params['id']).get_local_sale_email(page=request.query_params['page'])
            
            return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
        except:
            return Response({'status': False, 'message': 'Erro interno ao executar função'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    @validate_form('LocalSaleEmailSingleFormPost')
    def post(self, request):
        try:
            response = LocalSale(id=request.data['localSaleId']).edit_local_sale_email(infos=request.data['localSaleEmail'])
            
            return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
        except:
            return Response({'status': False, 'message': 'Erro interno ao executar função'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def delete(self, request):
        try:
            response = LocalSale(id=request.query_params['id']).delete_local_sale_email()
            
            return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
        except:
            return Response({'status': False, 'message': 'Erro interno ao executar função'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)