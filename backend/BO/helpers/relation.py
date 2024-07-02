from BO.layout.general import (
    Cascade,
    City,
    ColorList,
    ComissionDiscount,
    ComissionPolicy,
    Margin,
    OrderType,
    SalesTeam,
    ShippingCif,
    TabGeral,
    VolumeClass
)
from BO.customer.customer import Customer
from BO.financial.offer import Offer
from BO.layout.graphics import Graphics
from BO.layout.menu import Menu
from BO.localsale.localsale import LocalSale
from BO.price.price import Price
from BO.product.product import Product
from BO.salesregion.salesregion import SalesRegion
from BO.user.user import User

option_relation_dict = {
    'bigGroup': Product.get_big_group_options(),
    'brand': Product.get_brand_options(),
    'cascade': Cascade.get_cascade_options(),
    'category': Product.get_category_options(),
    'city': City.get_city_options(),
    'colorListByName': ColorList.get_color_list_by_name_options(),
    'colorListByHex': ColorList.get_color_list_by_hex_options(),
    'comissionDiscount': ComissionDiscount.get_comission_discount_options(),
    'comissionPolicy': ComissionPolicy.get_comission_policy_options(),
    'comissionPolicyFull': ComissionPolicy.get_comission_policy_full_options(),
    'customerCoderpFantasy': Customer.get_customer_by_coderp_fantasy_options(),
    'customerType': Customer.get_customer_type_options(),
    'emailType': TabGeral.get_email_type_options(),
    'family': Product.get_family_options(),
    'graphicGrouper': Graphics.list_groupers_options(),
    'graphicType': Graphics.list_type_options(),
    'group': Product.get_group_options(),
    'localSale': LocalSale.get_local_sale_options(),
    'manufacturer': Product.get_manufacturer_options(),
    'margin': Margin.get_margin_options(),
    'menu': Menu.get_menu_options(),
    'offer': Offer.get_offer_options(),
    'orderType': OrderType.get_order_type_options(),
    'origin': Product.get_origin_options(),
    'price': Price.get_price_options(),
    'priceRules': Price.get_price_rules_options(),
    'product': Product.get_product_options(),
    'productLine': Product.get_product_line_options(),
    'salesRegion': SalesRegion.get_sale_regions_options(),
    'salesTeam': SalesTeam.get_sales_team_options(),
    'shippingCif': ShippingCif.get_shipping_cif_options(),
    'structurePrice': Price.get_structure_price_options(),
    'subGroup': Product.get_sub_group_options(),
    'uf': City.get_federative_unit_options(),
    'userIdName': User.get_user_id_name_options(),
    'userNameSurname': User.get_user_name_surname_options(),
    'volume': VolumeClass.get_volume_options(),
}