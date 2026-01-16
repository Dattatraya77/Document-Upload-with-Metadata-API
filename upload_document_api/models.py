from django.db import models
from django.contrib.auth.models import User, Group


FILE_STATUS = (
    ('ac', 'Active'),
    ('ia', 'Inactive'),
    ('de', 'Deleted')
)


DOC_TYPE = (
    ('docx', 'docx'),
    ('pdf', 'pdf'),
    ('xlsx', 'xlsx'),
    ('html', 'html')
)


class UploadDocument(models.Model):
    doc_id = models.CharField(max_length=64, primary_key=True, unique=True, verbose_name='Upload Document ID')
    document = models.FileField(upload_to="uploads/", verbose_name='Document', max_length=200,
                                null=True, blank=True)
    document_name = models.CharField(max_length=200, verbose_name='Document name', null=True, blank=True)
    doc_created_at = models.DateTimeField(auto_now_add=True)
    doc_created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE,
                                       verbose_name='Owner', related_name='created_by')
    status = models.CharField(
        max_length=2,
        choices=FILE_STATUS,
        default='ac'
    )
    doc_group = models.ManyToManyField(Group, blank=True)
    locked = models.BooleanField(default=False)
    notification_list = models.ManyToManyField(User, blank=True)
    doc_type = models.CharField(
        max_length=20,
        choices=DOC_TYPE,
        default='pdf'
    )
    doc_updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.doc_id


class MetadataChoice(models.Model):
    meta_choice = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return self.meta_choice


METADATA_TYPE = (
    ('string', 'String'),
    ('integer', 'Integer'),
    ('date', 'Date'),
    ('bool', 'Boolean'),
    ('choice', 'Choice'),
    ('textarea', 'TextArea'),
    ('image', 'Image'),
    ('signature', 'Signature'),
)


class MetadataKey(models.Model):
    key_id = models.AutoField(primary_key=True)
    metadata_key = models.CharField(max_length=100, unique=True)
    metadata_description = models.CharField(max_length=200, blank=True)
    metadata_type = models.CharField(max_length=10, choices=METADATA_TYPE)
    metadata_choice = models.ManyToManyField(MetadataChoice, blank=True)

    def __str__(self):
        return self.metadata_key


class MetadataUpload(models.Model):
    meta_upload_id = models.AutoField(primary_key=True)
    meta_upload_value = models.CharField(max_length=1000)
    meta_key = models.ForeignKey(MetadataKey, on_delete=models.CASCADE)
    meta_upload_doc = models.ForeignKey(UploadDocument, on_delete=models.CASCADE, related_name="metadata")

    def __str__(self):
        return self.meta_upload_value
