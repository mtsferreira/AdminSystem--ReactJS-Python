from backoffice.models import Menu as MenuModel, MenuFavorito
from backoffice.serializers.layout import MenuFavoritoSerializer
from BO.user.user import AccessProfile
from django.db.models import F


class Menu:
    def __init__(self, menu_id):
        self.menu_id = menu_id

    def delete_favorite(self, user_id=None):
        response = {
            'status': True,
            'message': 'Menu desfavoritado com sucesso',
            'is_favorited': False
        }

        MenuFavorito.objects.get(idmenu=self.menu_id, idusuario=user_id).delete()

        return response

    def get_favorite(self, user_id=None):
        response = {
            'status': True,
            'message': 'Status obtido com sucesso',
            'is_favorited': False
        }

        try:
            MenuFavorito.objects.get(idmenu=self.menu_id, idusuario=user_id)
            response['is_favorited'] = True
            return response
        except:
            pass

        return response

    def save_favorite(self, user_id=None):
        response = {
            'status': True,
            'message': 'Menu favoritado com sucesso',
            'is_favorited': False
        }

        MenuFavorito(idmenu_id=self.menu_id, idusuario_id=user_id).save()

        return response

    @staticmethod
    def list_all_favorites(user_id):
        response = {
            'status': True,
            'message': 'Favoritos listado com sucesso',
            'favorites': []
        }

        favorites = MenuFavorito.objects.filter(idusuario=user_id)
        serializer = MenuFavoritoSerializer(favorites, many=True)

        response['favorites'] = serializer.data

        return response
    
    @staticmethod
    def list_all_modules(user_id=None):
        response = {
            'status': True,
            'message': 'Módulos listado com sucesso',
            'modules': []
        }

        enabled_children_modules = AccessProfile().get_access_profile_by_user(user_id=user_id)

        parent_modules = MenuModel.objects.filter(idmenu__in=enabled_children_modules).values_list('idmenupai', flat=True).distinct()

        modules = list(MenuModel.objects.filter(idmenupai__isnull=True, idmenu__in=parent_modules).order_by('ordem').values())

        for mod in modules:
            mod['submenus'] = MenuModel.objects.filter(idmenupai=mod['idmenu'], idmenu__in=enabled_children_modules).order_by('ordem').values()
            response['modules'].append(mod)

        return response
            
    @staticmethod
    def get_menu_options():
        return list(MenuModel.objects.filter(idmenupai__isnull=False).values('idmenu').annotate(value=F('idmenu'), label=F('descmenu')))