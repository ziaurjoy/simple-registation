from django.contrib import admin

# Register your models here.
from .models import Designation,Branch,Division,Title,EmployeeInfo

admin.site.register(Designation)
admin.site.register(Branch)
admin.site.register(Division)
admin.site.register(Title)
admin.site.register(EmployeeInfo)