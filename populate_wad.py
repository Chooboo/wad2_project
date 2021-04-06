import os
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'wad2_project.settings')
import django

django.setup()

from musicquiz.models import MusicCategory, UserProfile, Comment, QuizQuestion
from django.contrib.auth.models import User


def add_category(title, description, image_name):
    cat = MusicCategory.objects.get_or_create(title=title)[0]
    cat.description = description
    cat.image_name = "/images/category_images/" + image_name
    cat.save()
    return cat


def create_mock_users():
    userprofiles = []

    user = User.objects.get_or_create(username="soyjak123", password="nooo")[0]
    userprofile = UserProfile.objects.get_or_create(user=user)[0]
    userprofile.picture = "profile_images/soyjak.jpg"
    userprofile.save()
    userprofiles.append(userprofile)

    user = User.objects.get_or_create(username="chad47", password="xxx")[0]
    userprofile = UserProfile.objects.get_or_create(user=user)[0]
    userprofile.picture = "profile_images/chad.png"
    userprofile.save()
    userprofiles.append(userprofile)

    user = User.objects.get_or_create(username="npc000074652", password="beepboop")[0]
    userprofile = UserProfile.objects.get_or_create(user=user)[0]
    userprofile.picture = "profile_images/npc.jpg"
    userprofile.save()
    userprofiles.append(userprofile)

    return userprofiles


def add_comment(category, author, body, liking_users):
    comment = Comment.objects.create(category=category, author=author)
    comment.body = body
    for i in range(random.randint(0, 3)):
        comment.likes.add(liking_users[i])
    comment.save()

    return comment


def add_question(question_id, text, choice1, choice2, choice3, choice4):
    question, created = QuizQuestion.objects.get_or_create(question_id=question_id)
    if created:
        question.question_text = text
        question.choice_1 = choice1
        question.choice_2 = choice2
        question.choice_3 = choice3
        question.choice_4 = choice4
        question.save()


def populate():
    baby_comments = [
        {'body': 'I hate you all, you ruined my life!'},
        {'body': 'Meow'},
        {'body': 'Beep boop'},
    ]

    categories = {
        'Innocent Baby': {
            'description': "You are like a little baby. I bet you only listen to music on radio.",
            'image_name': 'baby.jpg',
            'comments': baby_comments},

        'The Awakening': {
            'description': "You found out what real music sounds like. You are so excited that you "
                           "constantly need to tell your friends about the new bands you just discovered.",
            'image_name': 'awakening.jpg'},

        'The Child': {
            'description': "You\'re on a good path. But at this point you're just pretending to like the genre "
                           "even though at the bottom of your heart you still know you don't like the music. "
                           "Good luck living in denial but keep it up for long enough and you might actually "
                           "convince yourself you're a fan.",
            'image_name': 'child.jpg'},

        'The Faded Adult': {
            'description': "Your music palate is almost fully evolved. You fail to find joy in other activities"
                           "and spend all your time discovering semi-obscure bands that probably sound crap. "
                           "Wasn't music supposed to be fun though?",
            'image_name': 'adult.jpg'},
    }

    questions = [
        {'text': 'This is question number one.',
         'choice1': 'Yes',
         'choice2': 'No',
         'choice3': 'Maybe',
         'choice4': 'What'},
        {'text': 'This is question number two.',
         'choice1': 'Hello',
         'choice2': 'World',
         'choice3': 'For',
         'choice4': 'Chrissake'},
        {'text': 'This is question number one.',
         'choice1': 'I',
         'choice2': 'Need',
         'choice3': 'More',
         'choice4': 'Coffee'},
    ]

    userprofiles = create_mock_users()
    for category, data in categories.items():
        cat = add_category(category, data['description'], data['image_name'])
        if data.get('comments') is not None:
            for i, comment in enumerate(data['comments']):
                print(comment['body'][:10])
                c = add_comment(cat, userprofiles[i % 3], comment['body'], userprofiles)

    for i, question in enumerate(questions):
        add_question(i + 1, question['text'], question['choice1'], question['choice2'], question['choice3'],
                     question['choice4'])


if __name__ == "__main__":
    populate()
