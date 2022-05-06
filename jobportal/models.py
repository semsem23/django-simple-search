from django.db import models
from django.urls import reverse

      

class CompanyAddress(models.Model):
    country         = models.CharField(max_length=60, null=False)
    state           = models.CharField(max_length=60, null=False, blank=True)
    city            = models.CharField(max_length=60, null=False, blank=True)
    zipcode         = models.CharField(max_length=5, null=False, blank=True)
    address         = models.CharField(max_length=100, null=False, blank=True)

    def __str__(self):
        return '{} {} {} {}'.format(self.address, self.city, self.state, self.zipcode) 
        
    
class Company(models.Model):
    name            = models.CharField(max_length=100, null=False)
    activity        = models.CharField(max_length=20, null=False)
    size_choices  = [
      ('Less than 6 employees','less than 6 employees'),
      ('Between 6 and 49 employees','between 6 and 49 employees'),
      ('Between 50 and 199 employees','between 50 and 199 employees'),
      ('More than 200 employees','more than 200 employees'),]
    size            = models.CharField(max_length=100, choices=size_choices)
    infos           = models.TextField(null=False, blank=True)
    website         = models.CharField(max_length=100, null=False, blank=True)
    headquarters    = models.ForeignKey(CompanyAddress, on_delete = models.CASCADE)
    slug            = models.SlugField(unique = True)

    def get_absolute_url(self):
        return reverse('company_detail', kwargs={'slug':self.slug})
        
    def __str__(self):
        return self.name

   

class JobInformation(models.Model):
    title           = models.CharField(max_length=100, null=False)
    description     = models.TextField(null=False, blank=True)
    published_date  = models.DateTimeField(auto_now_add=True)
    salary          = models.CharField(max_length=100, null=False)
    company         = models.ForeignKey(Company, on_delete = models.CASCADE)
    contract_type_choices  = [
      ('Permanent contract','permanent contract'),
      ('Fixed-term contract','fixed-term contract'),]
    contract_type   = models.CharField(max_length=100, choices=contract_type_choices)
    is_published    = models.BooleanField(default=False)
    slug            = models.SlugField(unique = True)

    def get_absolute_url(self):
        return reverse('job_detail', kwargs={'slug':self.slug})
        
    def __str__(self):
        return self.title
        
 