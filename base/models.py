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
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.first_name + " " + self.content[:10]

    class Meta:
        ordering = ['created']
