from .serializer import DynamicFieldsModelSerializer
from backoffice.models import RegiaoVendedor, RepresentadaRegiao
from backoffice.serializers.represented import RepresentadaSerializer
from rest_framework import serializers


class RegiaoVendedorSerializer(DynamicFieldsModelSerializer):
    usuario = serializers.ReadOnlyField(source='get_users')
    
    class Meta:
        model = RegiaoVendedor
        fields = '__all__'
        
class RegiaoRepresentadaSerializer(DynamicFieldsModelSerializer):
    representada = RepresentadaSerializer(source='idrepresentada')

    class Meta:
        model = RepresentadaRegiao
        fields = '__all__'