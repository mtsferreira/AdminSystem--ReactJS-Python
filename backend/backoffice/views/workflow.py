from BO.workflow.workflow import Workflow
from rest_framework import status
from rest_framework.decorators import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class WorkflowOrderView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            response = Workflow(id=request.data['id']).edit_order_workflow(workflow_id=request.data['workflowId'])
            return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
        except:
            return Response({'status': False, 'message': 'Erro interno ao executar função'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

class WorkflowOrderSearchView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            response = Workflow().get_orders(start_date=request.query_params['initialDate'], end_date=request.query_params['finalDate'], local_sale_id=request.query_params['localSale'])
            return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
        except:
            return Response({'status': False, 'message': 'Erro interno ao executar função'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

class WorkflowSearchView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        try:
            response = Workflow().get_workflow_list(page=request.query_params.get('page'), no_pagination=request.query_params.get('noPagination'))
            
            return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
        except:
            return Response({'status': False, 'message': 'Erro interno ao executar função'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def post(self, request):
        try:
            response = Workflow().create_workflow(infos=request.data['infos'])
            
            return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
        except:
            return Response({'status': False, 'message': 'Erro interno ao executar função'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def delete(self, request):
        try:
            response = Workflow(id=request.query_params['id']).delete_workflow()

            return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
        except:
            return Response({'status': False, 'message': 'Erro interno ao executar função'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    
class WorkflowSingleView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        try:
            response = Workflow(id=request.data['id']).edit_single_workflow(infos=request.data['workflow'])
            
            return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
        except:
            return Response({'status': False, 'message': 'Erro interno ao executar função'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)