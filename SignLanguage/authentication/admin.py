from django.contrib import admin

# Register your models here.
from authentication.models import UploadedFile
# from authentication.models import
admin.site.register(UploadedFile)