from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=120)
    describtion = models.TextField()

    def __str__(self):
        return self.name
    
    
class Notes(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='notes')

    def __str__(self):
        return self.title

