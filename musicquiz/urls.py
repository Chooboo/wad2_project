from django.urls import path
from musicquiz import views

app_name = 'musicquiz'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('categories/', views.categories, name='categories'),
    path('category/<slug:category_slug>/', views.show_category, name='category'),
    path('category/<slug:category_slug>/remove-comment/<slug:comment_id>/', views.remove_comment, name='remove_comment'),
    path('category/<slug:category_slug>/toggle-like/<slug:comment_id>/', views.toggle_like, name='toggle_like'),
    path('quiz/', views.quiz, name='quiz'),
    path('quiz/question/<question_id>/', views.show_question, name='show_question'),
    path('quiz/quizresults/<points>/', views.quiz_results, name='quiz_results'),
    path('error/', views.error, name='error'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/<username>/', views.profile, name='profile'),
    path('register_profile/', views.register_profile, name='register_profile'),
]
