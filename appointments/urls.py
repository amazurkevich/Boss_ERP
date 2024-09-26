from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("appointments/", views.appointments_view, name="appointments"),
    path("teachers/", views.all_teachers_view, name="teachers")
]