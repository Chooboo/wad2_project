import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'wad2_project.settings')
import django

django.setup()

from musicquiz.models import MusicCategory, UserProfile, Comment
from django.contrib.auth.models import User


def add_category(title, description, image_name):
    cat = MusicCategory.objects.get_or_create(title=title)[0]
    cat.description = description
    cat.image_name = "/images/category_images/" + image_name
    cat.save()
    return cat


def create_mock_user():
    user = User.objects.get_or_create(username="soyjak123", password="nooo")[0]
    userprofile = UserProfile.objects.get_or_create(user=user)[0]

    return userprofile


def add_comment(category, author, body, likes):
    comment = Comment.objects.create(category=category, author=author)
    comment.body = body
    comment.likes = likes
    comment.save()

    return comment


def populate():
    baby_comments = [
        {'body': 'I hate you all, you ruined my life!',
         'likes': 13},
        {'body': 'goo goo gaa gaa',
         'likes': 33}
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

    userprofile = create_mock_user()
    for category, data in categories.items():
        cat = add_category(category, data['description'], data['image_name'])
        if data.get('comments') is not None:
            for comment in data['comments']:
                print(comment['body'][:10])
                c = add_comment(cat, userprofile, comment['body'], comment['likes'])
                print(c.id)


if __name__ == "__main__":
    populate()
