""" EnquiryProvider Tests """

from django.test import TestCase, tag
from django.core import mail
from django.conf import settings
from ..helpers.mailer import EmailSender


@tag('mailer_tests')
class TestEmailSender(TestCase):
    """ Tests for EmailSender object """

    def setUp(self):
        customer_details_data = {
                'first_name': 'Steve',
                'email': 'steve@example.co.uk',
                'preferred_time_to_contact': 'S',
            }
        self.mailer = EmailSender(customer_details_data)

    def tearDown(self):
        customer_details_data = None
        self.mailer = None

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
