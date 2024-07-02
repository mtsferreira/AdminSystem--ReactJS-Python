from backoffice.forms.decorator import validate_form
from BO.customer.customer import Customer
from rest_framework import status
from rest_framework.decorators import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class CustomerAddressView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            response = Customer(id=request.query_params['id']).get_address(page=request.query_params['page'])

            return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
        except:
            return Response({'status': False, 'message': 'Erro interno ao executar função'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def delete(self, request):
        try:
            response = Customer(id=request.query_params['id']).delete_address(contact_id=request.query_params['addressId'])
            
            return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
        except:
            return Response({'status': False, 'message': 'Erro interno ao executar função'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

class CustomerContactView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            response = Customer(id=request.query_params['id']).get_contacts(page=request.query_params['page'])

            return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
        except:
            return Response({'status': False, 'message': 'Erro interno ao executar função'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def post(self, request):
        try:
            response = Customer(id=request.data['id']).edit_contact(contact_id=request.data['contact']['idcontato'], infos=request.data['contact'])

            return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
        except:
            return Response({'status': False, 'message': 'Erro interno ao executar função'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def delete(self, request):
        try:
            response = Customer(id=request.query_params['id']).delete_contact(contact_id=request.query_params['contactId'])
            
            return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
        except:
            return Response({'status': False, 'message': 'Erro interno ao executar função'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class CustomerProfileView(APIView):
    permission_classes = [IsAuthenticated]

    @validate_form('CustomerProfileFormPost')
    def post(self, request):
        try:
            response = Customer(id=request.data['id']).edit_customer_profile(infos=request.data['profile'])
            
            return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
        except:
            return Response({'status': False, 'message': 'Erro interno ao executar função'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class CustomerInfoView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            response = Customer(id=request.query_params['id']).get_infos()

            return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
        except:
            return Response({'status': False, 'message': 'Erro interno ao executar função'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class CustomerSearchView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            response = Customer().list_customer(page=request.query_params['page'], search_term=request.query_params['term'])

            return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
        except:
            return Response({'status': False, 'message': 'Erro interno ao executar função'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

class CustomerSellerView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            response = Customer(id=request.query_params['id']).get_seller(page=request.query_params['page'])

            return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
        except:
            return Response({'status': False, 'message': 'Erro interno ao executar função'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class CustomerSellerSingleView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            response = Customer(id=request.query_params['id']).get_single_seller(customer_seller_id=request.query_params['customerSellerId'])

            return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
        except:
            return Response({'status': False, 'message': 'Erro interno ao executar função'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    @validate_form('CustomerSellerSingleFormPost')
    def post(self, request):
        try:
            response = Customer(id=request.data['id']).edit_single_seller(customer_seller_id=request.data.get('customerSellerId'), user_id=request.data.get('userId'), infos=request.data['customerSeller'])

            return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
        except:
            return Response({'status': False, 'message': 'Erro interno ao executar função'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def delete(self, request):
        try:
            response = Customer(id=request.query_params['id']).delete_single_seller(customer_seller_id=request.query_params['customerSellerId'])

            return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
        except:
            return Response({'status': False, 'message': 'Erro interno ao executar função'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)