from django.urls import path
from .views import WebSiteCreateView, WebSiteDetailView, WebSiteStatsView

app_name = 'web_sites'
urlpatterns = [
    path('create_web_site/', WebSiteCreateView.as_view(), name="create_web_site"),
    path('statistic/', WebSiteStatsView.as_view(), name="statistic"),
    path('detail_web_site/<int:site_id>/', WebSiteDetailView.as_view(), name="detail_web_site")

]

