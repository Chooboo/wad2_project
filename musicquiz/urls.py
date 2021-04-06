from django.urls import path
from musicquiz import views

app_name = 'musicquiz'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('quiz/', views.quiz, name='quiz'),
    path('categories/', views.categories, name='categories'),
    path('categories/<slug:category_slug>/', views.show_category, name='category'),
    path('profile/<username>/', views.profile, name='profile'),
    path('logout/', views.user_logout, name='logout'),
    path('register-profile/', views.register_profile, name='register_profile'),
    path('error/', views.error, name='error'),
    # ajax urls
    path('quiz/question/<question_id>/', views.show_question, name='show_question'),
    path('quiz/quizresults/<points>/', views.quiz_results, name='quiz_results'),
    path('categories/<slug:category_slug>/remove-comment/<slug:comment_id>/', views.remove_comment, name='remove_comment'),
    path('categories/<slug:category_slug>/toggle-like/<slug:comment_id>/', views.toggle_like, name='toggle_like'),
]
