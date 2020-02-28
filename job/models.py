from django.db import models

 #Create your models here.
class job(models.Model):
    image = models.ImageField(upload_to = 'images/')
    summary = models.TextField(max_length = 200)
    vote = models.IntegerField(default=0)

    def __str__(self):
        return self.summary[0:2]

    def summary(self):
        return self.summary[0:3]


