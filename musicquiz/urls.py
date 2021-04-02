from django.urls import path
from musicquiz import views

app_name = 'musicquiz'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('categories/', views.categories, name='categories'),
    path('category/<slug:category_slug>/', views.category, name='category'),
    path('quiz/', views.quiz, name='quiz'),
    path('error/', views.error, name='error'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/<username>/', views.profile, name='profile'),
    path('register_profile/', views.register_profile, name='register_profile'),
]
