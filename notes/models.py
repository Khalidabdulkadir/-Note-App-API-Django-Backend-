from django.db import models

# Create your models here.
class Notes(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=120)
    describtion = models.TextField()

    def __str__(self):
        return self.name