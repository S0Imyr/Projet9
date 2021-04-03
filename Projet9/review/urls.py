from django.urls import path

from review import views


urlpatterns = [
    path('', views.flux, name="flux"),
    path('addticket/', views.create_ticket, name="addticket"),
    path('addreview/', views.create_review, name="addreview"),
]