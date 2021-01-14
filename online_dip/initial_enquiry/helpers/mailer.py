""" Handles email functionality """

from django.core.mail import send_mail
from django.template.loader import render_to_string


class EmailSender():
    """ Handles the sending of email """

    def __init__(self, customer_data, email_enabled):

        if not email_enabled:
            raise PermissionError("EmailSender is disabled. Enable it with the setting: ENABLE_MAIL in settings.py")

        try:
            self.address = customer_data["email"]
        except KeyError as ex:
            raise KeyError("Recipient email address was not found in the provided data") from ex

        self.message = 'Thank you for your enquiry. A Mortgage Adviser will be in touch in the next few days'
        self.subject = 'Newcastle Building Society - Request for Online Decision in Principle'
        self.html_message = render_to_string('_email.html', customer_data)

    def send(self):
        """ Sends the email """

        send_mail(
            subject=self.subject,
            message=self.message,
            from_email=None,
            recipient_list=[self.address],
            html_message=self.html_message,
            fail_silently=False,
        )

    def __str__(self):
        return f"Sends a confirmation email to: {self.address}"

    def __repr__(self):
        return "EmailSender()"
