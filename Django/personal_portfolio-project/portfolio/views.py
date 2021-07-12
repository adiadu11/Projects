from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Project
# Create your views here.


def home(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/home.html', {'projects': projects})


def detail(request, project_id):
    project = Project.objects.get(pk=project_id)
    return render(request, 'portfolio/detail.html', {'project': project})
