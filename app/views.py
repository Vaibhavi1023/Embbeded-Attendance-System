
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth.forms import UserCreationForm
from http.client import HTTPResponse
# Create your views here.
def home(request):
    return render(request,'attendance.html')

def login(request):
    if request.method == 'POST':
       username=request.POST['username']
       password=request.POST['password']
       x=auth.authenticate(username=username,password=password)
       if x is None:
             return redirect('/')   
             print(hi)
       else:
            return render(request,'Registration1.html')
            print(hello)
    else:
        return render(request,'attendance.html')
        print(hii)


def t_details(request):
    t=''
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phno=request.POST.get('phno')
        DOB=request.POST.get('DOB')
        gender=request.POST.get('gender')
        ocuupation=request.POST.get('ocuupation')
        id_name=request.POST.get('id_name')
        id_no=request.POST.get('id_no')
        issue_date=request.POST.get('issue_date')
        post=request.POST.get('post')
        branch=request.POST.get('branch')
        tn=teacher(t_name=name,t_mail=email,t_phno=phno,t_DOB=DOB,t_Gender=gender,t_Occupation=ocuupation,tid_name=id_name,tid_no=id_no,t_issue_date=issue_date,t_post=post,t_branch=branch)
    
        tn.save()
        t='Data Inserted'

        return render(request,"")
        
    return render(request,"Registration1.html",{'t':t})


def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        confirm_password = request.POST['confirm_password']
        user = User.objects.create_user(username,password,email)
        user.save()
        # myuser = User.objects.create_user(username,email,password)
        # myuser.save()
        # user.save()
        print("user created")
        return redirect('t_details')
    else:  
        return render(request,'sign_up.html')