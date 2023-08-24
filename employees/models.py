from django.db import models
from django.core.exceptions import ValidationError

def validate_pdf_extension(value):
    if not value.name.endswith('.pdf'):
        raise ValidationError('Only PDF files are allowed.')

class Employee(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey('departments.Department', on_delete=models.CASCADE)
    identification_document = models.FileField(upload_to='identification_docs/', validators=[validate_pdf_extension])
    manager = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

    def clean(self):
        if self.manager == self:
            raise ValidationError("An employee cannot be their own manager.")




