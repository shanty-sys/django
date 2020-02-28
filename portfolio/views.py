from django.shortcuts import render
from job.models import job
from django.shortcuts import redirect
from django.contrib import auth
from django.contrib.auth.models import User
from job.models import job
from django.shortcuts import get_object_or_404
from django.http import request
from django.contrib.auth.decorators import login_required
def home(request):
    jobs = job.objects
   
    return render(request,'home.html',{'job':jobs})
def signup(request):
    if request.method == 'POST':
        #user has info and wants an account now
        if request.POST['password1']== request.POST['password2']:
            try:
                user=User.objects.get(username=request.POST['username'])
                return render(request,'signup.html',{'error':'user already exist'})
            except:
                user=User.objects.create_user(username=request.POST['username'],password=request.POST['password1'])
                auth.login(request,user)
                return redirect('home')
        else:
            return render(request,'signup.html',{'error':"password did not match"})
        
    return render(request,'signup.html')


def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username = request.POST['username'],password=request.POST['password1'])
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            return render(request,'login.html',{'error':"username or password is incorrect"})
    else:
            return render(request,'login.html')
    return render(request,'login.html')
@login_required(login_url="/signup")
def create(request):
    if request.method=="POST":
        if request.FILES['image'] and request.POST['summary']:
            j=job()
            j.image=request.FILES['image']
            j.summary=request.POST['summary']
            j.save()
            return redirect('home')
        else:
            return render(request,'create.html',{'error':"no product found"})
    return render(request,'create.html')
def update(request,blog_id):
    d= get_object_or_404(job,pk=blog_id)
    if request.method=="POST":
        if request.FILES['image'] and request.POST['summary']:
            
            d.image=request.FILES['image']
            d.summary=request.POST['summary']
            d.save()
            return redirect('home')
        else:
            return render(request,'update.html')
    else:
        return render(request,'update.html',{'error':"no product found",'update':d})

    return render(request,'update.html',{"update":d})
@login_required(login_url="/signup")
def delete(request,blog_id):
    d=get_object_or_404(job,pk=blog_id)
    d.delete()
    return redirect('home')
def logout(request):
    if request.method=='POST':
        auth.logout(request)
    return redirect('home')
def detail(request,job_id):
    j=get_object_or_404(job,pk=job_id)
    return render(request,'detail.html',{"detail":j})
@login_required(login_url="/signup")
def vote(request,job_id):
    v=get_object_or_404(job,pk=job_id)
    if request.method=='POST':
        v.vote+= 1
        v.save()
    return redirect('home')
def base(request):
    return render(request,'base.html')