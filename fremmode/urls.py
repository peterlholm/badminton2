from django.urls import path
from fremmode import views

urlpatterns = [
  path("", views.home, name="index"),
  ]
