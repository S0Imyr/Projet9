
from django.urls import path

from review import views


urlpatterns = [
    path('review/', views.flux, name="flux"),
]