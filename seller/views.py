from django.shortcuts import render,redirect
from rest_framework.views import APIView
from buyer import models
from django.http import Http404
from buyer import serializers
from rest_framework.response import Response
from django.http import HttpResponse
from . import serializers as seller
from .models import Proposal,ProjectRequrment
from rest_framework import viewsets
from django.contrib.auth import get_user_model
from rest_framework import status
# Create your views here.
User = get_user_model()

# Create your views here.
class categorySlugApiView(APIView):
    def get_object(self, slug):
        try: 
            return models.AddCategory.objects.get(slug = slug);
        except models.AddCategory.DoesNotExist:
            raise Http404
    
    def get(self, request, category_slug = None, format = None):
        category = self.get_object(category_slug)
        jobs = models.PostJob.objects.filter(category = category)
        job_serializer = serializers.JobPostSerializer(jobs, many=True)

        return Response(job_serializer.data)
    
class JOB_DETAILS_API_VIEW(APIView):

    def get_objects(self, pk):
        try:
            return models.PostJob.objects.get(pk = pk)
        except models.PostJob.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format = None):
        job = self.get_objects(pk=pk)
        serializer = serializers.JobPostSerializer(job)
        return Response(serializer.data)
    

class Proposal_Veiw_set(viewsets.ModelViewSet):
    queryset = Proposal.objects.all()
    serializer_class = seller.ProposalSerializers

class Requirmnet_Veiw_set(viewsets.ModelViewSet):
    queryset = ProjectRequrment.objects.all()
    serializer_class = seller.RequirmentSerializers


def user_requirment(request ,id):
    try:
        requirment = Proposal._default_manager.get(pk=id)
    except(Proposal.DoesNotExist):
        requirment = None
    
    if requirment is not None:
        requirment.submit_reqirment = True
        requirment.save()
        return redirect("http://127.0.0.1:5500/Frontend/sellerDashboard.html")
    else:
        return HttpResponse("Activation link is invalid!", status=status.HTTP_400_BAD_REQUEST)