from backoffice.models import (
    Cascata,
    Cidade,
    ComDesconto,
    EquipeVenda,
    FreteCif,
    GrupoEconomico as GrupoEconomicoModel,
    ListaCor,
    Margem,
    PoliticaComissao,
    Rede as RedeModel,
    RegiaoVenda,
    TabGeral as TabGeralModel,
    TipoFrete as TipoFreteModel,
    TipoPedido,
    Volume as VolumeModel,
)
from django.db.models import F, Count
from datetime import datetime


class Cascade:
    @staticmethod
    def get_cascade_options():
        return list(Cascata.objects.all().values('idcascata').annotate(value=F('idcascata'), label=F('descascata'))) # idcasacata = pk da tabela 


class City:
    def __init__(self, uf=None, codibge=None):
        self.uf = uf
        self.codibge = codibge
        self.response = {
            'status': True,
            'message': '',
        }  
        
    def get_city_name_by_code(self):
        city = Cidade.objects.get(codibge=self.codibge)
        
        return city.descidade
        
    def get_city_options_by_uf(self):
        city_options = Cidade.objects.filter(uf=self.uf).values().annotate(value=F('codibge'), label=F('descidade'))
        
        self.response['city_options'] = city_options
        
        self.response['message'] = 'Dados retornados'
        
        return self.response
    
    @staticmethod
    def get_city_options():
        return list(Cidade.objects.all().values('codibge').annotate(value=F('codibge'), label=F('descidade')))
    
    @staticmethod
    def get_federative_unit_options():
        return list(Cidade.objects.all().values('uf').annotate(Count('uf'), value=F('uf'), label=F('uf')))


class ColorList:
    @staticmethod
    def get_color_list_by_name_options():
        return list(ListaCor.objects.all().values('idlistacor').annotate(value=F('idlistacor'), label=F('descricao')))
    
    @staticmethod
    def get_color_list_by_hex_options():
        return list(ListaCor.objects.all().values('idlistacor').annotate(value=F('idlistacor'), label=F('cor')))


class ComissionDiscount:
    @staticmethod
    def get_comission_discount_options():
        return list(ComDesconto.objects.all().values('idcomdesconto').annotate(value=F('idcomdesconto'), label=F('descomissaodesc')))


class ComissionPolicy:
    @staticmethod
    def get_comission_policy_options():
        return list(PoliticaComissao.objects.all().values('idpolcomissao').annotate(value=F('idpolcomissao'), label=F('despolitica')))
    
    def get_comission_policy_full_options():
        return list(PoliticaComissao.objects.all().values().annotate(value=F('idpolcomissao'), label=F('despolitica')))


class GrupoEconomico:
    def __init__(self):
        pass
    
    @staticmethod
    def get_economic_group_options():
        return list(GrupoEconomicoModel.objects.filter(situacao='A').values('idgrupoeconomico').annotate(value=F('idgrupoeconomico'), label=F('descricao')))


class Margin:
    @staticmethod
    def get_margin_options():
        return list(Margem.objects.all().values('idmargem').annotate(value=F('idmargem'), label=F('desmargem')))


class OrderType:
    @staticmethod
    def get_order_type_options():
        return list(TipoPedido.objects.filter(situacao='A').values('idtipopedido').annotate(value=F('idtipopedido'), label=F('destipopedido')))


class Rede:
    @staticmethod
    def get_network_options():
        return list(RedeModel.objects.filter(situacao='A').values('idrede').annotate(value=F('idrede'), label=F('descricao')))
    
    @staticmethod
    def get_sales_region_by_id_list(id_list=[]):
        return RegiaoVenda.objects.filter(idregiao__in=id_list)


class SalesTeam:
    @staticmethod
    def get_sales_team_options():
        return list(EquipeVenda.objects.filter(situacao='A').values('idequipe').annotate(value=F('idequipe'), label=F('desequipe')))
    
    
class ShippingCif:
    @staticmethod
    def get_shipping_cif_options():
        today = datetime.now()
        return list(FreteCif.objects.filter(situacao='A', datainicial__lte=today, datafinal__gte=today).values('idfretecif').annotate(value=F('idfretecif'), label=F('desfretecif')))


class TabGeral:
    def __init__(self):
        pass
    
    @staticmethod
    def get_destination_options():
        return list(TabGeralModel.objects.filter(situacao='A', identificador='DESTINACAO').values('idtabgeral').annotate(value=F('idtabgeral'), label=F('descricao')))

    @staticmethod
    def get_fiscal_status_options():
        return list(TabGeralModel.objects.filter(situacao='A', identificador='SITUACAO FISCAL').values('idtabgeral').annotate(value=F('idtabgeral'), label=F('descricao')))

    @staticmethod
    def get_legal_nature_options():
        return list(TabGeralModel.objects.filter(situacao='A', identificador='NATUREZA JURIDICA').values('idtabgeral').annotate(value=F('idtabgeral'), label=F('descricao')))
    
    @staticmethod
    def get_email_type_options():
        return list(TabGeralModel.objects.filter(situacao='A', identificador='TIPO EMAIL').values('idtabgeral').annotate(value=F('idtabgeral'), label=F('descricao')))
    

class TipoFrete:
    @staticmethod
    def get_shipping_type_options():
        return list(TipoFreteModel.objects.filter(situacao='A').values('idtipofrete').annotate(value=F('idtipofrete'), label=F('descricao')))
    
    
class VolumeClass:
    @staticmethod
    def get_volume_options():
        today = datetime.now()
        return list(VolumeModel.objects.filter(situacao='A', datainicial__lte=today, datafinal__gte=today).values('idvolume').annotate(value=F('idvolume'), label=F('desvolume')))