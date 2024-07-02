from backoffice.forms.decorator import validate_form
from BO.financial.financial import Financial
from rest_framework import status
from rest_framework.decorators import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class FinancialTermView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        response = Financial().list_financial_terms(page=request.query_params['page'], term=request.query_params['term'], status=request.query_params['status'])
        return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)


class FinancialTermRangeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        response = Financial(id=request.query_params['id']).list_range_terms(page=request.query_params['page'])
        return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    @validate_form('FinancialTermRangeFormPost')
    def post(self, request):
        response = Financial(id=request.data['id']).edit_term_range(infos=request.data['termRange'])
        return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def delete(self, request):
        response = Financial(id=request.query_params['paymentId']).delete_range_term(id=request.query_params['id'])
        return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)


class FinancialTermSingleView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        response = Financial(request.query_params['id']).get_single_financial_term()
        return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)

    @validate_form('FinancialTermSingleFormPost')
    def post(self, request):
        response = Financial(request.data['id']).edit_financial_term(infos=request.data['paymentTerm'])
        return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
    

class FinancialCommissionPoliciesView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        response = Financial().list_financial_commission_policies(page=request.query_params['page'], term=request.query_params['term'], code=request.query_params['code'], status=request.query_params['status'])
        return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def post(self, request):
        if request.data['type'] == 'Include':
            response = Financial().create_single_commission_policies(infos=request.data['infos'])
        elif request.data['type'] == 'Edit':
            response = Financial(id=request.data.get('id')).edit_financial_commission_policies(infos=request.data['infos'])
        
        return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)