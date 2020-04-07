from django import forms
from . import models
from student.models import Student
from coach.models import Coach


class CreateProject(forms.ModelForm):
    project_name = forms.CharField(max_length=100,
                                   widget=forms.TextInput(attrs={
                                       'class': 'form-control',
                                       'placeholder': 'project name'
                                   }))
    project_duration = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'project duration'
        }))
    time_allocated_by_creator = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'placeholder': 'time allocated by creator'

    }))

    creator = forms.ModelChoiceField(queryset=Student.objects.all(), widget=forms.Select(attrs={
        'class': 'form-control',

    }))
    needs = forms.CharField(max_length=500, widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'describe the project needs'
    }))
    description = forms.CharField(max_length=500, widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'description'
    }))
    validity_state = forms.ChoiceField(choices=((True, True), (False, False)), widget=forms.Select(attrs={
        'class': 'form-control',
        'placeholder': 'validity state'
    }))
    supervisor = forms.ModelChoiceField(queryset=Coach.objects.all(), widget=forms.Select(attrs={
        'class': 'form-control'
    }))
    members = forms.ModelMultipleChoiceField(queryset=Student.objects.all(), widget=forms.SelectMultiple(attrs={
        'class': 'form-control'
    }))

    class Meta:
        model = models.Project
        fields = ['project_name', 'project_duration',
                  'time_allocated_by_creator', 'needs',
                  'description', 'validity_state',
                  'creator', 'supervisor', 'members']


