from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Department
from django.urls import reverse_lazy

class DepartmentListView(ListView):
    model = Department
    template_name = 'department/department_list.html'
    context_object_name = 'departments'

class DepartmentCreateView(CreateView):
    model = Department
    fields = '__all__'
    template_name = 'department/department_form.html'
    success_url = reverse_lazy('departments:department-list')

class DepartmentUpdateView(UpdateView):
    model = Department
    fields = '__all__'
    template_name = 'department/department_form.html'
    success_url = reverse_lazy('departments:department-list')

class DepartmentDeleteView(DeleteView):
    model = Department
    template_name = 'department/department_confirm_delete.html'
    success_url = reverse_lazy('departments:department-list')

class DepartmentDetailView(DetailView):
    model = Department
    template_name = 'department/department_detail.html'
    context_object_name = 'department'
