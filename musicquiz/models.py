from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.utils import timezone


class MusicCategory(models.Model):
    title = models.CharField(max_length=50, unique=True)
    description = models.TextField()
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
    picture = models.ImageField(upload_to='profile_images', default="profile_images/default_profile_pic.png")
    category = models.ForeignKey(MusicCategory, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.user.username


class Comment(models.Model):
    category = models.ForeignKey(MusicCategory, blank=False, on_delete=models.CASCADE)
    author = models.ForeignKey(UserProfile, related_name="author", blank=False, on_delete=models.CASCADE)
    body = models.CharField(max_length=300, blank=False)
    date_added = models.DateTimeField(default=timezone.now)
    likes = models.ManyToManyField(UserProfile, related_name="liked_by", null=True)

    def __str__(self):
        return self.body[:20]

