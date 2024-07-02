from .serializer import DynamicFieldsModelSerializer
from backoffice.models import LocalVenda
from rest_framework import serializers

class LocalVendaSerializer(DynamicFieldsModelSerializer):
    situacao = serializers.ReadOnlyField(source='get_status_description')
    
    class Meta:
        model = LocalVenda
        fields = '__all__'