from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Writer(models.Model):
    name = models.OneToOneField(User, on_delete = models.CASCADE)
    is_editor = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name.username}"

class Article(models.Model):
    
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    status = models.CharField(max_length=50, default='APPROVED')
    
    written_by = models.ForeignKey(Writer, on_delete=models.CASCADE, null=True,related_name="article_writer") 
    
    edited_by = models.ForeignKey(Writer, on_delete=models.CASCADE, null=True, related_name="article_editor")

    def __str__(self):
        return f"{self.id} | {self.title} | {self.written_by} | {self.status}"


