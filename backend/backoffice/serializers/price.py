from .serializer import DynamicFieldsModelSerializer
from backoffice.models import PrecoProduto, PrecoRegra
from rest_framework import serializers

class PrecoProdutoSerializer(DynamicFieldsModelSerializer):
    produto = serializers.ReadOnlyField(source='get_product_infos')

    class Meta:
        model = PrecoProduto
        fields = '__all__'
        
        
class PrecoRegraSerializer(DynamicFieldsModelSerializer):
    datainicial = serializers.DateField(format="%d/%m/%Y")
    datafinal = serializers.DateField(format="%d/%m/%Y")
    
    class Meta:
        model = PrecoRegra
        fields = '__all__'