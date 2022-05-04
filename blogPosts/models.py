from django.db import models

# Create your models here.

class BlogPosts(models.Model):

    title = models.CharField(max_length=200) # verbose_name yazmaq olar
    description = models.TextField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    author = models.TextField(max_length=100)
    photo = models.ImageField(upload_to='images/blog/%y/%m/%d')



    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Postlar'
        ordering = ['-created_at']
