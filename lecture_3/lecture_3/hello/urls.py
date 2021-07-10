from django.urls import path

from . import views

urlpatterns ={
    path("", views.index, name="index"),
    path("chen", views.chen, name="chen"),
    path("steve", views.steve, name="steve"),
    path("<str:name>", views.greet, name="greet")
}