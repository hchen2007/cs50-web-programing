from django.urls import path

from . import views

urlpatterns ={
    path("", views.index, name="index"),
    path("chen", views.chen, name="chen")
}