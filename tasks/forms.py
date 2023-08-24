from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    completion_date = forms.DateTimeField(
        label='Completion Date',
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
        input_formats=['%Y-%m-%dT%H:%M']
    )
    class Meta:
        model = Task
        fields = '__all__'
