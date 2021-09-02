from django.shortcuts import render
from django.http import HttpResponse
from .models import Project

projectsList = [
    {
        'id':"1",
        'title':'Ecommerce Website',
        'description':'Fully functional ecommerce'
    },
    {
        'id':"2",
        'title':'Portofolio wedsite',
        'description':'This is a project where i built out my portofolio'
    },
    {
        'id':"3",
        'title':'Social Network',
        'description':'Awesome open project i am still working'
    }
]

def projects(request):

    projects = Project.objects.all()
   
    context = {
        'projects':projects,
    }
    return render(request, 'projects/projects.html', context)

def project(request, pk):
    
    projectObj = Project.objects.get(id=pk)
    

    return render(request, 'projects/single-project.html', {'project':projectObj,})
