from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    
    def __str__(self):
        return self.user.username


class QuizPage(models.Model):
    quiz = models.OneToOneField(Quiz, on_delete=models.CASCADE)
    question = models.CharField(max_Length=100)
    answer = models.CharField(max_Length=100)
    option_one = models.CharField(max_Length=100)
    option_two = models.CharField(max_Length=100)
    option_three = models.CharField(max_Length=100)
    option_four = models.CharField(max_Length=100)

    def __str__(self):
        return self.quiz