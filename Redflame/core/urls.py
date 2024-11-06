from django.urls import path
from . import views
#------ To incude Media file ---------------
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index,name='index'),
    path('register/',views.register,name='register'),
    path('login/',views.log_in,name='login'),
    path('logout/',views.log_out, name="logout"),
    path('profile',views.profile,name='profile'),
    path('changepassword/',views.changepassword, name="changepassword"),
    path('trending/',views.trending,name='trending'),
    path('newarrival/',views.newarrival,name='newarrival'),
    path('bigcard/<int:id>/',views.bigcard,name='bigcard'),
    path('shirtcard/<int:id>/',views.shirtcard,name='shirtcard'),
    path('shirt/',views.shirt,name='shirt')


]


#--------- THis is will add file to media folder -----------
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)