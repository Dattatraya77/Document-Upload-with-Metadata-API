from django.urls import path, include
from rest_framework import  routers
from .views import UploadDocumentViewSet, MetadataKeyViewSet, MetadataChoiceViewSet


router = routers.DefaultRouter()
router.register(r"documents", UploadDocumentViewSet)
router.register(r"metadata-keys", MetadataKeyViewSet)
router.register(r"metadata-choices", MetadataChoiceViewSet)


urlpatterns = [
    path('', include(router.urls))
]