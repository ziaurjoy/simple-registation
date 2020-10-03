from django import forms

from users.models import CreateEmployee, EmployeeInfo


class CreateUserForm(forms.ModelForm):
    class Meta:
        model = CreateEmployee
        fields = ('username','password','re_password')
        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control','placeholder': 'Username .....'}),
            'password':forms.PasswordInput(attrs={'class':'form-control','placeholder': 'Password ...'}),
            're_password':forms.PasswordInput(attrs={'class':'form-control','placeholder': 'Re Password ...'})
        }

class CreateEmployeeForm(forms.ModelForm):
    class Meta:
        model = EmployeeInfo
        fields = ('employee_id','full_name','designation','branch_division','title')
        widgets = {
            'employee_id': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Employee ID .....'}),
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name .....'}),
            'designation': forms.Select(attrs={'class': 'form-control'}),
            'branch_division': forms.Select(attrs={'class': 'form-control'}),
            'title': forms.Select(attrs={'class': 'form-control'}),
        }

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username ...'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password ...'}))