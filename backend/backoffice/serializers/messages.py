from .serializer import DynamicFieldsModelSerializer
from backoffice.models import PortalMensagem
from rest_framework import serializers

class PortalMensagemSerializer(DynamicFieldsModelSerializer):
    datainicial = serializers.DateTimeField(format="%d/%m/%Y")
    datafinal = serializers.DateTimeField(format="%d/%m/%Y")
    
    class Meta:
        model = PortalMensagem
        fields = '__all__'