from .models import UploadDocument, MetadataKey, MetadataChoice, MetadataUpload
from rest_framework import serializers
import json


class MetadataChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetadataChoice
        fields = ["id", "meta_choice"]


class MetadataKeySerializer(serializers.ModelSerializer):
    metadata_choice = MetadataChoiceSerializer(many=True, read_only=True)

    class Meta:
        model = MetadataKey
        fields = [
            "key_id",
            "metadata_key",
            "metadata_description",
            "metadata_type",
            "metadata_choice"
        ]


class MetadataUploadSerializer(serializers.ModelSerializer):
    meta_key = serializers.CharField(source="meta_key.metadata_key", read_only=True)

    class Meta:
        model = MetadataUpload
        fields = ["meta_key", "meta_upload_value"]


class UploadDocumentDetailSerializer(serializers.ModelSerializer):
    metadata = MetadataUploadSerializer(many=True, read_only=True)

    class Meta:
        model = UploadDocument
        fields = [
            "doc_id",
            "document",
            "document_name",
            "doc_type",
            "status",
            "locked",
            "doc_created_at",
            "doc_updated_on",
            "metadata"
        ]


class UploadDocumentCreateSerializer(serializers.ModelSerializer):
    metadata = serializers.CharField(write_only=True)

    class Meta:
        model = UploadDocument
        fields = [
            "doc_id",
            "document",
            "document_name",
            "doc_type",
            "metadata",
        ]

    def create(self, validated_data):
        request = self.context.get("request")

        # ✅ Convert JSON string to Python list
        try:
            metadata_list = json.loads(validated_data.pop("metadata"))
        except json.JSONDecodeError:
            raise serializers.ValidationError({
                "metadata": "Invalid JSON format"
            })

        document = UploadDocument.objects.create(
            **validated_data,
            doc_created_by=request.user
        )

        for item in metadata_list:
            key_obj, created = MetadataKey.objects.get_or_create(
                metadata_key=item["key"]
            )
            MetadataUpload.objects.create(
                meta_key=key_obj,
                meta_upload_doc=document,
                meta_upload_value=item["value"]
            )

        return document


class MetadataKeyCreateSerializer(serializers.ModelSerializer):
    metadata_choice = serializers.PrimaryKeyRelatedField(
        queryset=MetadataChoice.objects.all(),
        many=True,
        required=False
    )

    class Meta:
        model = MetadataKey
        fields = [
            "metadata_key",
            "metadata_description",
            "metadata_type",
            "metadata_choice"
        ]
