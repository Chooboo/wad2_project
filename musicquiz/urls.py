from django.urls import path
from musicquiz import views

app_name = 'musicquiz'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('categories/', views.categories, name='categories'),
    path('quiz/', views.quiz, name='quiz'),
    path('error/', views.error, name='error'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('my_account/', views.my_account, name='my_account'),
]
