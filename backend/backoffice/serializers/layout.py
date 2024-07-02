from .serializer import DynamicFieldsModelSerializer
from backoffice.models import Menu, MenuFavorito
from rest_framework import serializers


class MenuSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = Menu
        fields = '__all__'


class MenuFavoritoSerializer(DynamicFieldsModelSerializer):
    menu = MenuSerializer(read_only=True, source='idmenu')

    class Meta:
        model = MenuFavorito
        fields = '__all__'