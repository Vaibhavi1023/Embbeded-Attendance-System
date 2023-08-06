from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/',admin.site.urls),
    path('',views.home),
    path('login',views.login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('t_details/',views.t_details,name="t_details"),
    # path('signup/',views.signup,name='signup'),


]