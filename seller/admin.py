from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Proposal);
admin.site.register(models.ProjectRequrment);
admin.site.register(models.SubmitedProject);