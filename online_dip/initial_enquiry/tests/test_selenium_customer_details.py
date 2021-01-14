""" Test file for Customer Details journey, with selenium """

from django.test import TestCase, tag
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

@tag('slow', 'selenium')
class TestJourneyCustomerDetails(TestCase):
    """ Test class to test Customer Details """

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.address = "http://127.0.0.1:8000/yourdetails"

    def tearDown(self):
        self.driver.quit()

    def test_first_name_empty_should_show_validation_error(self):
        """ Missing First Name Validation """

        # Arrange
        validation_message = "First Name is required"

        # Act
        self.driver.get(self.address)
        self.assertIn("Your Details", self.driver.title)

        last_name_field = self.driver.find_element_by_id("id_last_name")
        last_name_field.send_keys("test_last_name")
        address_building_field = self.driver.find_element_by_id("id_building")
        address_building_field.send_keys("test_address_building")
        address_street_field = self.driver.find_element_by_id("id_street")
        address_street_field.send_keys("test_address_street")
        address_town_field = self.driver.find_element_by_id("id_town")
        address_town_field.send_keys("test_address_town")
        address_county_field = self.driver.find_element_by_id("id_county")
        address_county_field.send_keys("test_address_county")
        address_postcode_field = self.driver.find_element_by_id("id_postcode")
        address_postcode_field.send_keys("postcode")
        telephone_number_field = self.driver.find_element_by_id("id_telephone_number")
        telephone_number_field.send_keys("123")
        email_field = self.driver.find_element_by_id("id_email")
        email_field.send_keys("test_email@email.com")
        preferred_time_to_call_field = self.driver.find_element_by_id("time-to-call-early-morning")
        preferred_time_to_call_field.send_keys(Keys.SPACE)

        btn_next = self.driver.find_element_by_id("next")
        btn_next.click()

        self.assertTrue (validation_message in self.driver.page_source)

    def test_last_name_empty_should_show_validation_error(self):
        """ Missing Last Name Validation """

        # Arrange
        validation_message = "Last Name is required"

        # Act
        self.driver.get(self.address)
        self.assertIn("Your Details", self.driver.title)

        first_name_field = self.driver.find_element_by_id("id_first_name")
        first_name_field.send_keys("test_first_name")
        address_building_field = self.driver.find_element_by_id("id_building")
        address_building_field.send_keys("test_address_building")
        address_street_field = self.driver.find_element_by_id("id_street")
        address_street_field.send_keys("test_address_street")
        address_town_field = self.driver.find_element_by_id("id_town")
        address_town_field.send_keys("test_address_town")
        address_county_field = self.driver.find_element_by_id("id_county")
        address_county_field.send_keys("test_address_county")
        address_postcode_field = self.driver.find_element_by_id("id_postcode")
        address_postcode_field.send_keys("postcode")
        telephone_number_field = self.driver.find_element_by_id("id_telephone_number")
        telephone_number_field.send_keys("123")
        email_field = self.driver.find_element_by_id("id_email")
        email_field.send_keys("test_email@email.com")
        preferred_time_to_call_field = self.driver.find_element_by_id("time-to-call-early-morning")
        preferred_time_to_call_field.send_keys(Keys.SPACE)

        btn_next = self.driver.find_element_by_id("next")
        btn_next.click()

        self.assertTrue (validation_message in self.driver.page_source)

    def test_tel_number_empty_should_show_validation_error(self):
        """ Missing Telephone Number Validation """

        # Arrange
        validation_message = "Telephone Number is required"

        # Act
        self.driver.get(self.address)
        self.assertIn("Your Details", self.driver.title)

        first_name_field = self.driver.find_element_by_id("id_first_name")
        first_name_field.send_keys("test_first_name")
        last_name_field = self.driver.find_element_by_id("id_last_name")
        last_name_field.send_keys("test_last_name")
        address_building_field = self.driver.find_element_by_id("id_building")
        address_building_field.send_keys("test_address_building")
        address_street_field = self.driver.find_element_by_id("id_street")
        address_street_field.send_keys("test_address_street")
        address_town_field = self.driver.find_element_by_id("id_town")
        address_town_field.send_keys("test_address_town")
        address_county_field = self.driver.find_element_by_id("id_county")
        address_county_field.send_keys("test_address_county")
        address_postcode_field = self.driver.find_element_by_id("id_postcode")
        address_postcode_field.send_keys("postcode")
        email_field = self.driver.find_element_by_id("id_email")
        email_field.send_keys("test_email@email.com")
        preferred_time_to_call_field = self.driver.find_element_by_id("time-to-call-early-morning")
        preferred_time_to_call_field.send_keys(Keys.SPACE)

        btn_next = self.driver.find_element_by_id("next")
        btn_next.click()

        self.assertTrue (validation_message in self.driver.page_source)

    def test_time_to_call_none_selected_should_show_validation_error(self):
        """ Missing Preferred Time to Contact Validation """

        # Arrange
        validation_message = "Preferred Time to Call is required"

        # Act
        self.driver.get(self.address)
        self.assertIn("Your Details", self.driver.title)

        first_name_field = self.driver.find_element_by_id("id_first_name")
        first_name_field.send_keys("test_first_name")
        last_name_field = self.driver.find_element_by_id("id_last_name")
        last_name_field.send_keys("test_last_name")
        address_building_field = self.driver.find_element_by_id("id_building")
        address_building_field.send_keys("test_address_building")
        address_street_field = self.driver.find_element_by_id("id_street")
        address_street_field.send_keys("test_address_street")
        address_town_field = self.driver.find_element_by_id("id_town")
        address_town_field.send_keys("test_address_town")
        address_county_field = self.driver.find_element_by_id("id_county")
        address_county_field.send_keys("test_address_county")
        address_postcode_field = self.driver.find_element_by_id("id_postcode")
        address_postcode_field.send_keys("postcode")
        telephone_number_field = self.driver.find_element_by_id("id_telephone_number")
        telephone_number_field.send_keys("07777777777")
        email_field = self.driver.find_element_by_id("id_email")
        email_field.send_keys("test_email@email.com")

        btn_next = self.driver.find_element_by_id("next")
        btn_next.click()

        # Assert
        self.assertTrue (validation_message in self.driver.page_source)

    def test_valid_customer_details_should_transition_to_next_page(self):
        """ Creates a page with valid input and sends it """

        # Arrange
        expected_page_title = "Property Details"

        # Act
        self.driver.get(self.address)
        self.assertIn("Your Details", self.driver.title)

        first_name_field = self.driver.find_element_by_id("id_first_name")
        first_name_field.send_keys("test_first_name")
        last_name_field = self.driver.find_element_by_id("id_last_name")
        last_name_field.send_keys("test_last_name")
        address_building_field = self.driver.find_element_by_id("id_building")
        address_building_field.send_keys("test_address_building")
        address_street_field = self.driver.find_element_by_id("id_street")
        address_street_field.send_keys("test_address_street")
        address_town_field = self.driver.find_element_by_id("id_town")
        address_town_field.send_keys("test_address_town")
        address_county_field = self.driver.find_element_by_id("id_county")
        address_county_field.send_keys("test_address_county")
        address_postcode_field = self.driver.find_element_by_id("id_postcode")
        address_postcode_field.send_keys("postcode")
        telephone_number_field = self.driver.find_element_by_id("id_telephone_number")
        telephone_number_field.send_keys("07777777777")
        email_field = self.driver.find_element_by_id("id_email")
        email_field.send_keys("test_email@email.com")
        preferred_time_to_call_field = self.driver.find_element_by_id("time-to-call-early-morning")
        preferred_time_to_call_field.send_keys(Keys.SPACE)

        btn_next = self.driver.find_element_by_id("next")
        btn_next.click()

        # Assert
        self.assertIn(expected_page_title, self.driver.title)

    def test_valid_customer_details_should_save_to_session(self):
        """ Creates a page with valid input and sends it """

        # Arrange
        expected_page_title = "Property Details"

        # Act
        self.driver.get(self.address)
        self.assertIn("Your Details", self.driver.title)

        first_name_field = self.driver.find_element_by_id("id_first_name")
        first_name_field.send_keys("test_first_name")
        last_name_field = self.driver.find_element_by_id("id_last_name")
        last_name_field.send_keys("test_last_name")
        address_building_field = self.driver.find_element_by_id("id_building")
        address_building_field.send_keys("test_address_building")
        address_street_field = self.driver.find_element_by_id("id_street")
        address_street_field.send_keys("test_address_street")
        address_town_field = self.driver.find_element_by_id("id_town")
        address_town_field.send_keys("test_address_town")
        address_county_field = self.driver.find_element_by_id("id_county")
        address_county_field.send_keys("test_address_county")
        address_postcode_field = self.driver.find_element_by_id("id_postcode")
        address_postcode_field.send_keys("postcode")
        telephone_number_field = self.driver.find_element_by_id("id_telephone_number")
        telephone_number_field.send_keys("07777777777")
        email_field = self.driver.find_element_by_id("id_email")
        email_field.send_keys("test_email@email.com")
        preferred_time_to_call_field = self.driver.find_element_by_id("time-to-call-early-morning")
        preferred_time_to_call_field.send_keys(Keys.SPACE)

        btn_next = self.driver.find_element_by_id("next")
        btn_next.click()

        # Assert
        self.assertIn(expected_page_title, self.driver.title)
