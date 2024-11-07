from django.contrib import admin
from . models import Userdetails,upperwear,new_arrival,cart
# Register your models here.


@admin.register(Userdetails)
class useradmin(admin.ModelAdmin):
    list_display=['id','user','name','address','city','state','pincode']

@admin.register(upperwear)
class upperwear_admin(admin.ModelAdmin):
    list_display=['id','name','category','short_d','desc','original_price','discounted_price']

@admin.register(new_arrival)
class new_arrival_admin(admin.ModelAdmin):
    list_display=['id','name','short_d','desc','original_price','discounted_price']


@admin.register(cart)
class cart_admin(admin.ModelAdmin):
    list_display=['id','user','product','quantity']