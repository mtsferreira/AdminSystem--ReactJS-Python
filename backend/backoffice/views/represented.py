from BO.represented.represented import Represented
from rest_framework import status
from rest_framework.decorators import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class RepresentativeSearchView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            response = Represented(id=request.query_params['id']).list_representatives()

            return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
        except:
            return Response({'status': False, 'message': 'Erro interno ao executar função'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class RepresentedComissionPolicyView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            response = Represented(id=request.data['id']).edit_comission_policy(comission_policy_id=request.data['comissionPolicyId'], infos=request.data['comissionPolicy'])

            return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
        except:
            return Response({'status': False, 'message': 'Erro interno ao executar função'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
     

class RepresentedLocalSaleView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            response = Represented(id=request.query_params['id']).get_represented_local_sale(page=request.query_params['page'])

            return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
        except:
            return Response({'status': False, 'message': 'Erro interno ao executar função'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def post(self, request):
        try:
            response = Represented(id=request.data['id']).create_represented_local_sale(local_sale_id=request.data['localSaleId'])

            return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
        except:
            return Response({'status': False, 'message': 'Erro interno ao executar função'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request):
        try:
            response = Represented(id=request.query_params['id']).delete_represented_local_sale(local_sale_id=request.query_params['localSaleId'])

            return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
        except:
            return Response({'status': False, 'message': 'Erro interno ao executar função'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

class RepresentedLocalSaleMainView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            response = Represented(id=request.data['id']).change_main_represented_local_sale(local_sale_id=request.data['localSaleId'])

            return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
        except:
            return Response({'status': False, 'message': 'Erro interno ao executar função'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

class RepresentedSalesRegionView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            response = Represented(id=request.query_params['id']).get_represented_sales_region(page=request.query_params['page'])

            return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
        except:
            return Response({'status': False, 'message': 'Erro interno ao executar função'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def post(self, request):
        try:
            response = Represented(id=request.data['id']).create_represented_sales_region(local_sale_id=request.data['localSaleId'])

            return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
        except:
            return Response({'status': False, 'message': 'Erro interno ao executar função'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request):
        try:
            response = Represented(id=request.query_params['id']).delete_represented_sales_region(local_sale_id=request.query_params['localSaleId'])

            return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
        except:
            return Response({'status': False, 'message': 'Erro interno ao executar função'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class RepresentedSearchView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        try:
            response = Represented().list_represented(page=request.query_params['page'], term=request.query_params['term'], status=request.query_params['status'])

            return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
        except:
            return Response({'status': False, 'message': 'Erro interno ao executar função'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class RepresentedSingleView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            response = Represented(id=request.query_params['id']).get_single_represented()

            return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
        except:
            return Response({'status': False, 'message': 'Erro interno ao executar função'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

class RepresentedStatusView(APIView):
     permission_classes = [IsAuthenticated]

     def post(self, request):
        try:
            response = Represented(id=request.data['id']).edit_status(status=request.data['status'])

            return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
        except:
            return Response({'status': False, 'message': 'Erro interno ao executar função'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
