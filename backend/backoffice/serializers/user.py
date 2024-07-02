from .serializer import DynamicFieldsModelSerializer
from backoffice.models import AcessoPerfil, Usuario
from backoffice.serializers.other import TipoUsuarioSerializer
from rest_framework import serializers


class AcessoPerfilSerializer(DynamicFieldsModelSerializer):
    menu_list = serializers.ReadOnlyField(source='get_menu')
    usuarios = serializers.ReadOnlyField(source='get_user')

    class Meta:
        model = AcessoPerfil
        fields = '__all__'
        

class UsuarioSerializer(DynamicFieldsModelSerializer):
    tipousuario = TipoUsuarioSerializer()

    class Meta:
        model = Usuario
        fields = '__all__'