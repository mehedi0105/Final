from rest_framework import serializers
from . import models

class ProposalSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Proposal
        fields = '__all__'

class RequirmentSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.ProjectRequrment
        fields = '__all__'

class SubmitedProjectSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.SubmitedProject
        fields = '__all__'