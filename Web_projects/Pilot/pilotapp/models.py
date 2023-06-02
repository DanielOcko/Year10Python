from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length = 100)
    authorid = models.CharField(max_length = 100)
    creationdate = models.DateField()
    topic = models.CharField(max_length = 20)
    text = models.TextField()
    def __str__(self):
        return self.title
