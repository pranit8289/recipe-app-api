from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_sucessful(self):
        """  test creating user with email successfully"""
        email = "test@itachi.com"
        password = "Testpass@123"
        user = get_user_model().objects.create_user(
            email=email, password=password)
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """ test to check that username is normelized """
        email = "test@Domain.Com"
        user = get_user_model().objects.create_user(email, "test123")

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """ test to create user with no email raises error """
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                email=None, password="test123")

    def test_create_nre_superuser(self):
        """ creating new superuser """
        user = get_user_model().objects.create_superuser(
            email="test@dmian.com", password="test123")
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
