from django.db import models

class UploadedFile(models.Model):
    file_name = models.CharField(max_length=255)
    category = models.CharField(max_length=50)
    file = models.FileField(upload_to='uploads/')
    
    def __str__(self):
        return self.file_name
# Create your models here.
