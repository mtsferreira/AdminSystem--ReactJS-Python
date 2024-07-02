from .serializer import DynamicFieldsModelSerializer
from backoffice.models import WorkFlow
from backoffice.serializers.other import ListaCorSerializer
from rest_framework import serializers


class WorkFlowSerializer(DynamicFieldsModelSerializer):
    cor = ListaCorSerializer(source='idlistacor')

    class Meta:
        model = WorkFlow
        fields = '__all__'