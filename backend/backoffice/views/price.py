from backoffice.forms.decorator import validate_form
from BO.price.price import Price
from rest_framework import status
from rest_framework.decorators import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class PriceView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        response = Price().list_prices(page=request.query_params['page'], term=request.query_params['term'], current=request.query_params['isCurrent'], expired=request.query_params['isExpired'])
        return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
    

class PriceProductView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        response = Price(id=request.query_params['id']).get_price_products(page=request.query_params['page'])
        return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)


class PriceRulesView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        try:
            response = Price().list_price_rules(page=request.query_params['page'], term=request.query_params['term'], priceRulesCode=request.query_params['priceRulesCode'], isCurrent=request.query_params['isCurrent'], isExpired=request.query_params['isExpired'])
            return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
        except:
            return Response({'status': False, 'message': 'Erro interno ao executar função'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

class PriceRulesSingleView(APIView):
        permission_classes = [IsAuthenticated]
        
        def get(self, request):
            try:
                response = Price(id=request.query_params['id']).get_single_price_rules()
                return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
            except:
                return Response({'status': False, 'message': 'Erro interno ao executar função'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        @validate_form('PriceRulesSingleFormPost')
        def post(self, request):
            try:
                response = Price(id=request.data.get('id')).edit_single_price_rules(infos=request.data['priceRules'])
                return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
            except:
                return Response({'status': False, 'message': 'Erro interno ao executar função'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class PriceSingleView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        response = Price(id=request.query_params['id']).get_single_price()
        return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    @validate_form('PriceSingleFormPost')
    def post(self, request):
        response = Price(id=request.data['id']).edit_price(infos=request.data['price'])
        return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def delete(self, request):
        response = Price(id=request.query_params['id']).delete_price()
        return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)


class PriceTermView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        response = Price(id=request.query_params['id']).get_single_price_term(page=request.query_params['page'])
        return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def post(self, request):
        response = Price(id=request.data['id']).create_price_term(days=request.data['days'])
        return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def delete(self, request):
        response = Price().delete_price_term(id=request.query_params['id'])
        return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
    

class PriceStructureSearchView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        response = Price().list_price_structure(page=request.query_params['page'], term=request.query_params['term'], code=request.query_params['code'], isCurrent=request.query_params['isCurrent'], isExpired=request.query_params['isExpired'])
        return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
    

class PriceStructureSingleView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            response = Price(id=request.query_params['id']).get_single_price_structure_composition(page=request.query_params['page'])
            return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
        except:
            return Response({'status': False, 'message': 'Erro interno ao executar função'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def post(self, request):
        try:
            if request.data['type'] == 'updateOrCreate':
                response = Price(id=request.data.get('id')).edit_single_price_structure(infos=request.data['priceStructure'])

            elif request.data['type'] == 'addComposition':
                    response = Price(id=request.data.get('id')).create_single_price_structure_composition(infos=request.data['priceStructureComposition'])
            
            return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
        except:
            return Response({'status': False, 'message': 'Erro interno ao executar função'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def delete(self, request):
        try:
            response = Price().delete_price_structure_composition(id=request.query_params['id'])

            return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
        except:
            return Response({'status': False, 'message': 'Erro interno ao executar função'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)