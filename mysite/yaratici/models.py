from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField


# Create your models here.

class BlogPost(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE )
    title = models.CharField(max_length=255)
    meta_title = models.CharField(max_length=255)
    meta_tags = models.CharField(max_length=255,blank=True)
    photo = models.ImageField(upload_to='blog_img')
    create_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)
    is_Published = models.BooleanField(default=False)
    message = RichTextField(blank=True,null=True)
    slug = models.SlugField()

    def __str__(self):
            return self.title

    def get_absolute_url(self):
        return reverse('yaratici:show_post', kwargs={'slug':self.slug})


