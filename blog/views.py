from django.shortcuts import render, redirect
from blog.forms import EmployeeForm
from blog.models import Employee
from viva import settings

def emp(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("/show")
            except:
                pass
    else:
        form = EmployeeForm()
    return render(request,'blog/index.html',{"BASE_URL":settings.Base_url,'form':form})

def show(request):
    employee = Employee.objects.all()
    return render(request,"blog/show.html",{"BASE_URL":settings.Base_url,'employee': employee})

def edit(request, id):
    employee = Employee.objects.get(id=id)
    return render(request,'blog/edit.html',{"BASE_URL":settings.Base_url,'employee': employee})

def update(request, id):
    employee = Employee.objects.get(id=id)
    form = EmployeeForm(request.POST, instance = employee)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request, 'blog/edit.html',{"BASE_URL":settings.Base_url,'employee': employee})

def delete(request, id):
        employee = Employee.objects.get(id=id)
        employee.delete()
        return redirect("/show")