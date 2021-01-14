""" Test file for Thank You page, with selenium """

from django.test import TestCase, tag
from selenium import webdriver

@tag('slow', 'selenium')
class TestJourneyThankYou(TestCase):
    """ Test class to create enquiry using selenium """

    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_direct_access_should_redirect_to_beginning_journey(self):
        """ Direct Access should redirect """

        # Arrange
        user_location = "Your Details"

        # Act
        self.driver.get("http://127.0.0.1:8000/thankyou")

        # Assert
        self.assertTrue (user_location in self.driver.title)
