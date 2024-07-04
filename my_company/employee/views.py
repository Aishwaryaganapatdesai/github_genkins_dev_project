from django.shortcuts import render,redirect
from .models import EmpModel
from .forms import EmpForm
def index(r):
    return render(r,'index.html')

def read_operation(r):
    objects = EmpModel.objects.all()
    my_dict = {'objects':objects}
    return render(r,'employee/emplist.html',context=my_dict)

def insert(r):
    form = EmpForm()
    if r.method=='POST':
        # a = 10 / 0
        print("In view function")
        form = EmpForm(r.POST)
        if form.is_valid():
            form.save()
            return redirect('/emplist/')
    return render(r,'employee/empform.html',{'form':form})

def update_operation(r,pk):
    emp = EmpModel.objects.get(pk=pk) # database
    if r.method=='POST':
        form = EmpForm(r.POST,instance=emp)
        if form.is_valid():
            form.save()
            return redirect("/emplist/")
    return render(r,'employee/update.html',{'emp':emp})

def delete_operation(r,pk):
    emp = EmpModel.objects.get(pk=pk)
    emp.delete()
    return redirect('/emplist/')