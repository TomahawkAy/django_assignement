from django import forms
from . import models
from student.models import Student
from project.models import Project


class CreateMembership(forms.ModelForm):
    allocated_time_per_member = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'placeholder': 'time allocated by member'

    }))

    project = forms.ModelChoiceField(queryset=Project.objects.all(), widget=forms.Select(attrs={
        'class': 'form-control',
    }))
    student = forms.ModelChoiceField(queryset=Student.objects.all(), widget=forms.Select(attrs={
        'class': 'form-control',

    }))

    class Meta:
        model = models.MembershipInProject
        fields = ['allocated_time_per_member', 'project',
                  'student']
