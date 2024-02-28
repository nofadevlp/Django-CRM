from django import forms
from .models import Student


class StudentForm(forms.ModelForm):    
    class Meta:
        model = Student
        fields = ['std_no', 'first_name', 'last_name', 'email', 'field_of_study', 'gpa']
        labels = {
            'std_no' : 'Student Number',
            'first_name' : 'First Name',
            'last_name' : 'Last Name',
            'email' : 'Email',
            'field_of_study' : 'Field of Study',
            'gpa' : 'GPA'
            
        }
        widgets = {
            'std_no' : forms.NumberInput(attrs={'class':'form-control'}),
            'first_name' : forms.TextInput(attrs={'class':'form-control'}),
            'last_name' : forms.TextInput(attrs={'class':'form-control'}),
            'email' : forms.EmailInput(attrs={'class':'form-control'}),
            'field_of_study' : forms.TextInput(attrs={'class':'form-control'}),
            'gpa' : forms.NumberInput(attrs={'class':'form-control'})
            
        }