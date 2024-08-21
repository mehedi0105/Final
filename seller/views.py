from django.shortcuts import render,redirect
from rest_framework.views import APIView
from buyer import models
from django.http import Http404
from buyer import serializers
from rest_framework.response import Response
from django.http import HttpResponse
from . import serializers as seller
from .models import Proposal,ProjectRequrment, SubmitedProject
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
    
    def put(self, request, pk, format = None):
        job = self.get_objects(pk=pk)
        serializer = serializers.JobPostSerializer(job, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format = None):
        job = self.get_objects(pk=pk)
        job.delete()
        return Response({'message': 'JobPost deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    

class Proposal_Veiw_set(viewsets.ModelViewSet):
    queryset = Proposal.objects.all()
    serializer_class = seller.ProposalSerializers

class ProposalDelete(APIView):
    def get_objects(self, pk):
        try:
            return Proposal.objects.get(pk = pk)
        except Proposal.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format = None):
        job = self.get_objects(pk=pk)
        serializer = seller.ProposalSerializers(job)
        return Response(serializer.data)
    
    def put(self, request, pk, format = None):
        job = self.get_objects(pk=pk)
        serializer = serializers.JobPostSerializer(job, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format = None):
        job = self.get_objects(pk=pk)
        job.delete()
        return Response({'message': 'Proposal deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        

class Requirmnet_Veiw_set(viewsets.ModelViewSet):
    queryset = ProjectRequrment.objects.all()
    serializer_class = seller.RequirmentSerializers

class Project_Veiw_set(viewsets.ModelViewSet):
    queryset = SubmitedProject.objects.all()
    serializer_class = seller.SubmitedProjectSerializers


def user_requirment(request ,id):
    try:
        requirment = Proposal._default_manager.get(pk=id)
    except(Proposal.DoesNotExist):
        requirment = None
    
    if requirment is not None:
        requirment.submit_reqirment = True
        requirment.save()
        return redirect("https://mehedi0105.github.io/Final-Front/buyerDashbord.html")
    else:
        return HttpResponse("Activation link is invalid!", status=status.HTTP_400_BAD_REQUEST)
    
def is_accepted(request ,id):
    try:
        requirment = Proposal._default_manager.get(pk=id)
    except(Proposal.DoesNotExist):
        requirment = None
    
    if requirment is not None:
        requirment.is_accepted = True
        requirment.save()
        return redirect("https://mehedi0105.github.io/Final-Front/buyerDashbord.html")
    else:
        return HttpResponse("Activation link is invalid!", status=status.HTTP_400_BAD_REQUEST)
    
def submit_project(request ,id):
    try:
        requirment = Proposal._default_manager.get(pk=id)
    except(Proposal.DoesNotExist):
        requirment = None
    
    if requirment is not None:
        requirment.submit_project = True
        requirment.save()
        return redirect("https://mehedi0105.github.io/Final-Front/buyerDashbord.html")
    else:
        return HttpResponse("Activation link is invalid!", status=status.HTTP_400_BAD_REQUEST)