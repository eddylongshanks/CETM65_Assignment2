"""
Test file for Create Enquiry user journey, with selenium
"""

from selenium import webdriver
from selenium.webdriver.support.select import Select
from django.test import TestCase
from ..models import Enquiry


class TestJourneyCreateEnquiry(TestCase):
    """
    Test class to create enquiry using selenium
    """

    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    # User Story: billy_testcase should be able to add himself as a new user
    def test_create_enquiry_with_all_valid_fields_should_create_entry_in_db(self):
        """
        Creates a full Enquiry with valid input
        """

        self.driver.get("http://127.0.0.1:8000/customer_details")
        self.assertIn("Customer Details", self.driver.title)
        first_name_field = self.driver.find_element_by_id("id_first_name")
        first_name_field.send_keys("test_first_name")
        last_name_field = self.driver.find_element_by_id("id_last_name")
        last_name_field.send_keys("test_last_name")
        address_building_field = self.driver.find_element_by_id("id_address_building")
        address_building_field.send_keys("test_address_building")
        address_street_field = self.driver.find_element_by_id("id_address_street")
        address_street_field.send_keys("test_address_street")
        address_town_field = self.driver.find_element_by_id("id_address_town")
        address_town_field.send_keys("test_address_town")
        address_county_field = self.driver.find_element_by_id("id_address_county")
        address_county_field.send_keys("test_address_county")
        address_postcode_field = self.driver.find_element_by_id("id_address_postcode")
        address_postcode_field.send_keys("test_address_postcode")
        telephone_number_field = self.driver.find_element_by_id("id_telephone_number")
        telephone_number_field.send_keys("123")
        email_field = self.driver.find_element_by_id("id_email")
        email_field.send_keys("test_email@email.com")
        preferred_time_to_call_field = Select(self.driver.find_element_by_id("id_preferred_time_to_call"))
        preferred_time_to_call_field.select_by_index('1')

        btn_next = self.driver.find_element_by_id("next")
        btn_next.click()

        self.assertIn("Property Details", self.driver.title)
        annual_income_field = self.driver.find_element_by_id("id_annual_income")
        annual_income_field.send_keys("5001")
        loan_amount_field = self.driver.find_element_by_id("id_loan_amount")
        loan_amount_field.send_keys("6001")
        property_value_field = self.driver.find_element_by_id("id_property_value")
        property_value_field.send_keys("7001")
        mortgage_type_field = Select(self.driver.find_element_by_id("id_mortgage_type"))
        mortgage_type_field.select_by_index('1')

        btn_submit = self.driver.find_element_by_id("submit")
        btn_submit.click()

        enquiry_actual = Enquiry.objects.all().filter(first_name="test_first_name").first
        print(enquiry_actual)
        self.assertIsInstance(enquiry_actual, Enquiry)
