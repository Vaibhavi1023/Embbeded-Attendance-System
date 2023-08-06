from django.db import models

# Create your models here.
class student(models.Model):
    student_name=models.CharField(max_length=50,null=True)
    student_mailid=models.EmailField(max_length=254,null=True)
    student_PRN=models.CharField(max_length=50,null=True)
    student_branch=models.CharField(max_length=30,null=True)
    student_year=models.CharField(max_length=30,null=True)
    student_semester=models.CharField(max_length=30,null=True)
    student_phno=models.CharField(max_length=30,null=True)

class teacher(models.Model):
    t_name=models.CharField(max_length=50,null=True)
    t_mail=models.EmailField(max_length=254,null=True)
    t_phno=models.CharField(max_length=30,null=True)
    t_Gender=models.CharField(max_length=50,null=True)
    t_Occupation=models.CharField(max_length=50,null=True)
    t_branch=models.CharField(max_length=50,null=True)
    t_post=models.CharField(max_length=50,null=True)
    t_DOB=models.DateField(max_length=50,null=True)
    tid_name=models.CharField(max_length=50,null=True)
    tid_no=models.CharField(max_length=50,null=True)
    t_issue_date=models.DateField(max_length=50,null=True)

class course(models.Model):
    c_code=models.CharField(max_length=50,null=True)
    c_name=models.CharField(max_length=50,null=True)
    c_semester=models.CharField(max_length=30,null=True)
    c_creadit=models.CharField(max_length=30,null=True)
    c_Teacher=models.CharField(max_length=30,null=True)

