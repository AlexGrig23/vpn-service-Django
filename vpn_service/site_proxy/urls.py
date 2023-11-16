from django.urls import path
from .views import ExternalSiteProxyView

app_name = 'site_proxy'
urlpatterns = [
    path('external_site_proxy/<str:user_site_name>/<path:original_routes>/',
         ExternalSiteProxyView.as_view(),
         name='external_site_proxy'),

]