from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'categories', views.AllCategoryViewSet, basename="categorylist")
# router.register(r'reviw', views.RevewViewSet, basename="reviw")


urlpatterns = [
    path('', include(router.urls)),
    path('postJob/',views.PostJobApiView.as_view(), name='postJob'),
    path('categoriy/<int:cat_id>/',views.GetCategoryNameApiView.as_view(), name='categoryname'),
    path('accept_work/<int:id>/', views.accept_work, name="accept_work"),
    path('reviw/', views.RevewViewSet.as_view(), name="accept_work"),
]
