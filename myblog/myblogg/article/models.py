from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models.signals import pre_save
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.utils.text import slugify
from django.conf import settings


def upload_location(instance, filename):
	file_path = 'blog/{author_id}/{title}-{filename}'.format(
		author_id=str(instance.author.id),
        title=str(instance.title),
        filename=filename
    )
	return file_path

class BlogPost(models.Model):
	title = models.CharField(max_length=50, null=False, blank=False)
	body = models.TextField(max_length=5000, null=False, blank=False)
	image = models.ImageField(upload_to=upload_location, null=True, blank=True)
	date_published = models.DateTimeField(auto_now_add=True, verbose_name="date published")
	date_updated = models.DateTimeField(auto_now=True, verbose_name="date updated")
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	slug = models.SlugField(blank=True, unique=True) # url to blog post
	likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='likes', blank=True)

	def __str__(self):
		return self.title


class Comment(models.Model):
	post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, null=True)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	content = models.TextField(max_length=100)
	time = models.DateTimeField(auto_now_add=True)

	def __str__(self):
	    return '{}'.format(str(self.user.get_username()))


@receiver(post_delete, sender=BlogPost)
def submission_delete(sender, instance, **kwargs):
    instance.image.delete(False)


def pre_save_blog_post_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = slugify(instance.author.username + "-" + instance.title)

pre_save.connect(pre_save_blog_post_receiver, sender=BlogPost)