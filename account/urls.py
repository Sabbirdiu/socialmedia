from django.urls import path,include
from . import views
from account import views as user_views #for register
from django.contrib.auth import views as auth_views #for login/logout

urlpatterns = [

    path('',views.dashboard,name='dashboard'),
    # path('', include('django.contrib.auth.urls')),
    path('register/',user_views.register,name='register'),
    path('login/',auth_views.LoginView.as_view(template_name='account/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='account/logout.html'),name='logout'),
    path('password_change/',auth_views.PasswordChangeView.as_view(template_name='account/passwordChange.html'),name='passwordChange'),
    path('password_change/done/',auth_views.PasswordChangeDoneView.as_view(template_name='account/passwordDone.html'),name='password_change_done'),
    path('password_reset/',auth_views.PasswordResetView.as_view(template_name='account/passwordReset.html'),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='account/passwordResetDone.html'),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='account/passwordResetConfirm.html'),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(template_name='account/passwordResetComplete.html'),name='password_reset_complete'),

    

]