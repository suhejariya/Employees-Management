from django.shortcuts import render
from .forms import EmployeeForm
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView
from .models import *
from django.urls import reverse_lazy

class EmployeeCreateView(CreateView):
    model = Employee
    fields = '__all__'
    template_name = 'employees/employee_form.html'
    success_url = reverse_lazy('employee:employee-list')

class EmployeeDetailView(DetailView):
    model = Employee
    template_name = 'employees/employee_detail.html'

class EmployeeUpdateView(UpdateView):
    model = Employee
    fields = ['name', 'department', 'manager', 'salary']
    template_name = 'employees/employee_form.html'
    success_url = reverse_lazy('employee:employee-list')

class EmployeeDeleteView(DeleteView):
    model = Employee
    template_name = 'employees/employee_confirm_delete.html'
    success_url = reverse_lazy('employee:employee-list')

class EmployeeListView(ListView):
    model = Employee
    template_name = 'employees/employee_list.html'
    context_object_name = 'employees'

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.GET.get('name')
        if name:
            queryset = queryset.filter(name__icontains=name)
        return queryset