# Generated by Django 3.1.1 on 2020-09-23 09:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_branch_designation_division_employeeinfo_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeeinfo',
            name='users',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.createemployee'),
        ),
    ]
