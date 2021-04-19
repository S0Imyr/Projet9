from django.urls import path

from review import views


urlpatterns = [
    path('', views.flux, name="flux"),
    path('follow/', views.follow, name="follow"),
    path('posts/', views.posts, name="posts"),

    path('addticket/', views.create_ticket, name="addticket"),
    path('addticket/<int:id_ticket>', views.create_ticket, name="addticket"),
    path('modifyticket/<int:id_ticket>', views.modify_ticket, name="modifyticket"),
    path('deleteticket/<int:id_ticket>', views.delete_ticket, name="deleteticket"),

    path('addreview/<int:id_ticket>', views.create_review, name="addreview"),
    path('modifyreview/<int:id_review>', views.modify_review, name="modifyreview"),
    path('deletereview/<int:id_review>', views.delete_review, name="deletereview"),

    path('addticketreview/', views.create_ticketreview, name="addticketreview"),

    path('deletefollow/<int:id_followed_user>', views.delete_follow, name="deletefollow"),
]
