from heart_disease import views
from django.urls import path

urlpatterns = [
    path("", views.heart, name="heart"),
]
