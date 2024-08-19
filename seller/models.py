from django.db import models
from buyer.models import PostJob 
from freelance_marketplace import settings
# Create your models here.
class Proposal(models.Model):
    job = models.ForeignKey(PostJob, on_delete=models.CASCADE)
    seller = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    cover_letter = models.TextField()
    submit_reqirment = models.BooleanField(default=False)
    submit_project = models.BooleanField(default=False)
    is_accepted = models.BooleanField(default=False)
    reveiw = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__ (self):
        return self.seller.username
    
class ProjectRequrment(models.Model):
    job = models.ForeignKey(PostJob, on_delete=models.CASCADE)
    buyer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    requirment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)