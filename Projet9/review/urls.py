from django.urls import path

from review import views


urlpatterns = [
    path('', views.flux, name="flux"),
    path('follow/', views.follow, name="follow"),
    path('posts/', views.posts, name="posts"),
    path('addticket/', views.create_ticket, name="addticket"),
    path('addticket/<int:id_ticket>', views.create_ticket, name="addticket"),
    path('addreview/', views.create_review, name="addreview"),
    path('addreview/<int:id_ticket>', views.create_review, name="addreview"),
    path('addticketreview/', views.create_ticketreview, name="addticketreview"),
]