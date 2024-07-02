from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from . import views

urlpatterns = [

    path('accessprofile', views.AccessProfileView.as_view()),
    path('accessprofile/search', views.AccessProfileSearchView.as_view()),

    path('company', views.CompanyView.as_view(), name='company'),

    path('customer', views.CustomerInfoView.as_view(), name='customer'),
    path('customer/address', views.CustomerAddressView.as_view(), name='customer_address'),
    path('customer/contact', views.CustomerContactView.as_view(), name='customer_contact'),
    path('customer/profile', views.CustomerProfileView.as_view(), name='customer_profile'),
    path('customer/search', views.CustomerSearchView.as_view(), name='customer_search'),
    path('customer/seller', views.CustomerSellerView.as_view(), name='customer_seller'),
    path('customer/seller/single', views.CustomerSellerSingleView.as_view(), name='customer_seller_single'),

    path('discount/cascade/search', views.CascadeDiscountSearchView.as_view(), name='cascade_discount_search'),
    path('discount/cascade/single', views.CascadeDiscountSingleView.as_view(), name='cascade_discount_single'),
    path('discount/cascade/term', views.CascadeDiscountTermView.as_view(), name='cascade_discount_term'),
    path('discount/commission/search', views.CommissionDiscountSearchView.as_view(), name='commission_discount_search'),
    path('discount/commission/single', views.CommissionDiscountSingleView.as_view(), name='commission_discount_single'),
    path('discount/customer/search', views.CustomerTypeDiscountSearchView.as_view(), name='customer_type_discount_search'),
    path('discount/customer/single', views.CustomerTypeDiscountSingleView.as_view(), name='customer_type_discount_single'),
    path('discount/volume/search', views.VolumeDiscountSearchView.as_view(), name='volume_discount_search'),
    path('discount/volume/single', views.VolumeDiscountSingleView.as_view(), name='volume_discount_single'),
    
    path('financial/commissionpolicies', views.FinancialCommissionPoliciesView.as_view(), name='commission_policies_view'),
    path('financial/term', views.FinancialTermView.as_view(), name='term'),
    path('financial/term/range', views.FinancialTermRangeView.as_view(), name='term_range'),
    path('financial/term/single', views.FinancialTermSingleView.as_view(), name='term_single'),

    path('graphics/grouper', views.GraphicsGrouperView.as_view(), name='graphics_grouper'),
    
    path('localsale/config/single', views.LocalSaleConfigSingleView.as_view(), name='local_sale_config_single'),
    path('localsale/email', views.LocalSaleEmailView.as_view(), name='local_sale_email'),
    path('localsale/search', views.LocalSaleSearchView.as_view(), name='local_sale'),
    path('localsale/single', views.LocalSaleSingleView.as_view(), name='local_sale_single'),

    path('menu/list', views.MenuListView.as_view(), name='menu_list'),
    path('menu/favorite/list', views.MenuFavoriteListView.as_view(), name='menu_favorite_list'),
    path('menu/favorite', views.MenuFavoriteView.as_view(), name='menu_favorite'),

    path('offer/search', views.OfferSearchView.as_view(), name='offer_search'),
    path('offer/single', views.OfferSingleView.as_view(), name='offer_single'),
    path('offer/localsale/single', views.OfferLocalSaleSingleView.as_view(), name='offer_localsale_single'),
    
    path('order/book/search', views.OrderBookSearchView.as_view(), name='order_book'),
    path('order/book/single', views.OrderBookSingleView.as_view(), name='order_book_single'),
    path('order/type/search', views.OrderTypeSearchView.as_view(), name='order_type'),
    path('order/type/single', views.OrderTypeSingleView.as_view(), name='order_type_single'),
    
    path('payment', views.PaymentView.as_view(), name='payment'),
    path('payment/single', views.PaymentSingleView.as_view(), name='payment_single'),

    path('price', views.PriceView.as_view(), name='price'),
    path('price/product', views.PriceProductView.as_view(), name='price_product'),
    path('price/rules', views.PriceRulesView.as_view(), name='price_rules'),
    path('price/rules/single', views.PriceRulesSingleView.as_view(), name='price_rules_single'),
    path('price/single', views.PriceSingleView.as_view(), name='price_single'),
    path('price/structure/search', views.PriceStructureSearchView.as_view(), name='price_structure_search'),
    path('price/structure/single', views.PriceStructureSingleView.as_view(), name='price_structure_single'),
    path('price/term', views.PriceTermView.as_view(), name='price_term'),

    path('message/portal/search', views.MessagePortalView.as_view(), name='portal_message'),
    path('message/portal/single', views.MessagePortalSingleView.as_view(), name='portal_message_single'),
    
    path('product/brandsmanufacturers/single', views.ProductBrandsManufacturersSingleView.as_view(), name='product_brands_manufacturers_single'),
    path('product/dimensions/single', views.ProductDimensionsSingleView.as_view(), name='product_dimensions_single'),
    path('product/lines/search', views.ProductLinesSearchView.as_view(), name='product_lines_search'),
    path('product/lines/single', views.ProductLinesSingleView.as_view(), name='product_lines_single'),
    path('product/local/single', views.ProductLocalSingleView.as_view(), name='product_local_single'),
    path('product/margins/search', views.ProductMarginsSearchView.as_view(), name='product_margins_search'),
    path('product/margins/single', views.ProductMarginsSingleView.as_view(), name='product_margins_single'),
    path('product/margins/structure/single', views.ProductMarginsStructureSingleView.as_view(), name='product_margins_structure_single'),
    path('product/message/single', views.ProductMessageSingleView.as_view(), name='product_message_single'),
    path('product/search', views.ProductSearchView.as_view(), name='product'),
    path('product/single', views.ProductSingleView.as_view(), name='product_single'),
    path('product/structure/single', views.ProductStructureSingleView.as_view(), name='product_structure_single'),

    path('representative/search', views.RepresentativeSearchView.as_view(), name='representative_search'),
    path('represented/comissionpolicy', views.RepresentedComissionPolicyView.as_view(), name='represented_comission_policy'),
    path('represented/localsale', views.RepresentedLocalSaleView.as_view(), name='represented_local_sale'),
    path('represented/localsale/main', views.RepresentedLocalSaleMainView.as_view(), name='represented_local_sale'),
    path('represented/salesregion', views.RepresentedSalesRegionView.as_view(), name='represented_sales_region'),
    path('represented/search', views.RepresentedSearchView.as_view(), name='represented_search'),
    path('represented/single', views.RepresentedSingleView.as_view(), name='represented_single'),
    path('represented/status', views.RepresentedStatusView.as_view(), name='represented_status'),
    
    path('salesregion/represented', views.SalesRegionRepresentedView.as_view(), name='sale_regions_represented'),
    path('salesregion/search', views.SalesRegionSearchView.as_view(), name='sale_regions_search'),
    path('salesregion/sellers', views.SalesRegionSellersView.as_view(), name='sale_regions_sellers'),
    path('salesregion/single', views.SalesRegionSingleView.as_view(), name='sale_regions_single'),

    path('shippingcif/search', views.ShippingCifSearchView.as_view(), name='shipping_cif_search'),
    path('shippingcif/single', views.ShippingCifSingleView.as_view(), name='shipping_cif_single'),

    path('user/search', views.UserSearchView.as_view(), name='user_search'),
    
    path('workflow/order', views.WorkflowOrderView.as_view(), name='workflow_order'),
    path('workflow/order/search', views.WorkflowOrderSearchView.as_view(), name='workflow_order_search'),
    path('workflow/search', views.WorkflowSearchView.as_view(), name='workflow_search'),
    path('workflow/single', views.WorkflowSingleView.as_view(), name='workflow_single'),

    # token
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

    # user
    path('login', views.LoginView.as_view(), name='login'),
    path('user/image', views.UserImageView.as_view(), name='user_image'),
    path('verify', views.VerifyView.as_view(), name='verify'),
    
    # utilities
    path('list/city', views.ListCityOptionsView.as_view(), name='list_city_options'),
    path('list/options', views.ListOptionsView.as_view(), name='list_options'),
]
