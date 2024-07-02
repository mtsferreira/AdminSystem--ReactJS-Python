from backoffice.forms.decorator import validate_form
from BO.discount.discount import Discount
from rest_framework import status
from rest_framework.decorators import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class CustomerTypeDiscountSearchView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            response = Discount().list_customer_type_discount(page=request.query_params['page'], term=request.query_params['search'], isCurrent=request.query_params['isCurrent'], isExpired=request.query_params['isExpired'])

            return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
        except:
            return Response({'status': False, 'message': 'Erro interno ao executar função'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def delete(self, request):
        try:
            response = Discount(id=request.query_params['id']).delete_customer_type_discount()

            return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
        except:
            return Response({'status': False, 'message': 'Erro interno ao executar função'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

class CustomerTypeDiscountSingleView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            response = Discount(id=request.query_params['id']).get_single_customer_type_discount_structure(page=request.query_params['page'])

            return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
        except:
            return Response({'status': False, 'message': 'Erro interno ao executar função'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def post(self, request):
        try:
            if request.data['type'] == 'updateOrCreate':
                response = Discount(id=request.data.get('id')).edit_single_customer_type_discount(infos=request.data['customerTypeDiscount'])

            elif request.data['type'] == 'addStructure':
                response = Discount(id=request.data.get('id')).create_single_customer_type_discount_structure(infos=request.data['customerTypeDiscountStructure'])

            return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
        except:
            return Response({'status': False, 'message': 'Erro interno ao executar função'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def delete(self, request):
        try:
            response = Discount().delete_customer_type_discount_structure(id=request.query_params['id'])

            return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
        except:
            return Response({'status': False, 'message': 'Erro interno ao executar função'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

class VolumeDiscountSearchView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            response = Discount().list_volume_discount(page=request.query_params['page'], term=request.query_params['term'], code=request.query_params['code'], isCurrent=request.query_params['isCurrent'], isExpired=request.query_params['isExpired'])

            return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
        except:
            return Response({'status': False, 'message': 'Erro interno ao executar função'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

class VolumeDiscountSingleView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            response = Discount(id=request.query_params['id']).get_single_volume_range_discount(page=request.query_params['page'])

            return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
        except:
            return Response({'status': False, 'message': 'Erro interno ao executar função'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        try:
            if request.data['type'] == 'updateOrCreate':
                response = Discount(id=request.data.get('id')).edit_single_volume_discount(infos=request.data['volumeDiscount'])

            elif request.data['type'] == 'addRange':
                    response = Discount(id=request.data.get('id')).create_single_volume_range_discount(infos=request.data['volumeRangeDiscount'])
            
            return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
        except:
            return Response({'status': False, 'message': 'Erro interno ao executar função'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def delete(self, request):
        try:
            response = Discount().delete_volume_range_discount(id=request.query_params['id'])

            return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
        except:
            return Response({'status': False, 'message': 'Erro interno ao executar função'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class CommissionDiscountSearchView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            response = Discount().list_commission_discount(page=request.query_params['page'], term=request.query_params['term'], code=request.query_params['code'])

            return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
        except:
            return Response({'status': False, 'message': 'Erro interno ao executar função'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

class CommissionDiscountSingleView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            response = Discount(id=request.query_params['id']).get_single_commission_discount_range(page=request.query_params['page'])

            return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
        except:
            return Response({'status': False, 'message': 'Erro interno ao executar função'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def post(self, request):
        try:
            if request.data['type'] == 'updateOrCreate':
                response = Discount(id=request.data.get('id')).edit_single_commission_discount(infos=request.data['commissionDiscount'])

            elif request.data['type'] == 'addRange':
                    response = Discount(id=request.data.get('id')).create_single_commission_discount_range(infos=request.data['commissionDiscountRange'])
            
            return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
        except:
            return Response({'status': False, 'message': 'Erro interno ao executar função'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def delete(self, request):
        try:
            response = Discount().delete_commission_discount_range(id=request.query_params['id'])

            return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
        except:
            return Response({'status': False, 'message': 'Erro interno ao executar função'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

class CascadeDiscountTermView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        response = Discount().list_cascade_term_discount(page=request.query_params['page'])

        return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    @validate_form('CascadeDiscountTermFormPost')
    def post(self, request):
        response = Discount(request.data['id']).edit_cascade_term(infos=request.data['discount'])

        return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def delete(self, request):
        response = Discount().delete_cascade_term(id=request.query_params['id'])

        return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
    

class CascadeDiscountSearchView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        response = Discount().list_cascade_discount(page=request.query_params['page'], term=request.query_params['term'])

        return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
    

class CascadeDiscountSingleView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        response = Discount(request.query_params['id']).get_single_cascade_discount()

        return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)

    @validate_form('CascadeDiscountSingleFormPost')
    def post(self, request):
        response = Discount(request.data['id']).edit_cascade_discount(infos=request.data['discount'])

        return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
