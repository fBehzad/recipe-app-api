from django.test import TestCase
from django.contrib.auth import get_user_model


class Model_Test(TestCase):
    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        email = "test@btre.com"
        password = "11111368"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for the user is normalized"""
        email = "testf@BTRE.COM"
        password = "11111368"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating eamil with no email raises an error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "test1234")

    def tests_create_new_supper_user(self):
        """Test creating a new supper user"""
        user = get_user_model().objects.create_supperuser(
            email="testf@BTRE.COM",
            password="11111368"
        )
        self.assertTrue(user.is_supperuser)
        self.assertTrue(user.is_staff)
