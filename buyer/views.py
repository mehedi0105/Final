from django.shortcuts import render,redirect
from . import serializers, models
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework import status
from seller.models import Proposal
from django.http import HttpResponse
# Create your views here.

User = get_user_model()

class AllCategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset  = models.AddCategory.objects.all()
    serializer_class = serializers.AddCategorySerializer

class RevewViewSet(APIView):
    def post(self, request, format= None):
        serializer = serializers.RevewSerializes(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostJobApiView(APIView):

    def get(self, request, format=None):
        jobs = models.PostJob.objects.all()
        serializer =serializers.JobPostSerializer(jobs, many= True)
        return Response(serializer.data)
    
    def post(self, request, format= None):
        serializer = serializers.JobPostSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    
    
    # propal kaj baki Ace

class GetCategoryNameApiView(APIView):
    def get(self, request, cat_id):
        try:
            category = models.AddCategory.objects.get(id=cat_id)
            serializer = serializers.AddCategorySerializer(category)
            return Response(serializer.data)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

def accept_work(request ,id):
    try:
        requirment = Proposal._default_manager.get(pk=id)
    except(Proposal.DoesNotExist):
        requirment = None
    
    if requirment is not None:
        requirment.is_accepted = True
        requirment.save()
        return redirect("https://final-s1v0.onrender.com/Frontend/buyerDashbord.html")
    else:
        return HttpResponse("Activation link is invalid!", status=status.HTTP_400_BAD_REQUEST)
        


    
