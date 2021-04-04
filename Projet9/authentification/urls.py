from django.urls import path

from authentification import views


urlpatterns = [
    path('home', views.login, name="home"),
    path('account', views.register, name="account"),
    path('account/<int:id_user>', views.modifyaccount, name="modifyaccount"),
]