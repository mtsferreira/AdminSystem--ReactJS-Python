from backoffice.forms.decorator import validate_form
from BO.product.product import Product
from rest_framework import status
from rest_framework.decorators import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class ProductSearchView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        try:
            response = Product().list_product(page=request.query_params['page'], term=request.query_params['term'])
            
            return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
        except:
            return Response({'status': False, 'message': 'Erro interno ao executar função'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class ProductSingleView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        try:
            response = Product(id=request.query_params['id']).get_single_product()
        
            return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
        except:
            return Response({'status': False, 'message': 'Erro interno ao executar função'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def post(self, request):
        try:
            response = Product(id=request.data['id']).edit_single_product(infos=request.data['product'])
            
            return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
        except:
            return Response({'status': False, 'message': 'Erro interno ao executar função'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
class ProductMessageSingleView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        try:
            response = Product(id=request.query_params['id']).get_single_product_message(page=request.query_params['page'])
            
            return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
        except:
            return Response({'status': False, 'message': 'Erro interno ao executar função'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def post(self, request):
        try:
            response = Product(id=request.data['id']).edit_single_product_message(infos=request.data['productMessage'])
        
            return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
        except:
            return Response({'status': False, 'message': 'Erro interno ao executar função'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class ProductStructureSingleView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        try:
            response = Product(id=request.query_params['id']).get_single_product_structure()
            
            return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
        except:
            return Response({'status': False, 'message': 'Erro interno ao executar função'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    @validate_form('ProductStructureSingleFormPost')
    def post(self, request):
        try:
            response = Product(id=request.data['id']).edit_single_product_structure(infos=request.data['productStructure'])
            
            return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
        except:
            return Response({'status': False, 'message': 'Erro interno ao executar função'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class ProductDimensionsSingleView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        try:
            response = Product(id=request.query_params['id']).get_single_product_dimensions(page=request.query_params['page'])
            
            return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
        except:
            return Response({'status': False, 'message': 'Erro interno ao executar função'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
class ProductLocalSingleView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self,request):
        try:
            response = Product(id=request.query_params['id']).get_single_product_local(page=request.query_params['page'])
            
            return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
        except:
            return Response({'status': False, 'message': 'Erro interno ao executar função'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def post(self, request):
        try:
            response = Product().edit_singel_product_local(product_local_id=request.data['id'], infos=request.data['productLocal'])
            
            return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
        except:
            return Response({'status': False, 'message': 'Erro interno ao executar função'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class ProductBrandsManufacturersSingleView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        try:
            response = Product(id=request.query_params['id']).get_single_product_brands_manufacturers(page=request.query_params['page'])
            
            return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
        except:
            return Response({'status': False, 'message': 'Erro interno ao executar função'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
class ProductLinesSearchView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        try:
            response = Product().list_product_lines(page=request.query_params['page'], term=request.query_params['search'], productlinescode=request.query_params['productLinesCode'], status=request.query_params['status'])
            
            return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
        except:
            return Response({'status': False, 'message': 'Erro interno ao executar função'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def post(self, request):
        try:
            response = Product().create_product_lines(infos=request.data['infos'])
            
            return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
        except:
            return Response({'status': False, 'message': 'Erro interno ao executar função'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
class ProductLinesSingleView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        try:
            response = Product(id=request.query_params['id']).get_single_product_lines_structure(page=request.query_params['page'])
            
            return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
        except:
            return Response({'status': False, 'message': 'Erro interno ao executar função'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    @validate_form('ProductLinesSingleFormPost')
    def post(self, request):
        try:
            if request.data['type'] == 'updateProductLine':
                response = Product(id=request.data['id']).edit_single_product_lines(infos=request.data['productLines'])
                
            elif request.data['type'] == 'addProductLinesStructure':
                response = Product(id=request.data['id']).create_single_product_lines_structure(infos=request.data['productLinesStructure'])
                
            return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
        except:
            return Response({'status': False, 'message': 'Erro interno ao executar função'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def delete(self, request):
        try:
            response = Product().delete_single_product_lines_structure(id=request.query_params['id'])
            
            return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
        except:
            return Response({'status': False, 'message': 'Erro interno ao executar função'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class ProductMarginsSearchView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        try:
            response = Product().list_product_margins(page=request.query_params['page'], term=request.query_params['search'], marginscode=request.query_params['marginsCode'], status=request.query_params['status'])
            
            return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
        except:
            return Response({'status': False, 'message': 'Erro interno ao executar função'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
class ProductMarginsSingleView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        try:
            response = Product(id=request.query_params['id']).get_single_product_margin()
            
            return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
        except:
            return Response({'status': False, 'message': 'Erro interno ao executar função'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    @validate_form('MarginsSingleFormPost')
    def post(self, request):
        try:
            response = Product(id=request.data.get('id')).edit_single_product_margin(infos=request.data['margins'])
            
            return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
        except:
            return Response({'status': False, 'message': 'Erro interno ao executar função'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
class ProductMarginsStructureSingleView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        try:
            response = Product(id=request.query_params['id']).get_single_product_margin_structure(page=request.query_params['page'])
            
            return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
        except:
            return Response({'status': False, 'message': 'Erro interno ao executar função'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def post(self, request):
        try:
            response = Product(id=request.data['id']).create_single_product_margin_structure(infos=request.data['marginsStructure'])
            
            return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
        except:
            return Response({'status': False, 'message': 'Erro interno ao executar função'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def delete(self, request):
        try:
            response = Product().delete_single_product_margin_structure(id=request.query_params['id'])
            
            return Response(response, status=status.HTTP_200_OK if response['status'] else status.HTTP_500_INTERNAL_SERVER_ERROR)
        except:
            return Response({'status': False, 'message': 'Erro interno ao executar função'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)