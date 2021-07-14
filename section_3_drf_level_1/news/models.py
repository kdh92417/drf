from django.db import models

class Journalist(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    biography = models.TextField()
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Article(models.Model):
    author = models.ForeignKey(Journalist,
                               on_delete=models.CASCADE,
                               related_name='articles')
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=200)
    body = models.TextField()
    location = models.CharField(max_length=120)
    publication_date = models.DateField()
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.author} {self.title}"
    

class JobOffer(models.Model):
    company_name = models.CharField(max_length=60)
    job_title    = models.CharField(max_length=60)
    job_description = models.TextField()
    salary = models.IntegerField(blank=True)
    city = models.CharField(max_length=60)
    state = models.CharField(max_length=60)
    created_at = models.DateTimeField(auto_now_add=True)
    available = models.BooleanField()
    
    def __str__(self):
        return f"{self.company_name} {self.job_title}"
