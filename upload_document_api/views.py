from rest_framework import viewsets, permissions
from .models import UploadDocument, MetadataKey, MetadataChoice, MetadataUpload
from .serializers import (
    UploadDocumentCreateSerializer,
    UploadDocumentDetailSerializer,
    MetadataKeySerializer,
    MetadataChoiceSerializer,
    MetadataKeyCreateSerializer,
    MetadataUploadSerializer,
)
from rest_framework.decorators import action
from rest_framework.response import Response


class MetadataChoiceViewSet(viewsets.ModelViewSet):
    queryset = MetadataChoice.objects.all()
    serializer_class = MetadataChoiceSerializer
    permission_classes = [permissions.IsAuthenticated]


class UploadDocumentViewSet(viewsets.ModelViewSet):
    queryset = UploadDocument.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.action == "create":
            return UploadDocumentCreateSerializer
        return UploadDocumentDetailSerializer


class MetadataKeyViewSet(viewsets.ModelViewSet):
    queryset = MetadataKey.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update"]:
            return MetadataKeyCreateSerializer
        return MetadataKeySerializer


class MetadataUploadViewSet(viewsets.ModelViewSet):
    queryset = MetadataUpload.objects.all()
    serializer_class = MetadataUploadSerializer
    permission_classes = [permissions.IsAuthenticated]