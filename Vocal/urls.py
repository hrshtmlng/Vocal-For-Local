
from django.contrib import admin
from django.urls import path,re_path
from django.urls.conf import include

from django.views.static import serve

from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('shops.urls')),
    path('shops/',include('shops.urls')),
    path('listedShops/',include('listedShops.urls')),
    path('account/',include('userAccounts.urls')),
    path("__reload__/", include("django_browser_reload.urls")),
    path('auth_accounts/', include('allauth.urls')),
    path('home/', TemplateView.as_view(template_name='dashboard/home.html'), name='home'),
    re_path(r'^media/(?P<path>.*)$', serve,
        {'document_root':       settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve,
        {'document_root': settings.STATIC_ROOT}),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
