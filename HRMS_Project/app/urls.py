from django .urls import path
from . import views

urlpatterns = [
    path('' , views.homePage , name='home'),
    path('dashboard/' , views.dashboardPage , name='dashboard'),
    path('signup/' , views.signUpPage , name='signup'),
    path('login/' , views.loginPage , name='login'),
    path('logout/' , views.logoutPage , name='logout'),
    path('addemployee/' , views.addEmployeePage , name='addemployee'),
    path('employeedetails/' , views.employeeDetailsPage , name='employee_details'),
    path('employeedetails/deleteemployee/<int:id>',views.deleteEmployee),
    # path('editemployee/',views.editEmployee),
    path('addattendance/' , views.addAttendancePage , name = 'addattendance'),
    path('attendancedetails/' , views.attendanceDetailsPage , name = 'attendance_details'),
    path('attendancedetails/deleteattendance/<int:id>',views.deleteAttendance),
    path('attendancedetails/editattendance/<int:id>',views.editAttendance),
    path('attendancedetails/do_editattendance/<int:id>',views.doEditAttendance),

    # path('applyleave/' , views.applyForLeavePage , name = 'applyleave'),
    # path('applyleavedetails/' , views.LeaveDetailsPage , name = 'apply_leave_details'),
]
