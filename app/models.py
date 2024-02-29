from django.db import models
from django.contrib.auth.models import User

from app.utils import avatar_path, image_path

# Create your models here.
class Author(models.Model):
    username = models.CharField(max_length= 28)
    first_name = models.CharField(max_length = 128)
    last_name = models.CharField(max_length = 128)
    avatar = models.ImageField(upload_to= avatar_path, default ='cobalt1.webp' )
    like_count = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.first_name

class Product(models.Model):
    image = models.ImageField(upload_to=image_path, default ='cobalt1.webp')
    title = models.CharField(max_length = 128)
    author = models.ForeignKey(Author, on_delete = models.CASCADE, related_name = 'products' )
    body = models.TextField()
    bid = models.FloatField()
    owner = models.CharField(max_length = 28)
    owner_username = models.CharField(max_length = 28)
    ends_in = models.TimeField()
    
 

