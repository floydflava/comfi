from django.urls import path
from django.views.static import serve
from django.conf.urls import url
from django.conf import settings
from .views import (
    AboutUs,
    Accessories,
    CardPaymentView,
    Clothes,
    ItemDetailView,
    CheckoutView,
    HomeView,
    OrderSuccessful,
    OrderSummaryView,
    PhoneView,
    PrivacyPolicy,
    SearchView,
    TermsConditions,
    add_to_cart,
    remove_from_cart,
    remove_single_item_from_cart,
    PaymentView,
    AddCouponView,
    RequestRefundView
)

app_name = 'rope'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('accessories', Accessories.as_view(), name='accessories'),
    path('search', SearchView.as_view(), name='search'),
    path('phones', PhoneView.as_view(), name='phones'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('add-coupon/', AddCouponView.as_view(), name='add-coupon'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('remove-item-from-cart/<slug>/', remove_single_item_from_cart,
         name='remove-single-item-from-cart'),
    path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),
    path('cardpayment/<payment_option>/', CardPaymentView.as_view(), name='cardpayment'),

    path('ordersuccessful', OrderSuccessful.as_view(), name='ordersuccessful'),
    path('clothes', Clothes.as_view(), name='clothes'),
    path('about_us', AboutUs.as_view(), name='about_us'),
    path('privacy-policy', PrivacyPolicy.as_view(), name='privacy-policy'),
    path('termsandconditions', TermsConditions.as_view(), name='termsandconditions'),




    path('request-refund/', RequestRefundView.as_view(), name='request-refund'),
    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
]
