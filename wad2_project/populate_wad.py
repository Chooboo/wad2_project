import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'wad2_project.settings.')

import django
django.setup()

from musicquiz.models import QuizPage

def add_data(data1, data2):
    dt, created = QuizPage.objects.get_or_create(data1=data1, data2=data2)
    print("- Data:{0}, Created: {1}".format(str(dt), str(created)))
    return dt


def populate():
    for row in data:
        data1 = row[0]
        data2 = row[1]
        add_data(data1, data2)


if __name__ == "__main__":
    populate()
