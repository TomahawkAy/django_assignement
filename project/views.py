from django.shortcuts import render, redirect
from project.models import Project
from . import form


# Create your views here.
def read_projects(request):
    if request.method == 'POST':
        data = form.CreateProject(request.POST)
        if data.is_valid():
            print('data saved successfully')
            data.save()
        else:
            print('there were an error occured...')
            print(data.errors)
        return redirect('create')
    else:
        project_form = form.CreateProject()
        return render(request, 'Project/index.html',
                      {'projects': Project.objects.all(),
                       'form': project_form})


def delete_project(request, id):
    project = Project.objects.filter(id=id)
    project.delete()
    return redirect('create')
