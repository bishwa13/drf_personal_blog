from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils import timezone




class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name






class Post(models.Model):
  title = models.CharField(max_length=255)
  slug = models.SlugField(max_length=300, unique=True)
  author = models.ForeignKey(
    'auth.User',
    on_delete=models.CASCADE,
    )
  content = models.TextField()
  # Additional fields
  excerpt = models.TextField(blank=True, null=True)   
  categories = models.ManyToManyField('Category', related_name='posts', blank=True)  
  tags = models.ManyToManyField('Tag', related_name='posts', blank=True)  
  status = models.CharField(
        max_length=10,
        choices=[('draft', 'Draft'), ('published', 'Published')],
        default='draft'
    )  
  views = models.PositiveIntegerField(default=0)
  created_at = models.DateTimeField(auto_now_add=True) 
  updated_at = models.DateTimeField(auto_now=True)  
  published_at = models.DateTimeField(blank=True, null=True)  
  



def __str__(self):
  return self.title

  
def get_absolute_url(self):
  return reverse("post_detail", kwargs={"pk": self.pk})