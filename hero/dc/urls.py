from django.urls import path
from . import views

urlpatterns = [
    path('superman/',views.superman),
    path('wonderman/',views.wonderman),
]