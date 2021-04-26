from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from appfirst import views



urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('portfolio/', views.about, name='portfolio'),
    path('employees/', views.EmployeeList.as_view(), name='getallEmployees'),
    path('contact/', views.contact, name='contact'),
    path('employees/<int:pk>', views.getEmployee, name='getEmployee'),
    path('employees/update/<int:pk>', views.updateEmployee, name = 'updateEmployee'),
    path('employees/delete/<int:pk>', views.deleteEmployee, name = 'deleteEmployee'),
    path('employees/create', views.postEmployee, name='createEmployee'),


]