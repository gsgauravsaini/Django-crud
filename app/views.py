from django.http import HttpResponse
from django.shortcuts import redirect,render
from app.forms import UserForm
from app.models import User
from django.contrib import messages

 
def insert(request):
    if request.method == "POST":
        uname=request.POST['uname']
        uemail=request.POST['uemail']
        upassword=request.POST['upassword']
        form = UserForm(request.POST)
        if form.is_valid:
            try:
              form.save()
              messages.success(request,'Data Save Sucessfully')
            except:
                pass
    form = UserForm()
    return render(request,'index.html',{'form':form})

def show(request):
    users = User.objects.all()
    return render(request,'show.html',{'users':users})

def delete(request,id):
    user = User.objects.get(id=id)
    user.delete()
    return redirect('/show')

def edit(request,id):
    user = User.objects.get(id=id)
    return render(request, 'edit.html',{'user':user})       


def update(request,id):
    user = User.objects.get(id=id)
    form = UserForm(request.POST,instance = user)
    if form.is_valid():
        form.save()
        return redirect('/show')
    return render(request,'edit.html',{'user':user})



                



