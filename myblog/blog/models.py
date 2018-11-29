from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    daetime = models.DateField(u'Дата публикации')
    content = models.TextField(max_length=10000)

    def __str__(self):
        return self.title