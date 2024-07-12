from django.contrib import admin
from .models import Employee, EmployeeAttendance, EmployeeLeave

# Register your models here.

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name', 'designation', 'email', 'phone_no', 'joining_date']  
    
    search_fields = ['name', 'designation', 'email', 'phone_no']  

@admin.register(EmployeeAttendance)
class EmployeeAttendanceAdmin(admin.ModelAdmin):
    list_display = ['employee', 'date', 'check_in', 'check_out', 'manually_updated']
    search_fields = ['employee__name']
    list_filter = ['date', 'manually_updated']
    date_hierarchy = 'date'

@admin.register(EmployeeLeave)
class EmployeeLeaveAdmin(admin.ModelAdmin):
    list_display = ['employee', 'leave_type', 'duration', 'start_date', 'end_date', 'is_approved']
    search_fields = ['employee__name', 'leave_type']
    list_filter = ['leave_type', 'is_approved']
    date_hierarchy = 'start_date'
