from django.shortcuts import redirect, render,HttpResponse,redirect
from .models import student
from .forms import stuform

# Create your views here.
def home(request):
    if request.method == 'POST':
        stu = stuform(request.POST)    
        if stu.is_valid():
            stu.save()
    stu = stuform()
    stu_data=student.objects.all()
    return render(request, 'home.html',context={"stuform":stu,"stu_data":stu_data})



def delete(request,id):
    stu=student.objects.get(id=id)
    stu.delete()
    return redirect('home')


def update(request,id):
    instance=student.objects.get(id=id)
    if request.method == 'POST':
        stu = stuform(request.POST,instance=instance)    
        if stu.is_valid():
            stu.save()
        return redirect("home")
    stu = stuform(instance=instance)
    stu_data=student.objects.all()
    return render(request, 'update.html',context={"stuform":stu,"stu_data":stu_data})
