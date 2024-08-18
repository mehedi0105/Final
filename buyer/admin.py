from django.contrib import admin
from . import models
# Register your models here.

class category_admin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('cat_name',)}

admin.site.register(models.AddCategory, category_admin)
admin.site.register(models.PostJob)
admin.site.register(models.Reveiw)
