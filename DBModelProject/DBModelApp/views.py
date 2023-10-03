from django.shortcuts import render
from DBModelApp.models import Employee
from DBModelApp.models import Company

# Create your views here.
def empdate(request):
    emplist =Employee.objects.all()
    dict1={'emplist':emplist}
    return render(request, 'DBModelApp/emp.html', context=dict1);
def companydata(request):
    complist=Company.objects.all()
    dict1={'complist':complist}
    return render(request,'DBModelApp/company.html',context=dict1);


