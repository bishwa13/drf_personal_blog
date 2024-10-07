from django.db import models

# Create your models here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from posts.models import Post  # Assuming you have a Post model


