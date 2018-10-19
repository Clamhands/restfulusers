from django.shortcuts import render, redirect
from .models import *

def index (request):
    context = {
        'test':User.objects.all()
    }
    return render(request,'users_app/index.html', context)

def add (request):
    User.objects.create(name=request.POST['name'],email=request.POST['email'])
    return redirect('/')

def new (request):
    return render(request, 'users_app/new.html')

def delete (request, userid):
    user=User.objects.get(id=userid)
    user.delete()
    return redirect('/')
def edit(request, userid):
    context={
        'user':User.objects.get(id=userid)
    }
    return render(request,'users_app/edit.html',context)
def update(request,userid):
    user=User.objects.get(id=userid)
    user.name=request.POST['name']
    user.email=request.POST['email']
    user.save()
    return redirect('/')
def show(request, userid):
    context={
        'user':User.objects.get(id=userid)
    }
    return render(request,'users_app/show.html',context)
def goback(request):
    return redirect('/')
def gonew(request):
    return render(request, 'users_app/new.html')


