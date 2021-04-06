import os
import re
import tempfile
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from django.contrib.staticfiles import finders
from musicquiz import forms
from django.conf import settings

FAILURE_HEADER = f"{os.linesep}{os.linesep}{os.linesep}==================={os.linesep}TEST FAILURE =({os.linesep}===================={os.linesep}"
FAILURE_FOOTER = f"{os.linesep}"

f"{FAILURE_HEADER} {FAILURE_FOOTER}"


def get_template(path_to_template):
    # helper function to get string representation of template files

    f = open(path_to_template, 'r')
    template_str = ""

    for line in f:
        template_str = f"{template_str}{line}"

    f.close()
    return template_str


def create_super_user_object():
    # helper function to create a super user account

    return User.objects.create_superuser('admin', 'admin@test.com', 'testpassword')


class mediaTests(TestCase):

    def test_does_media_directory_exist(self):
        """
        Tests whether the media directory exists in the correct location.
        Also checks for the presence of cat.jpg.
        """
        self.project_base_dir = os.getcwd()
        self.static_dir = os.path.join(self.project_base_dir, 'static')
        self.media_dir = os.path.join(self.project_base_dir, 'media')

        does_media_dir_exist = os.path.isdir(self.media_dir)
        does_goose_jpg_exist = os.path.isfile(os.path.join(self.media_dir, 'goose.jpg'))
        does_zebra_jpg_exist = os.path.isfile(os.path.join(self.media_dir, 'zebra.jpg'))
        does_vibecat_jpg_exist = os.path.isfile(os.path.join(self.media_dir, 'vibecat.jpg'))

        self.assertTrue(does_media_dir_exist,
                        f"{FAILURE_HEADER}We couldn't find the /media/ directory in the expected location. Make sure it is in your project directory (at the same level as the manage.py module).{FAILURE_FOOTER}")
        self.assertTrue(does_goose_jpg_exist, f"{FAILURE_HEADER}We couldn't find the goose.jpg image in /media/.")
        self.assertTrue(does_goose_jpg_exist, f"{FAILURE_HEADER}We couldn't find the zebra.jpg image in /media/.")
        self.assertTrue(does_goose_jpg_exist, f"{FAILURE_HEADER}We couldn't find the vibecat.jpg image in /media/.")


class IndexPageTests(TestCase):

    def test_index_contains_hello_message(self):
        # Checks for message "Is your music taste out of this world...?"
        response = self.client.get(reverse('musicquiz:index'))
        self.assertIn(b'Is your music taste out of this world...?', response.content)

    def test_index_using_template(self):
        # Insures the correct template has been used to render the page
        response = self.client.get(reverse('musicquiz:index'))
        self.assertTemplateUsed(response, 'musicquiz/index.html')

    def test_index_has_title(self):
        # Checks that the title tag has been used
        response = self.client.get(reverse('musicquiz:index'))
        self.assertIn(b'<title>', response.content)
        self.assertIn(b'</title>', response.content)


class AboutPageTests(TestCase):

    def test_about_contains_create_message(self):
        # Checks for specified message
        response = self.client.get(reverse('musicquiz:about'))
        self.assertIn(b'Here at Digital Planet', response.content)
        self.assertIn(b'Meet the developers!', response.content)
        self.assertIn(b'Want to contact us?', response.content)

    # def test_about_contain_image(self):
    # Check that there is an image on the page
    # response = self.client.get(reverse('musicquiz:about'))
    # self.assertIn(b'img src="/media/', response.content)

    def test_about_using_template(self):
        # Insures the correct template has been used to render the page
        response = self.client.get(reverse('musicquiz:about'))
        self.assertTemplateUsed(response, 'musicquiz/about.html')


class ErrorPageTests(TestCase):
    def test_error_contains_message(self):
        # Checks for message "Is your music taste out of this world...?"
        response = self.client.get(reverse('musicquiz:error'))
        self.assertIn(b'Looks like you pressed the wrong button!', response.content)

    def test_error_using_template(self):
        # Insures the correct template has been used to render the page
        response = self.client.get(reverse('musicquiz:error'))
        self.assertTemplateUsed(response, 'musicquiz/error.html')


class ModelTests(TestCase):

    def setUp(self):
        try:
            from populate_wad import populate
            populate()
        except ImportError:
            print('The module populate_wad does not exist')
        except NameError:
            print('The function populate() does not exist or is not correct')
        except:
            print('Something went wrong in the populate() function :-(')


class FormTests(TestCase):
    # Checks that both UserProfileForm and UserForm are present
    def setUp(self):
        try:
            from forms import UserProfileForm
            from forms import UserForm
        except ImportError:
            print('The module forms does not exist')
        except NameError:
            print('The class PageForm does not exist or is not correct')
        except:
            print('Something else went wrong')

    pass


class Registration_and_Login_Tests(TestCase):
    """
    A series of tests that examine the registration is correct
    """

    def test_new_registration_view_exists(self):
        """
        Checks to see if the new registration view exists in the correct place, with the correct name.
        """
        url = ''

        try:
            url = reverse('registration_register')
        except:
            pass

        self.assertEqual(url, '/accounts/register/',
                         f"{FAILURE_HEADER}Have you created the musicquiz:register URL mapping correctly? It should point to the new register() view{FAILURE_FOOTER}")

    def test_registration_template(self):
        """
        #Does the registration_register.html template exist in the correct place, and does it make use of template inheritance?
        #"""
        template_base_path = os.path.join(settings.TEMPLATE_DIR, 'registration')
        template_path = os.path.join(template_base_path, 'registration_form.html')
        self.assertTrue(os.path.exists(template_path),
                        f"{FAILURE_HEADER}We couldn't find the 'registration_register.html' template in the 'templates/musicquiz/' directory. Did you put it in the right place?{FAILURE_FOOTER}")

        template_str = get_template(template_path)
        full_title_pattern = r'<title>(\s*|\n*)TITLE(\s*|\n*)</title>'
        block_title_pattern = r'{% block title_block %}(\s*|\n*)Register(\s*|\n*){% (endblock|endblock title_block) %}'

        request = self.client.get(reverse('registration_register'))
        content = request.content.decode('utf-8')

        self.assertTrue(re.search(full_title_pattern, content),
                        f"{FAILURE_HEADER}The <title> of the response for 'registration_register' is not correct. Check your register.html template, and try again.{FAILURE_FOOTER}")
        self.assertTrue(re.search(block_title_pattern, template_str),
                        f"{FAILURE_HEADER}Is registration_register.html using template inheritance? Is your <title> block correct?{FAILURE_FOOTER}")

    # def test_bad_registration_post_response(self):
    # """
    # Checks the POST response of the registration view.
    # What if we submit a blank form?
    # """
    # request = self.client.post(reverse('registration_register'))
    # content = request.content.decode('utf-8')

    # self.assertTrue('<ul class="errorlist">' in content)

    def test_new_login_form_is_displayed_correctly(self):
        # Access login page
        response = self.client.get(reverse('auth_login'))
        self.assertIn(b'Login', response.content)

        # Username label and input text
        self.assertIn(b'Username', response.content)

        # Password label and input text
        self.assertIn(b'Password', response.content)

        self.assertIn(b'Sign Up', response.content)

        # Message for not members
        self.assertIn(b'Not registered?', response.content)

    def test_new_registration_form_is_displayed_correctly(self):
        # Access registration page
        response = self.client.get(reverse('registration_register'))
        # Check if form is rendered correctly
        self.assertIn(b'Register Here', response.content)

        # Username label and input text
        self.assertIn(b'Username', response.content)

        # Email label and input email
        self.assertIn(b'E-mail', response.content)

        # Password label and input password
        self.assertIn(b'Password', response.content)

        # Password label and input password
        self.assertIn(b'Password confirmation', response.content)

        # Check submit button
        self.assertIn(b'type="submit"', response.content)

    def test_good_form_creation(self):
        """
        Tests the functionality of the forms.
        Creates a UserProfileForm and UserForm, and attempts to save them.
        Upon completion, we should be able to login with the details supplied.
        """
        user_data = {'username': 'testuser', 'password': 'test123', 'email': 'test@test.com'}
        user_form = forms.UserForm(data=user_data)

        user_profile_data = {'picture': tempfile.NamedTemporaryFile(suffix=".jpg").name}
        user_profile_form = forms.UserProfileForm(data=user_profile_data)

        self.assertTrue(user_form.is_valid(),
                        f"{FAILURE_HEADER}The UserForm was not valid after entering the required data. Check your implementation of UserForm, and try again.{FAILURE_FOOTER}")
        self.assertTrue(user_profile_form.is_valid(),
                        f"{FAILURE_HEADER}The UserProfileForm was not valid after entering the required data. Check your implementation of UserProfileForm, and try again.{FAILURE_FOOTER}")

        user_object = user_form.save()
        user_object.set_password(user_data['password'])
        user_object.save()

        user_profile_object = user_profile_form.save(commit=False)
        user_profile_object.user = user_object
        user_profile_object.save()

        self.assertEqual(len(User.objects.all()), 1,
                         f"{FAILURE_HEADER}We were expecting to see a User object created, but it didn't appear. Check your UserForm implementation, and try again.{FAILURE_FOOTER}")
        # self.assertEqual(len(musicquiz.models.UserProfile.objects.all()), 1, f"{FAILURE_HEADER}We were expecting to see a UserProfile object created, but it didn't appear. Check your UserProfileForm implementation, and try again.{FAILURE_FOOTER}")
        self.assertTrue(self.client.login(username='testuser', password='test123'),
                        f"{FAILURE_HEADER}We couldn't log our sample user in during the tests. Please check your implementation of UserForm and UserProfileForm.{FAILURE_FOOTER}")


class Quiz_Basic_Tests(TestCase):

    def test_quiz_contains_message(self):
        # Checks for message and correct template used
        response = self.client.get(reverse('musicquiz:quiz'))
        self.assertIn(b"Let's see what you're made of!", response.content)


class Category_Basic_Tests(TestCase):

    def test_categories_contains_message(self):
        # Checks for message and correct template used
        response = self.client.get(reverse('musicquiz:categories'))
        self.assertIn(b"How enlightened are you?", response.content)
