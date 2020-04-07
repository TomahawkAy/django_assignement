from django.shortcuts import render, redirect

from project.models import Project
from project_membership import form
from student.models import Student
from .models import MembershipInProject


# Create your views here.
def index(request):
    projects = Project.objects.all()
    if request.method == 'POST':
        data = form.CreateMembership(request.POST)
        if data.is_valid():
            print('data saved successfully')
            data.save()
        else:
            print('there were an error occured...')
            print(data.errors)
        return redirect('memberships-index')
    else:
        membership_form = form.CreateMembership()
        return render(request, 'Project-membership/index.html', {'projects': projects, 'form': membership_form})


def delete_membership(request, project_id, student_id):
    project = Project.objects.get(id=project_id)
    student = Student.objects.get(id=student_id)
    membership = MembershipInProject.objects.get(project=project, student=student)
    membership.delete()
    return redirect('memberships-index')
