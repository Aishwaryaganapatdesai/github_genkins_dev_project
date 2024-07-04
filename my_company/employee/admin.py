from django.contrib import admin
from .models import EmpModel
# Register your models here.
class EmpAdmin(admin.ModelAdmin):
    list_display = ['eid','ename','ecity','esal','eemail','edept']

admin.site.register(EmpModel,EmpAdmin)