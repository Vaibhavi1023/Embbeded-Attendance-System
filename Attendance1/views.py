from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render,redirect
from app.models  import student
from app.models  import teacher



# def t_details(request):
#     t=''
#     if request.method=="POST":
#         name=request.POST.get('name')
#         email=request.POST.get('email')
#         phno=request.POST.get('phno')
#         DOB=request.POST.get('DOB')
#         gender=request.POST.get('gender')
#         ocuupation=request.POST.get('ocuupation')
#         id_name=request.POST.get('id_name')
#         id_no=request.POST.get('id_no')
#         issue_date=request.POST.get('issue_date')
#         post=request.POST.get('post')
#         branch=request.POST.get('branch')
#         tn=teacher(t_name=name,t_mail=email,t_phno=phno,t_DOB=DOB,t_Gender=gender,t_Occupation=ocuupation,tid_name=id_name,tid_no=id_no,t_issue_date=issue_date,t_post=post,t_branch=branch)
    
#         tn.save()
#         t='Data Inserted'
        
#     return render(request,"Registration1.html",{'t':t})


