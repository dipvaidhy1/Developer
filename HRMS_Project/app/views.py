from django.shortcuts import render , HttpResponse , redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from app.models import *

# Create your views here.

@login_required(login_url = 'login')
def homePage(request):
    return render(request , "home.html")

def dashboardPage(request):
    return render(request , "dashboard.html")    

# def signUpPage(request):

#     if request.method == 'POST' :
#         sname = request.POST.get('username') 
#         semail = request.POST.get('email') 
#         spassword1 = request.POST.get('password') 
#         spassword2 = request.POST.get('confirm-password') 

#         if spassword1 != spassword2 :
#             messages.info(request,"Your Password and confirmation password are not same!!!")
#             return redirect('signup')

#         # elif sname == username:
#         #     messages.info(request,"user already exist")
#         #     return redirect('signup')

#         else :
#             my_user = User.objects.create_user(sname , semail , spassword1)
#             my_user.save()
#             return redirect('login')

#         # print(name , email , password1 , password2)

#     return render(request , "signup.html")

# def signUpPage(request):
#     if request.method == 'POST':
#         sname = request.POST.get('username') 
#         semail = request.POST.get('email') 
#         spassword1 = request.POST.get('password') 
#         spassword2 = request.POST.get('confirm-password') 

#         if spassword1 != spassword2:
#             return JsonResponse({'error': 'Your Password and confirmation password are not the same!'}, status=400)  # Return error JSON response
#         else:
#             my_user = User.objects.create_user(sname, semail, spassword1)
#             my_user.save()
#             return JsonResponse({'redirect_url': '/login/'})  # Return JSON response for redirecting to login page

def signUpPage(request):
    if request.method == 'POST':
        sname = request.POST.get('username') 
        semail = request.POST.get('email') 
        spassword1 = request.POST.get('password') 
        spassword2 = request.POST.get('confirm-password') 

        if spassword1 != spassword2:
            messages.info(request, "Your password and confirmation password do not match!")
            return JsonResponse({'error': 'Password mismatch'}, status=400)  # Return error message

        # Check if the user already exists with the same username or email
        if User.objects.filter(username=sname).exists() or User.objects.filter(email=semail).exists():
            messages.info(request, "User with the same username or email already exists!")
            return JsonResponse({'error': 'User already exists'}, status=400)  # Return error message

        # Create a new user if validation passes
        my_user = User.objects.create_user(sname, semail, spassword1)
        my_user.save()
        return JsonResponse({'redirect_url': '/login/'})  # Redirect to login page after successful signup

    # If the request is not POST, render the signup page template
    return render(request, "signup.html")

# def loginPage(request):

#     if request.method=="POST" :
#         lname = request.POST.get('username') 
#         lpassword = request.POST.get('password') 

#         user = authenticate (request , username = lname , password = lpassword)

#         if user is not None:
#             login(request , user)
#             return redirect('dashboard') 

#         else :
#             # return HttpResponse("Username or Password is incorrect!!!")
#             messages.info(request,"username not matched !")

#         # print(lname , lpassword)

#     return render(request , "login.html")

# def loginPage(request):
#     if request.method == "POST":
#         lname = request.POST.get('username') 
#         lpassword = request.POST.get('password') 

#         user = authenticate (request , username = lname , password = lpassword)

#         if user is not None:
#             login(request, user)
#             return JsonResponse({'redirect_url': '/dashboard/'})  # Return JSON response
#         else:
#             return JsonResponse({'error': 'Username or Password is incorrect!'}, status=400)  # Return error JSON response

def loginPage(request):
    if request.method == "POST":
        lname = request.POST.get('username') 
        lpassword = request.POST.get('password') 

        user = authenticate(request, username=lname, password=lpassword)

        if user is not None:
            login(request, user)
            return JsonResponse({'redirect_url': '/dashboard/'})  # Redirect to dashboard upon successful login
        else:
            messages.info(request, "Username or password is incorrect!")
            return JsonResponse({'error': 'Username or password is incorrect!'}, status=400)  # Return error message

    # If the request is not POST, render the login page template
    return render(request, "login.html")


# def logoutPage(request):

#     logout(request)
#     return redirect('home')

#     return render(request , "logout.html")

# def logoutPage(request):
#     if request.method == 'POST':
#         logout(request)
#         return JsonResponse({'redirect_url': '/home/'})  
#     else:
#         return render(request, "dashboard.html")

def logoutPage(request):
    if request.method == 'POST':
        logout(request)
        return JsonResponse({'redirect_url': '/signup/'})  
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

# def addEmployeePage(request):
    
#     # print(request.POST)
    
#     if request.method=="POST":
#         employee = Employee.objects.all()
        
#         name = request.POST["name"]
#         designation = request.POST["designation"]
#         email = request.POST["email"]
#         phone_no = request.POST["phone_no"]
#         joining_date = request.POST["joining_date"]

#         # print(name,designation)

#         employee = Employee(name=name , designation=designation , email=email , phone_no=phone_no , joining_date=joining_date)
#         employee.save()
#         print('2')
        
#         return redirect("employee_details")

#     return render(request , "add_employee.html" , {})


def addEmployeePage(request):

    if request.method == "POST":
        name = request.POST.get("name")
        designation = request.POST.get("designation")
        email = request.POST.get("email")
        phone_no = request.POST.get("phone_no")
        joining_date = request.POST.get("joining_date")

        # Save employee data to the database
        employee = Employee.objects.create(
            name=name,
            designation=designation,
            email=email,
            phone_no=phone_no,
            joining_date=joining_date,
        )

        # Return a JSON response indicating success
        return JsonResponse({'success': True, 'message': 'Employee added successfully.'})
    elif request.method == "GET":
        # Handle GET request (render the form)
        return render(request, "add_employee.html", {})
    else:
        # Handle other request methods
        return JsonResponse({'success': False, 'message': 'Invalid request method.'})

def employeeDetailsPage(request):
    employee = Employee.objects.all()
    return render(request , "employee_details.html" , {'employee': employee})

def deleteEmployee(request,id):
    employee = Employee.objects.get(pk=id)
    employee.delete()

    return redirect("employee_details")

# def editEmployee(request):
#     return render(request, 'edit_employee.html',{})

# def addAttendancePage(request):
#     if request.method == "POST":
       
#         employee_name = request.POST.get("name")
#         date = request.POST.get("date")
#         check_in = request.POST.get("check_in")
#         check_out = request.POST.get("check_out")
#         manually_updated = request.POST.get("manually_updated", False)

#         try:

#             matching_employees = Employee.objects.filter(name=employee_name)

#             if matching_employees.exists():
        
#                 employee = matching_employees.first()

#                 attendance = EmployeeAttendance(
#                     employee=employee,  
#                     date=date,
#                     check_in=check_in,
#                     check_out=check_out,
#                     manually_updated=manually_updated
#                 )
#                 attendance.save() 

#                 return redirect("attendance_details")

#         except:
#             pass

#         else:
#             messages.info(request,"Employee does not exist!")  

#             return redirect("addattendance") 
        

#     return render(request, 'add_attendance.html', {})

def addAttendancePage(request):
    if request.method == "POST" and request.is_ajax():
        employee_name = request.POST.get("employee")
        date = request.POST.get("date")
        check_in = request.POST.get("check-in")
        check_out = request.POST.get("check-out")
        manually_updated = request.POST.get("manually-updated", False)

        try:
            matching_employees = Employee.objects.filter(name=employee_name)

            if matching_employees.exists():
                employee = matching_employees.first()

                attendance = EmployeeAttendance.objects.create(
                    employee=employee,
                    date=date,
                    check_in=check_in,
                    check_out=check_out,
                    manually_updated=manually_updated
                )

                return JsonResponse({'success': True, 'message': 'Attendance added successfully.'})
            else:
                return JsonResponse({'success': False, 'message': 'Employee does not exist.'})

        except Exception as e:
            return JsonResponse({'success': False, 'message': 'Error occurred: {}'.format(str(e))})

    else:
        return JsonResponse({'success': False, 'message': 'Invalid request method or not AJAX.'})

        

def attendanceDetailsPage(request):
    attendance = EmployeeAttendance.objects.all()

    return render(request , 'attendance_details.html' , {'attendance' : attendance})

def deleteAttendance(request,id):
    delete_attendance = EmployeeAttendance.objects.get(pk=id)
    delete_attendance.delete()

    return redirect("attendance_details")    

def editAttendance(request,id):

    edit_atd = EmployeeAttendance.objects.get(pk=id)

    return render(request , "edit_attendace.html" , {'edit_atd' :  edit_atd})    


def doEditAttendance(request,id):
    employee_name = request.POST.get("name")
    date = request.POST.get("date")
    check_in = request.POST.get("check_in")
    check_out = request.POST.get("check_out")
    manually_updated = request.POST.get("manually_updated" , False)

    edit_atd = EmployeeAttendance.objects.get(pk=id)

    edit_atd.employee_name = employee_name
    edit_atd.date = date
    edit_atd.check_in = check_in
    edit_atd.check_out = check_out
    edit_atd.manually_updated = manually_updated

    edit_atd.save()

    return redirect("attendance_details")     

def applyForLeavePage(request):
    
    # print(request.POST)
    
    if request.method=="POST":
        # leave_apply = EmployeeLeave.objects.all()
        
        employee_name = request.POST.get("name")
        leave_type = request.POST.get("leave_type")
        duration = request.POST.get("duration")
        start_date = request.POST.get("start_date")
        end_date = request.POST.get("end_date")
        
        # print(employee_name , leave_type , duration , start_date , end_date )

        try:
            matching_employees = Employee.objects.filter(name=employee_name)

            if matching_employees.exists():
        
                employee = matching_employees.first()

                apply_leave = EmployeeLeave(
                    employee=employee, 
                    leave_type = leave_type,
                    duration = duration, 
                    start_date = start_date,
                    end_date = end_date,
                    
                )
                apply_leave.save()
                # print('2')

                return redirect("apply_leave_details")

        except:
            pass

        else:
            messages.info(request,"Employee does not exist!")  

            return redirect("applyleave")         

        # print(employee_name , leave_type , duration , start_date , end_date)

    return render(request , "leave_apply.html" , {})

def LeaveDetailsPage(request):
    apply_leave = EmployeeLeave.objects.all()

    return render(request , 'applyleave_details.html' , {'apply_leave' : apply_leave})