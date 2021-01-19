from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.urls import path,include

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('',views.index,name = 'home'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('accounts/register/',views.register, name='registration'),
    path('register_vet/',views.register_vet,name = 'register_vet'),
    path('delete/<id>/',views.delete_vet,name = 'delete_vet'),
    path('update/<id>/',views.update_vet,name = 'update_vet'),

    #api endpoint urls
    path('api/add_admin/',views.UserViewSet.as_view(),name = 'add_admin'),
    path('api/vets/',views.VetList.as_view(),name = 'vets'),
    path('api/vets/<pk>/',views.VetDetailList.as_view(),name = 'vet_detail'),
    path('api/login/', TokenObtainPairView.as_view(), name='login'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

  
]
