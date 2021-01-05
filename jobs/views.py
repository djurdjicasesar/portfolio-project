from django.shortcuts import render
from .models import Job

def home(request):
    jobs = Job.objects
    return render(request, 'jobs/home.html', {'jobs': jobs})

def resume(request):
    resume = Job.objects
    return render(request, 'jobs/resume.html', {'resume': resume})
