from django.urls import path
from . import views
from account import views as user_views #for register
from django.contrib.auth import views as auth_views #for login/logout

urlpatterns = [

    path('',views.dashboard,name='dashboard'),
    path('register/',user_views.register,name='register'),
    path('login/',auth_views.LoginView.as_view(template_name='account/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='account/logout.html'),name='logout'),
    

]