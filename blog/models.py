from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    entry_title = models.CharField(max_length=50)
    entry_text = models.TextField()
    entry_date = models.DateTimeField(auto_now_add=True)
    entry_pic = models.ImageField(upload_to = 'media/')
    entry_author = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.entry_title

class Comment(models.Model):
    post = models.ForeignKey(Blog,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)