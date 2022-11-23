from django.urls import path
from fremmode import views

urlpatterns = [
  path("", views.home, name="index"),
  path("serviceworker.js", views.service_worker),
  path("manifest.json", views.manifest)
  ]
