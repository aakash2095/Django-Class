from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),

    # path('product/<int:id>',views.product,name='product'),
    path('product/<int:id>',views.product,name='product')


]
