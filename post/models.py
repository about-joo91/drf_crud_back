from django.db import models

# Create your models here.
class PostModel(models.Model):
    author = models.ForeignKey('user.UserModel' , on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=30)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)