from django.urls import path

from . import views
from .views import logout_view

app_name = 'default_auth'
urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),
    path('signup/', views.SignupView.as_view(), name="signup"),
    path('login/', views.LoginView.as_view(), name="login"),
    path('logout/', logout_view, name="logout"),
]