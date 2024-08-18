from django.shortcuts import render,redirect
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

# Create your views here.

User = get_user_model()

class UserRegistrationApiView(APIView):
    serializer_class = serializers.RegistrationSerializer

    def post(self, request):
        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            user = serializer.save()
            user.is_active = False
            user.save()
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            confirm_link = f"https://final-s1v0.onrender.com/activate/{uid}/{token}/"
            name = f"Hello {user.first_name}"
            email_subject = "Verify Your Email Address - Complete Your Registration"
            email_body = render_to_string('./register_email.html',{'confirm_link':confirm_link, 'name':name})
            email = EmailMultiAlternatives(email_subject,'',to=[user.email])
            email.attach_alternative(email_body,'text/html')
            email.send()
            return Response("Check your mail for confirmation")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def activate(request ,uid64, token):
    try:
        uid = urlsafe_base64_decode(uid64).decode()
        user = User._default_manager.get(pk=uid)
    except(User.DoesNotExist):
        user = None
    
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect("https://final-s1v0.onrender.com/Frontend/login.html")
    else:
        return HttpResponse("Activation link is invalid!", status=status.HTTP_400_BAD_REQUEST)


class GetUserNameApiView(APIView):
    def get(self, request, user_id):
        try:
            user = User.objects.get(id=user_id)
            serializer = serializers.GetUserNameSerialzers(user)
            return Response(serializer.data)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        
class GetdetailsApiView(APIView):
    def get(self, request, username):
        try:
            user = User.objects.get(username=username)
            serializer = serializers.GetUserNameSerialzers(user)
            return Response(serializer.data)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        

class GetAllUserApiView(APIView):
    def get(self, request):
        try:
            user = User.objects.all()
            serializer = serializers.GetUserNameSerialzers(user, many= True)
            return Response(serializer.data)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        
        

class ChangePasswordView(APIView):

    def post(self, request, format=None):
        serializer = serializers.PasswordChangeSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({"detail": "Password updated successfully."}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    



