from django.contrib import admin
from . models import Userdetails,upperwear
# Register your models here.


@admin.register(Userdetails)
class useradmin(admin.ModelAdmin):
    list_display=['id','user','name','address','city','state','pincode']

@admin.register(upperwear)
class upperwear_admin(admin.ModelAdmin):
    list_display=['id','name','category','short_d','desc','original_price','discounted_price']