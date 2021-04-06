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
            'description': "You listen to top 40 music and its fine, you are blissfully unaware of anything and "
                           "everything. You are unpretentious, you probably listen to music because, why not? "
                           " Stay that way, listen to Lizzo",
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
        'Transcendence': {
            'description': "You are God incarnate. All your friends desperately try to find an excuse to go "
                           "away from you when you start talking about music.",
            'image_name': 'transcendence.jpg'},
    }

    questions = [
        {'text': "Do you know Anthony Fantano aka theneedledrop?",
         'choice1': "No, who is that",
         'choice2': "Umm, yeah, I have heard of him",
         'choice3': "If he does not approve I won",
         'choice4': "Melon King"},
        {'text': "Do you listen to Billie Eilish and Drake a lot?",
         'choice1': "Yeah! drake is the best rapper alive and Billie's music is so scary",
         'choice2': "No i don't do top 40 ew",
         'choice3': "No? Should I be, are they cool now??",
         'choice4': "Ahah, 01010010010"},
        {'text': "Do you have friends?",
         'choice1': "Yeah, they're the best!",
         'choice2': "Yes, but they're jealous of my music taste",
         'choice3': "Oh, those people, I don't miss them. I DON'T!",
         'choice4': "*proceeds to cry*"},
        {'text': "What's your favourite Radiohead album?",
         'choice1': "What's a radiohead?",
         'choice2': "They are so old school, my fav is the one with that cover art. It's amazing",
         'choice3': "OK computer, greatest album of all times.",
         'choice4': "The second hand CD of Rainbow, that you can only hear in the Croatian black caves at midnight."},
        {'text': "You live with your mom don't you?",
         'choice1': "No, I have a stable job and a high income.",
         'choice2': "Ugn, no, I live in a flat with 30 people",
         'choice3': "Umm, maybe.",
         'choice4': "Yeah, what about it?"},
        {'text': "Do you endlessly search for new music on the Internet?",
         'choice1': "No, that's why we have Spotify playlists",
         'choice2': "I go hard on Spotify",
         'choice3': "That's why I watch Fantano",
         'choice4': "*proceeds to laugh nervously*"},
        {'text': "Death Grips. Opinion?",
         'choice1': "Death what???",
         'choice2': "Sounds like a trash can falling down the stairs.",
         'choice3': "I think I like them.",
         'choice4': "GET GET GET GOT GOT GOT"},
        {'text': "Are you an insomniac?",
         'choice1': "I sleep fine",
         'choice2': "I SLEEP FINE",
         'choice3': "Yeah, that's what sleeping pills are for",
         'choice4': "*drops mug of coffee on the floor, uncontrollably trembling*"},
        {'text': "Opinions on hyperpop?",
         'choice1': "Is that Billie Eilish?",
         'choice2': "That's noise, not real music.",
         'choice3': "I knew about PC Music before they were popular",
         'choice4': "IT'S CHARLI BABY"},
        {'text': "How are you feeling right now?",
         'choice1': "I am fine, thanks for asking",
         'choice2': "I'm greeeat, I feel totally awesome, why do you ask?",
         'choice3': "*bites down all their nails*",
         'choice4': "BLEP BLAP BLOP"},
    ]

    userprofiles = create_mock_users()
    for category, data in categories.items():
        cat = add_category(category, data['description'], data['image_name'])
        if data.get('comments') is not None:
            for i, comment in enumerate(data['comments']):
                print(comment['body'][:10])
                c = add_comment(cat, userprofiles[i % 3], comment['body'], userprofiles)

    for i, question in enumerate(questions):
        add_question(i + 1, str(i + 1) + ". " + question['text'],
                     question['choice1'], question['choice2'], question['choice3'],  question['choice4'])


if __name__ == "__main__":
    populate()
