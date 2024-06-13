from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    draft = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
