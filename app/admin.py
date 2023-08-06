from django.contrib import admin
from .models import student
from .models import teacher
from .models import course


class StudentAdmin(admin.ModelAdmin):
     list_display=('student_name','student_mailid','student_PRN','student_branch','student_year','student_semester','student_phno')

admin.site.register(student,StudentAdmin)


class TeacherAdmin(admin.ModelAdmin):
     list_display=('t_name','t_mail','t_phno','t_Gender','t_DOB','t_Occupation','tid_name','tid_no','t_issue_date','t_branch','t_post')

admin.site.register(teacher,TeacherAdmin)

class CourseAdmin(admin.ModelAdmin):
     list_display=('c_name','c_code','c_semester','c_creadit','c_Teacher')

admin.site.register(course,CourseAdmin)







# Register your models here.
