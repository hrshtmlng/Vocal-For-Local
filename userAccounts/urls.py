from django.urls import path

from userAccounts.views import login,signup,register,getotp


urlpatterns = [
    path('login',login),
    path('signup',signup),
    path('register',register),
    path('otp',getotp)
]