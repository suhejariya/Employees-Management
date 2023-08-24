from django import forms
from .models import Employee
from django.db.models import Q

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        instance = kwargs.get('instance')
        if instance:
            self.fields['manager'].queryset = Employee.objects.exclude(
                Q(pk=instance.pk) | Q(subordinates__in=[instance])
            )
