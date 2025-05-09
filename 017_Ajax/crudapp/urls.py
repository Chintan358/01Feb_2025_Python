from django.urls import path
from crudapp.views import *
urlpatterns = [

    path("",index,name="index"),
    path("adddata",adddata,name="adddata"),
    path("loaddata",loaddata,name="loaddata")

]