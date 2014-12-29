from django.db import models
from django.utils.text import slugify

class Post(models.Model):
    post_title = models.CharField(max_length=200)
    post_body = models.TextField()
    publish_date = models.DateField('Date Published', auto_now_add=True)
    edit_date = models.DateField('Last Edited', auto_now=True)
    post_slug = models.SlugField(blank=True)
    category = models.ForeignKey('blog.category')

    def __unicode__(self):
        return self.post_title

    def save(self, *args, **kwargs):
        self.post_slug = slugify(self.post_title)
        super(Post, self).save(*args, **kwargs)


class Category(models.Model):
    title = models.CharField(max_length=200)
