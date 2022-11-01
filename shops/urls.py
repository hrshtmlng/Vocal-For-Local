from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from listedShops.views import listShop

from shops.views import filterByCity, landingPage, saveShopInfo, showShops, testCss

urlpatterns = [
    path('',landingPage),
    path('showShops',showShops),
    path('filters',filterByCity),
    path('test/',testCss),
    path('postShop',listShop),
    path('saveShop',saveShopInfo)
]