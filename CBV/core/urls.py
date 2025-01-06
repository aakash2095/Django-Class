from django.urls import path
from . import views

urlpatterns = [
    path('',views.fbv,name='fbv')
]
