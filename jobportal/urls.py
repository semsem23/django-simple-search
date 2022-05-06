"""search URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .import views 

urlpatterns = [
    path('', views.index, name ='index'),
    path('search_results/', views.search_results, name ='search_results'),
    path('company/<slug:slug>/', views.company_detail, name ='company_detail'),
    path('job_list/', views.job_list, name ='job_list'),
    path('<slug:slug>/', views.job_detail, name ='job_detail'),

    

]
