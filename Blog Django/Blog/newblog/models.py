from django.db import models

# Create your models here.

class blogEnquiry(models.Model):
    blog_title = models.CharField(max_length = 100)
    blog_text = models.TextField()
    blog_file = models.FileField(upload_to="Blog_images" , max_length = 250 , null=True , default=None)
    