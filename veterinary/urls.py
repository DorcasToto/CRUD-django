from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.urls import path,include

urlpatterns = [
    path('',views.index,name = 'home'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('accounts/register/',views.register, name='registration'),
    path('register_vet/',views.register_vet,name = 'register_vet'),
    path('delete/<id>/',views.delete_vet,name = 'delete_vet'),
    path('update/<id>/',views.update_vet,name = 'update_vet')
  
]
