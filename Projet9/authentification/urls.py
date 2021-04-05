from django.urls import path

from authentification import views


urlpatterns = [
    path('home', views.login_page, name="home"),
    path('logout', views.logout_user, name="logout"),
    path('account', views.register, name="account"),
    path('account/<int:id_user>', views.modify_account, name="modifyaccount"),
]