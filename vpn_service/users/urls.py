from django.urls import path

from . import views

app_name = 'users'
urlpatterns = [
    path('update/', views.EditProfileView.as_view(), name="update"),
    path('dashboard/', views.DashboardView.as_view(), name="dashboard"),
    path('user/', views.UserProfileView.as_view(), name="user_profile")

]

