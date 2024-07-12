from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)  
    phone_no = models.IntegerField() 
    joining_date = models.DateField() 
    designation = models.CharField(max_length=100 , choices = [
        ('Frontend Developer' , 'Frontend Developer'),
        ('QA' , 'Quality Assurance'),
        ('UI/UX' , 'UI/UX Designer'),
        ('Full Stack Developer' , 'Full Stack Developer'),
        ('Backend Developer' , 'Backend Developer')
    ])

    def __str__(self):
        return self.name        

class EmployeeAttendance(models.Model):
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE)
    date = models.DateField()
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()
    # check_in = models.TimeField(auto_now=False , auto_now_add=False)
    # check_out = models.TimeField(auto_now=False , auto_now_add=False)
    manually_updated = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.employee.name} , {self.date}"
    
class EmployeeLeave(models.Model):
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE)
    leave_type = models.CharField(max_length=50 , choices = [
        ('Casual Leave' , 'Casual Leave'),
        ('Sick Leave' , 'Sick Leave'),
        ('Marriage Leave' , 'Marriage Leave'),
        ('Annual Leave' , 'Annual Leave'),
        ('Emergency Leave' , 'Emergency Leave')
    ])

    duration = models.PositiveIntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    is_approved = models.BooleanField()

    def __str__(self):
        return f"{self.employee.name} , {self.leave_type}"  