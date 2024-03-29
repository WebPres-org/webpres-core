
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date
from django.db.models.base import Model
from django.db.models.signals import pre_save
from blog.utils import unique_slug_generator
from tinymce.models import HTMLField

STATUS = (
    (0,"Draft"),
    (1,"Publish"),
)



class PostComment(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.sender.get_username()}'

class Categories(models.Model):
    categoryname = models.CharField(max_length=255)

    def __str__(self):
        return self.categoryname

class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255, default='Blog Post')
    slug = models.SlugField(max_length=255, null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='images', null=True)
    body = HTMLField('Content')
    comments = models.ManyToManyField(PostComment, blank=True)
    post_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Categories, null=True, on_delete=models.PROTECT, related_name='category_set')

    def __str__(self):
        return self.title + ' | ' + str(self.author)

def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(slug_generator, sender=Post)