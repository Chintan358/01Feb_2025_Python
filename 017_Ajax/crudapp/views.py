from django.shortcuts import render,HttpResponse
from crudapp.models import Student
from django.http import JsonResponse
# Create your views here.
def index(request):
    return render(request,"home.html")

def adddata(request):
    
    if request.method=='POST':
        data = request.POST
        uname = data.get("uname")
        email = data.get("email")
        age = data.get("age")

        Student.objects.create(username=uname,email=email,age=age)
        return HttpResponse("Registration successfully !!!")
    
def loaddata(request):
    alldata = Student.objects.all()
    return JsonResponse({"data":list(alldata.values())})