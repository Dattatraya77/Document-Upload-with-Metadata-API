from django.contrib import admin
from .models import *

admin.site.register(UploadDocument)
admin.site.register(MetadataUpload)
admin.site.register(MetadataKey)
admin.site.register(MetadataChoice)
