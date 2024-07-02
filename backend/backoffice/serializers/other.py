from .serializer import DynamicFieldsModelSerializer
from backoffice.models import Fabricante, Familia, GrandeGrupo, Grupo, ListaCor, Marca, SubGrupo, TabGeral, TipoUsuario
from rest_framework import serializers


class FabricanteSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = Fabricante
        fields = '__all__'


class FamiliaSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = Familia
        fields = '__all__'
        

class GrandeGrupoSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = GrandeGrupo
        fields = '__all__'
        

class GrupoSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = Grupo
        fields = '__all__'
        
        
class ListaCorSerializer(DynamicFieldsModelSerializer):
    
    class Meta:
        model = ListaCor
        fields = '__all__'

        
class MarcaSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = Marca
        fields = '__all__'
        
        
class SubGrupoSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = SubGrupo
        fields = '__all__'
        

class TabGeralSerializer(DynamicFieldsModelSerializer):
    
    class Meta:
        model = TabGeral
        fields = '__all__'
        

class TipoUsuarioSerializer(DynamicFieldsModelSerializer):
    
    class Meta:
        model = TipoUsuario
        fields = '__all__'