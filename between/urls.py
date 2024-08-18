from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

# router.register(r'register',views.UserRegistrationApiView, basename='register')

urlpatterns = [
    path('', include(router.urls)),
    path('register/', views.UserRegistrationApiView.as_view(), name='register'),
    path('activate/<uid64>/<token>/', views.activate , name='activate'),
    path('getUserName/<int:user_id>/', views.GetUserNameApiView.as_view() , name='getUserName'),
    path('GetAllUser/', views.GetAllUserApiView.as_view() , name='getAllUser'),
    path('Getdetails/<str:username>/', views.GetdetailsApiView.as_view() , name='Getdetails'),
    path('pass_change/', views.ChangePasswordView.as_view() , name='pass_change'),
]