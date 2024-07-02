from BO.financial.offer import Offer 
from rest_framework import status
from rest_framework.decorators import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class OfferSearchView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            response = Offer().list_offers(page=request.query_params['page'], term=request.query_params['term'], isCurrent=request.query_params['isCurrent'], isExpired=request.query_params['isExpired'])

            return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
        except:
            return Response({'status': False, 'message': 'Erro interno ao executar função'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class OfferSingleView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            response = Offer(id=request.query_params['id']).get_single_offer_structure(page=request.query_params['page'])

            return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
        except:
            return Response({'status': False, 'message': 'Erro interno ao executar função'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def post(self, request):
        try:
            if request.data['type'] == 'updateOrCreate':
                response = Offer(id=request.data.get('id')).edit_single_offer(infos=request.data['offers'])

            elif request.data['type'] == 'addStructure':
                response = Offer(id=request.data.get('id')).create_single_offer_structure(infos=request.data['offersStructure'])

            return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
        except:
            return Response({'status': False, 'message': 'Erro interno ao executar função'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def delete(self, request):
        try:
            response = Offer().delete_single_offer_structure(id=request.query_params['id'])

            return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
        except:
            return Response({'status': False, 'message': 'Erro interno ao executar função'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        
class OfferLocalSaleSingleView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        try:
            response = Offer(id=request.query_params['id']).list_offers_localsale(page=request.query_params['page'])

            return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
        except:
            return Response({'status': False, 'message': 'Erro interno ao executar função'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def post(self, request):
        try:
            response = Offer(id=request.data['id']).create_single_offer_localsale(localsale_id=request.data['localsale'])
            
            return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
        except:
            return Response({'status': False, 'message': 'Erro interno ao executar função'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def delete(self, request):
        # try:
            response = Offer(id=request.query_params['id']).delete_single_offer_localsale(localsale_id=request.query_params['localsaleId'])

            return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
        # except:
        #     return Response({'status': False, 'message': 'Erro interno ao executar função'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)