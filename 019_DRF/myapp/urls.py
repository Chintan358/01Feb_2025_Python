from django.urls import path
from myapp.views import *

urlpatterns = [
    path("getstudents",index,name="index"),
    path("addstudent",add,name="add"),
    path("updatestudent/<int:id>",update,name="update"),
    path("deletestudent/<int:id>",delete,name="delete")
]