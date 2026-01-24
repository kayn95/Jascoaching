from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("services/", views.offers, name="offers"),
    path("stories/", views.results, name="results"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
]
