from django.db import models
from django.conf import settings

class Post(models.Model):
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    
    image = models.ImageField(upload_to='posts/')
    
    caption = models.TextField(blank=True)
    
    created_at = models.DateTimeField(auto_now_add = True)
    
    updated_at = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return f"{self.user.username} - {self.caption[:30]}"