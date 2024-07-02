from .serializer import DynamicFieldsModelSerializer
from backoffice.models import Cascata, Cliente, ClienteDado, ClienteEndereco, ClienteFiscal, ClientePerfil, ClienteVendedor, Volume
from rest_framework import serializers


class CasacataSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = Cascata
        fields = '__all__'


class VolumeSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = Volume
        fields = '__all__'


class ClienteSerializer(DynamicFieldsModelSerializer):

    dados = serializers.ReadOnlyField(source='get_customer_data')
    enderecos = serializers.ReadOnlyField(source='get_customer_address')
    especial = serializers.ReadOnlyField(source='get_customer_stamp')
    fiscal = serializers.ReadOnlyField(source='get_customer_fiscal')
    perfil = serializers.ReadOnlyField(source='get_customer_profile')

    class Meta:
        model = Cliente
        fields = '__all__'


class ClienteDadoSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = ClienteDado
        fields = '__all__'


class ClienteEnderecoSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = ClienteEndereco
        fields = '__all__'


class ClienteFiscalSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = ClienteFiscal
        fields = '__all__'


class ClientePerfilSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = ClientePerfil
        fields = '__all__'


class ClienteVendedorSerializer(DynamicFieldsModelSerializer):

    usuario = serializers.ReadOnlyField(source='get_seller_user_info')
    cascata = CasacataSerializer(read_only=True, source='idcascata')
    volume = VolumeSerializer(read_only=True, source='idvolume')

    class Meta:
        model = ClienteVendedor
        fields = ['usuario', 'cascata', 'volume', 'idcliente', 'idclientevendedor', 'tipousuario']