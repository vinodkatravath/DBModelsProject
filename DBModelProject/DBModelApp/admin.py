from django.contrib import admin
from DBModelApp.models import Employee
from DBModelApp.models import Company
# Register your models here.
#admin.site.register(Employee)
#admin.site.register(Company)



class EmployeeAdmin(admin.ModelAdmin):
    list_display=['eno','ename','esal','eaddr'];

admin.site.register(Employee,EmployeeAdmin);

class CompanyAdmin(admin.ModelAdmin):
 list_display = ['compid','compname','noofemps','compaddr','compsharevalue']

admin.site.register(Company, CompanyAdmin)












