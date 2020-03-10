from django.db import models

class Announcements(models.Model):
    title = models.CharField(max_length = 200)
    date = models.DateTimeField(auto_now_add=True)
    content = models.TextField(max_length= 500)
