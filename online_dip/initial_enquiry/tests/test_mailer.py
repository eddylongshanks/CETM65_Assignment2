""" EmailSender Tests """

from django.test import TestCase, tag
from django.core import mail
from django.conf import settings
from ..helpers.mailer import EmailSender


@tag('fast')
class TestEmailSender(TestCase):
    """ Tests for EmailSender object """

    def setUp(self):
        customer_details_data = {
                'first_name': 'Steve',
                'email': 'steve@example.co.uk',
                'preferred_time_to_contact': 'S',
            }
        self.mailer = EmailSender(customer_details_data, True)

    def tearDown(self):
        self.mailer = None

    def test_email_enabled_is_false_should_raise_permission_error_exception(self):
        """
        Permission Error exception should be raised when attempting
        to create an EmailSender object when email functionality is disabled
        """

        # Arrange
        data = {'first_name': 'testdata'}
        email_enabled = False
        expected_message = "EmailSender is disabled. Enable it with the setting: ENABLE_MAIL in settings.py"

        # Act
        with self.assertRaises(PermissionError) as context:
            disabled_mailer = EmailSender(data, email_enabled)

        # Assert
        self.assertTrue(expected_message in str(context.exception))

    def test_missing_email_address_should_raise_value_error_exception(self):
        """
        Value Error exception should be raised when there is no
        email address contained within the provided data
        """

        # Arrange
        data = {'first_name': 'testdata'}
        expected_message = "Recipient email address was not found in the provided data"

        # Act
        with self.assertRaises(KeyError) as context:
            mailer = EmailSender(data, True)

        # Assert
        self.assertTrue(expected_message in str(context.exception))

    def test_mail_subject_is_correct(self):
        """ Ensures the subject of the mail is correct """

        # Act
        self.mailer.send()

        # Assert
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'Newcastle Building Society - Request for Online Decision in Principle')

    def test_mail_recipient_is_correct(self):
        """ Ensures the recipient of the mail is correct """

        # Arrange
        expected_recipient = ['steve@example.co.uk']

        # Act
        self.mailer.send()

        # Assert
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].to, expected_recipient)

    def test_mail_from_is_correct(self):
        """ Ensures the email originated from the address stored in setting: DEFAULT_FROM_EMAIL """

        # Arrange
        expected_from_address = settings.DEFAULT_FROM_EMAIL

        # Act
        self.mailer.send()

        # Assert
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].from_email, expected_from_address)

    def test__str__is_correct(self):
        """ Ensures the returning __str__ is accurate """

        # Arrange
        data = {
                'first_name': 'Steve',
                'email': 'testemail@test.com',
            }
        expected_response = "Sends a confirmation email to: testemail@test.com"
        mailer = EmailSender(data, True)

        # Act

        self.mailer.send()

        # Assert
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mailer.__str__(), expected_response)
