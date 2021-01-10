""" Handles email functionality """

from django.core.mail import send_mail
from django.conf import settings

class EmailSender():
    """ Handles the sending of email """

    def __init__(self, address):
        self.address = address
        self.message = 'Thank you for your enquiry. A Mortgage Adviser will be in touch in the next few days'
        self.subject = 'Newcastle Building Society - Request for Online Decision in Principle'

    def send(self):
        """ Sends the email """

        send_mail(
            self.subject,
            self.message,
            settings.EMAIL_FROM,
            [self.address],
            fail_silently=False,
        )

    def __str__(self):
        return f"Sends a confirmation email to: {self.address}"

    def __repr__(self):
        return "EmailSender()"
