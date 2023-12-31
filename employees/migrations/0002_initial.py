# Generated by Django 4.2.4 on 2023-08-24 06:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tasks', '0001_initial'),
        ('departments', '0001_initial'),
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='workinprogress',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.task'),
        ),
        migrations.AddField(
            model_name='salary',
            name='employee',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='employees.employee'),
        ),
        migrations.AddField(
            model_name='employee',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='departments.department'),
        ),
        migrations.AddField(
            model_name='employee',
            name='manager',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='employees.employee'),
        ),
    ]
