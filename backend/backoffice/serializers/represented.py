from .serializer import DynamicFieldsModelSerializer
from backoffice.models import Representada
from rest_framework import serializers

class RepresentadaSerializer(DynamicFieldsModelSerializer):

    cidade = serializers.ReadOnlyField(source='get_city')
    situacao = serializers.ReadOnlyField(source='get_status_description')

    class Meta:
        model = Representada
        fields = '__all__'