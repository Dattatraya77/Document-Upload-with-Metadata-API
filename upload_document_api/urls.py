from django.urls import path, include
from rest_framework import routers
from .views import UploadDocumentViewSet, MetadataKeyViewSet, MetadataChoiceViewSet, MetadataUploadViewSet


router = routers.DefaultRouter()
router.register(r"documents", UploadDocumentViewSet)
router.register(r"metadata-keys", MetadataKeyViewSet)
router.register(r"metadata-choices", MetadataChoiceViewSet)
router.register(r"metadata-uploads", MetadataUploadViewSet)


urlpatterns = [
    path('', include(router.urls))
]