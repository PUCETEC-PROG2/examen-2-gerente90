from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=30, null=False)
    genre = models.CharField(max_length=30, null=False)
    name = models.CharField(max_length=30, null=False)
    year = models.IntegerField(null= False, default=2000)
    Synopsis = models.TextField(max_length=300, null=False)

    def __str__(self) -> str:
        return self.name
