from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class CreateEmployee(models.Model):
    users = models.OneToOneField(User, on_delete=models.SET_NULL, blank=True, null=True)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    re_password = models.CharField(max_length=30)

    def __str__(self):
        return self.username


class Designation(models.Model):
    designation = models.CharField(max_length=30)
    def __str__(self):
        return self.designation

class Branch(models.Model):
    branch = models.CharField(max_length=30)
    def __str__(self):
        return self.branch

class Division(models.Model):
    division = models.CharField(max_length=30)
    branch = models.ForeignKey(Branch, on_delete=models.SET_NULL, blank=True, null=True)
    def __str__(self):
        return self.division

class Title(models.Model):
    title = models.TextField()
    def __str__(self):
        return self.title

class EmployeeInfo(models.Model):
    users = models.OneToOneField(CreateEmployee, on_delete=models.SET_NULL, blank=True, null=True)
    employee_id = models.IntegerField(unique=True,null=False)
    full_name = models.CharField(max_length=50)
    designation = models.ForeignKey(Designation, on_delete=models.SET_NULL, blank=True, null=True)
    branch_division = models.ForeignKey(Division, on_delete=models.SET_NULL, blank=True, null=True)
    title = models.ForeignKey(Title, on_delete=models.SET_NULL, blank=True, null=True)
    def __str__(self):
        return self.full_name


