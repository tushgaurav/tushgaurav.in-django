from django.db import models

class Suggestion(models.Model):
    name = models.CharField(max_length=255)
    message = models.TextField()
    email = models.EmailField()
    mobile = models.CharField(max_length=10, default=models.SET_NULL)

    def __str__(self):
        return self.name + "_" + self.message[:10]


class Quote(models.Model):
    text = models.TextField()
    category = models.CharField(max_length=30)

    def __str__(self):
        return self.category[:8].upper() + " " + self.text[:10]