from django.db import models
from datetime import datetime

class Stories(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    genre = models.CharField(max_length=50)
    url = models.CharField(max_length = 100,default=1)
    time_of_publish = models.DateTimeField("date Published",default = datetime.now())

    def __str__(self):
        return self.title
