from django.shortcuts import render , HttpResponse
from .models import Employee , Role , Department
from datetime import datetime
from django.db.models import Q
# Create your views here.
def index(request):
    return render(request, 'index.html')

def all_emp(request):
    employees = Employee.objects.all()
    context = {
        'employees' : employees
    }
    return render(request, 'all_emp.html',context)
def add_emp(request):
    if request.method == 'POST':
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
        phone = int(request.POST['phone'])
        department_id = int(request.POST['department'])
        role_id = int(request.POST['role'])

        # Retrieve Department and Role instances
        department_instance = Department.objects.get(pk=department_id)
        role_instance = Role.objects.get(pk=role_id)

        # Create and save the Employee instance
        new_employee = Employee(
            firstName=firstName,
            lastName=lastName,
            salary=salary,
            bonus=bonus,
            phone=phone,
            department=department_instance,
            role=role_instance,
            join_date=datetime.now()
        )
        new_employee.save()

        return HttpResponse('Employee added Successfully')

    elif request.method == 'GET':
        return render(request, 'add_emp.html')

    else:
        return HttpResponse("An Exception Occurred! Employee Has Not Been Added")


def delete_emp(request, emp_id = 0):
    if emp_id:
        try:
            emp_to_be_removed = Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return HttpResponse("Employee Removed Successfully")
        except:
            return HttpResponse("Please Enter A Valid EMP ID")
    employees = Employee.objects.all()
    context = {
        'employees': employees
    }
    return render(request, 'delete_emp.html' ,context)

def search_emp(request):
    if request.method == 'POST':
        # name = request.POST['name','']
        # dept = request.POST['dept','']
        # role = request.POST['role','']
        name = request.POST.get('name', '')
        dept = request.POST.get('department', '')
        role = request.POST.get('role', '')

        employees = Employee.objects.all()
        if name:
            employees = employees.filter(Q(firstName__icontains = name) | Q(lastName__icontains = name))
        if dept:
            employees = employees.filter(dept__name__icontains = dept)
        if role:
            employees = employees.filter(role__name__icontains = role)

        context = {
            'employees': employees
        }
        return render(request, 'all_emp.html', context)

    elif request.method == 'GET':
        return render(request, 'search_emp.html')
    else:
        return HttpResponse('An Exception Occurred')
