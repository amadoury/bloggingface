from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    content = models.TextField()
    pub_date = models.DateTimeField()
    img = models.CharField(max_length=300, default="")

    def __str__(self):
        return self.title