from django.db import models
from django.contrib.auth.models import User

class Suggestion(models.Model):
    name = models.CharField(max_length=255)
    message = models.TextField()
    email = models.EmailField()
    mobile = models.CharField(max_length=10, default=models.SET_NULL)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name + "_" + self.message[:10]
        
    class Meta:
        ordering = ['name', 'created']


class Quote(models.Model):
    text = models.TextField()
    category = models.CharField(max_length=30)

    def __str__(self):
        return self.category[:8].upper() + " " + self.text[:10]

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    contact_number = models.CharField(max_length=15)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.first_name + " " + self.content[:10]

    class Meta:
        ordering = ['created']

STATUS = ((0, "Draft"), (1, "Published"))
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title