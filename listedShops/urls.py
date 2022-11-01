from django.urls import path

from listedShops.views import listShop

urlpatterns = [
    path('postShop',listShop)
]