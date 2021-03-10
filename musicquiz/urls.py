from django.urls import path
from musicquiz import views

app_name = 'musicquiz'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('categories/', views.categories, name='categories'),
    path('quiz/', views.quiz, name='quiz'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('my-account/', views.my_account, name='my-account'),
    path('error/', views.error, name='error'),
]
