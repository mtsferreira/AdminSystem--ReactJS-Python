from .serializer import DynamicFieldsModelSerializer
from backoffice.models import Produto, ProdutoDados, ProdutoLocal, ProdutoMarca, ProdutoMensagem
from backoffice.serializers.localsale import LocalVendaSerializer
from backoffice.serializers.other import FabricanteSerializer, FamiliaSerializer, GrandeGrupoSerializer, GrupoSerializer, MarcaSerializer, SubGrupoSerializer, TabGeralSerializer
from rest_framework import serializers


class ProdutoEstruturaSerializer(DynamicFieldsModelSerializer):
    familia = FamiliaSerializer()
    ggrupo = GrandeGrupoSerializer()
    grupo = GrupoSerializer()
    sgrupo = SubGrupoSerializer()
    
    tipoproduto = TabGeralSerializer()  #caso o nome da variável e do campo no banco sejam diferentes, colocar assim = (source='tipopedido')
    origem = TabGeralSerializer()
    
    class Meta:
        model = ProdutoDados
        fields = '__all__'
        
class ProdutoLocalSerializer(DynamicFieldsModelSerializer):
    local = LocalVendaSerializer(source='idlocal')
    
    class Meta:
        model = ProdutoLocal
        fields = '__all__'

class ProdutoMarcaSerializer(DynamicFieldsModelSerializer):
    fabricante = FabricanteSerializer(source='idfabricante')
    marca = MarcaSerializer(source='idmarca')
    
    class Meta:
        model = ProdutoMarca
        fields = '__all__'

class ProdutoMensagemSerializer(DynamicFieldsModelSerializer):           # o ID da outra tabela está na tabela atual como ForeignKey
    local = serializers.ReadOnlyField(source='get_local_sale')
    
    class Meta:
        model = ProdutoMensagem
        fields = '__all__'

class ProdutoSerializer(DynamicFieldsModelSerializer):                   # o ID da tabela está na outra como ForeignKey
    informacao = serializers.ReadOnlyField(source='get_product_info')   # o ID de produto está na tabela de ProdutoInformação
    estrutura = serializers.ReadOnlyField(source='get_product_structure')
    
    class Meta:
        model = Produto
        fields = '__all__'
        

    

    
    