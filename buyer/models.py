from django.db import models
from . import constraints
from freelance_marketplace import settings
 
# Create your models here.

class AddCategory(models.Model):
    cat_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, blank=True, null=True,unique=True)

    def __str__(self):
        return self.cat_name


class PostJob(models.Model):
    tittle = models.CharField(max_length=100)
    location = models.CharField(max_length=100,choices=constraints.LOCATION)
    type = models.CharField(max_length=100,choices=constraints.TYPE)
    salary = models.DecimalField(max_digits=12, decimal_places=2)
    category = models.ManyToManyField(AddCategory)
    company = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    description = models.TextField()


    def __str__(self):
        return self.tittle

class Reveiw(models.Model):
    project = models.ForeignKey(PostJob, on_delete=models.CASCADE)
    worker = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    rating = models.CharField(max_length=100 ,choices=constraints.RATING)
    reveiw_text = models.TextField()

    def __str__(self):
        return self.project.tittle