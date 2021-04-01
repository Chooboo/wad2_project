import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'wad2_project.settings')
import django
django.setup()

from musicquiz.models import MusicCategory


def add_category(title, description, image_name):
    cat = MusicCategory.objects.get_or_create(title=title)[0]
    cat.description = description
    cat.image_name = "/category_images/" + image_name
    cat.save()
    return cat


def add_comment():
    pass


def populate():
    categories = {
        'Innocent Baby': {
                 'description': '',
                 'image_name': 'baby.jpg'},
        'The Awakening': {
                 'description': '',
                 'image_name': 'awakening.jpg'},
        'The Child': {
                 'description': '',
                 'image_name': 'child.jpg'},
        'The Faded Adult': {
                 'description': '',
                 'image_name': 'adult.jpg'},
        'Transcendence': {
                 'description': '',
                 'image_name': 'transcendence.jpg'},
    }
    for category, data in categories.items():
        cat = add_category(category, data['description'], data['image_name'])


if __name__ == "__main__":
    populate()
