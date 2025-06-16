from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()

    def __str__(self):
        return self.title
    

class Article(models.Model):
    title = models.CharField(max_length=250)
    summary = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title
    
    