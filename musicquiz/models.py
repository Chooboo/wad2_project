from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.utils import timezone


class MusicCategory(models.Model):
    title = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    user_count = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)
    image_name = models.CharField(max_length=200)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(MusicCategory, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'MusicCategories'

    def __str__(self):
        return self.title


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='profile_images', default="default_profile_pic.png")

    def __str__(self):
        return self.user.username


class Comment(models.Model):
    category = models.ForeignKey(MusicCategory,
                                 on_delete=models.CASCADE,
                                 blank=False)
    author = models.ForeignKey(UserProfile, blank=False, on_delete=models.CASCADE)
    body = models.CharField(max_length=300, blank=False)
    date_added = models.DateTimeField(default=timezone.now)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.body[:20]

