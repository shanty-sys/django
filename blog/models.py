from django.db import models

class blog(models.Model):
    image = models.ImageField(upload_to = 'images/')
    summary = models.TextField(max_length = 200)
    title = models.TextField(max_length = 200)
    time = models.DateTimeField()
