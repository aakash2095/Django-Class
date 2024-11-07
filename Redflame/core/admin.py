from django.contrib import admin
from . models import Userdetails,new_arrival,CartUpperwear
# Register your models here.


@admin.register(Userdetails)
class useradmin(admin.ModelAdmin):
    list_display=['id','user','name','address','city','state','pincode']


@admin.register(new_arrival)
class new_arrival_admin(admin.ModelAdmin):
    list_display=['id','name','category','short_d','desc','original_price','discounted_price']


@admin.register(CartUpperwear)
class cart_admin(admin.ModelAdmin):
    list_display=['id','user','product','quantity']

