from django.urls import path

from account import views

app_name = 'account'

urlpatterns = [
    path('sign-up-account/', views.sign_up_account, name='sign_up_account'),
    path('login/', views.login_account, name="login_account"),
    path('logout/', views.log_out_account, name='log_out_account'),
    path('profile/', views.profile, name='profile'),
]
