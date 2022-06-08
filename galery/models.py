from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Bb(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(null=True, blank=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    # created
    published = models.DateTimeField(auto_now_add=True, db_index=True)
