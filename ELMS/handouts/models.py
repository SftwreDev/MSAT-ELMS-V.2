from django.db import models


class Handouts(models.Model):
    
    name = models.CharField(max_length=100)
    documents = models.FileField(upload_to='handouts')
    description = models.CharField(max_length=200)
    uploaded_at = models.DateTimeField(auto_now_add=True)
