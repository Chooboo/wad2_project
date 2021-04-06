from django.contrib import admin
from musicquiz.models import UserProfile
from musicquiz.models import MusicCategory
from musicquiz.models import Comment
from musicquiz.models import QuizQuestion

admin.site.register(UserProfile)
admin.site.register(MusicCategory)
admin.site.register(Comment)
admin.site.register(QuizQuestion)
