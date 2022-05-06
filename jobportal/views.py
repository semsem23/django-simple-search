from django.shortcuts import render, get_object_or_404, redirect
from .models import Company, CompanyAddress, JobInformation
from django.db.models import Q
from django.contrib import messages


def index(request): 
    
    context = {}
    return render(request, 'index.html', context)

def job_list(request): 
    jobs = JobInformation.objects.all()
    
    context = {'jobs': jobs}
    return render(request, 'job_list.html', context)
    
    
def search_results(request): 
    if request.method == "GET":  
        query = request.GET['q']
        
        if not query:
            messages.error(request, 'Please refine your search query...')
            return redirect('index')
        
        jobs = JobInformation.objects.filter(title__contains=query) 
    
    context = {'jobs': jobs, 'query': query}
    return render(request, 'search_results.html', context)  


def job_detail(request, slug):
    jobs = get_object_or_404(JobInformation, slug=slug)
    
    context = {'jobs': jobs}
    return render(request, 'job_detail.html', context)
    
    
def company_detail(request, slug):
    comp = get_object_or_404(Company, slug=slug)
    
    context = {'comp': comp}
    return render(request, 'company_detail.html', context)
    
    