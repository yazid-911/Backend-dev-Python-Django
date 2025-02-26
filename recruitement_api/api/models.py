from django.db import models

class Candidate(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255) 
    skills = models.TextField(blank=True)
    def __str__(self):
        return self.name

class Recruiter(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)  
    company_name = models.CharField(max_length=255)
    def __str__(self):
        return self.name
