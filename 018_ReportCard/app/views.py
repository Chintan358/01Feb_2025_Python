from django.shortcuts import render
from app.models import *
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    allStudent = Student.objects.all()
    paginator = Paginator(allStudent, 5) 
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request,"index.html",{"students":page_obj})