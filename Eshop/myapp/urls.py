

from django.urls import path
from myapp.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path("", home, name="home"),
    # create url for accounts, cart,checkout,details,login-register,shop
    path("accounts",accounts,name="accounts"),
    path("cart",cart,name="cart"),
    path("checkout",checkout,name="checkout"),
    path("details",details,name="details"),
    path("login-register",login_register,name="login-register"),
    path("shop",shop,name="shop"),

   

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)  
    



