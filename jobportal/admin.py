from django.contrib import admin
from .models import Company, CompanyAddress, JobInformation


admin.site.register(Company)
admin.site.register(CompanyAddress)
admin.site.register(JobInformation)
