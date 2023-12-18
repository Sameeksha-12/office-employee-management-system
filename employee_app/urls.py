from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index , name = 'index'),
    path('all_emp', views.all_emp , name = 'all_emp'),
    path('add_emp', views.add_emp , name = 'add_emp'),
    path('delete_emp', views.delete_emp , name = 'delete_emp'),
    path('delete_emp/<int:emp_id>', views.delete_emp , name = 'delete_emp'),
    path('search_emp', views.search_emp , name = 'search_emp'),
]