from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'apply_job', views.Proposal_Veiw_set, basename="categorylist")
router.register(r'project_requirment', views.Requirmnet_Veiw_set, basename="project_requirment")
urlpatterns = [
    path('category_slug/<str:category_slug>/', views.categorySlugApiView.as_view(), name="category-slug"),
    path('jobDetails/<int:pk>/', views.JOB_DETAILS_API_VIEW.as_view(), name="jobDetails"),
    path('user_requirment1/<int:id>/', views.user_requirment, name="user_requirment1"),
    path('', include(router.urls)),
]


