from rest_framework import serializers
from . import models

class AddCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AddCategory
        fields = '__all__'

class JobPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PostJob
        fields = '__all__'

class RevewSerializes(serializers.ModelSerializer):
    class Meta:
        model = models.Reveiw
        fields = '__all__'