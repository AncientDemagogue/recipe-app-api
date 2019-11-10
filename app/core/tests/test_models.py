from django.test import TestCase
from django.contrib.auth import get_user_model
from core import models


def sample_user(email='test@demagogue.com', password='kolikoje'):
    """create a sample user"""
    return get_user_model().objects.create_user(email,password)


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """test creating a new user with an email is successful"""
        email = 'domagojbakota@gmail.com'
        password = 'kolikoje'
        user = get_user_model().objects.create_user(
            email = email,
            password = password
        ) 

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_meail_normalize(self):
        """test the email for a new user is normalized"""
        email = "test@DEMAGOGUE.com"
        user = get_user_model().objects.create_user(email, 'kolikoje')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """test creating user wit no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_new_superuser(self):
        """ test creating a new superuser """
        user = get_user_model().objects.create_superuser(
            'test@demagogue.com',
            'kolikoje'
            )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
        
    def test_tag_str(self):
        """test the tag string representation"""
        tag = models.Tag.objects.create(
            user = sample_user(),
            name='Vegan'
        )

        self.assertEqual(str(tag), tag.name)
