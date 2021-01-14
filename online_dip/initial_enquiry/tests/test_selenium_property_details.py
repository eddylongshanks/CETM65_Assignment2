""" Test file for Create Enquiry user journey, with selenium """

from django.test import TestCase, tag
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

@tag('slow', 'selenium')
class TestJourneyCreateEnquiry(TestCase):
    """ Test class to create enquiry using selenium """

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://127.0.0.1:8000/yourdetails")
        self.assertIn("Your Details", self.driver.title)

        # Get to the Property Details Page

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

    def tearDown(self):
        self.driver.quit()

    def test_annual_income_empty_should_show_validation_error(self):
        """ Missing Annual Income validation """

        # Arrange
        validation_message = "Annual Income is required"

        # Act
        loan_amount_field = self.driver.find_element_by_id("id_loan_amount")
        loan_amount_field.send_keys("6001")
        property_value_field = self.driver.find_element_by_id("id_property_value")
        property_value_field.send_keys("7001")
        mortgage_type_field = self.driver.find_element_by_id("mortgage-type-remortgage")
        mortgage_type_field.send_keys(Keys.SPACE)

        btn_submit = self.driver.find_element_by_id("submit")
        btn_submit.click()

        # Assert
        self.assertTrue (validation_message in self.driver.page_source)

    def test_loan_amount_empty_should_show_validation_error(self):
        """ Missing Loan Amount validation """

        # Arrange
        validation_message = "Loan Amount is required"

        # Act
        annual_income_field = self.driver.find_element_by_id("id_annual_income")
        annual_income_field.send_keys("5001")
        property_value_field = self.driver.find_element_by_id("id_property_value")
        property_value_field.send_keys("7001")
        mortgage_type_field = self.driver.find_element_by_id("mortgage-type-remortgage")
        mortgage_type_field.send_keys(Keys.SPACE)

        btn_submit = self.driver.find_element_by_id("submit")
        btn_submit.click()

        # Assert
        self.assertTrue (validation_message in self.driver.page_source)

    def test_property_value_empty_should_show_validation_error(self):
        """ Missing Property Value validation """

        # Arrange
        validation_message = "Property Value is required"

        # Act
        annual_income_field = self.driver.find_element_by_id("id_annual_income")
        annual_income_field.send_keys("5001")
        loan_amount_field = self.driver.find_element_by_id("id_loan_amount")
        loan_amount_field.send_keys("6001")
        mortgage_type_field = self.driver.find_element_by_id("mortgage-type-remortgage")
        mortgage_type_field.send_keys(Keys.SPACE)

        btn_submit = self.driver.find_element_by_id("submit")
        btn_submit.click()

        # Assert
        self.assertTrue (validation_message in self.driver.page_source)

    def test_mortgage_type_unselected_should_show_validation_error(self):
        """ Missing Mortgage Type validation """

        # Arrange
        validation_message = "Mortgage Type is required"

        # Act
        annual_income_field = self.driver.find_element_by_id("id_annual_income")
        annual_income_field.send_keys("5001")
        loan_amount_field = self.driver.find_element_by_id("id_loan_amount")
        loan_amount_field.send_keys("6001")
        property_value_field = self.driver.find_element_by_id("id_property_value")
        property_value_field.send_keys("7001")

        btn_submit = self.driver.find_element_by_id("submit")
        btn_submit.click()

        # Assert
        self.assertTrue (validation_message in self.driver.page_source)

    def test_valid_data_should_redirect(self):
        """ Valid Data should result in redirection """

        # Arrange
        expected_page = "Thank You"

        # Act
        annual_income_field = self.driver.find_element_by_id("id_annual_income")
        annual_income_field.send_keys("5001")
        loan_amount_field = self.driver.find_element_by_id("id_loan_amount")
        loan_amount_field.send_keys("6001")
        property_value_field = self.driver.find_element_by_id("id_property_value")
        property_value_field.send_keys("7001")
        mortgage_type_field = self.driver.find_element_by_id("mortgage-type-remortgage")
        mortgage_type_field.send_keys(Keys.SPACE)

        btn_submit = self.driver.find_element_by_id("submit")
        btn_submit.click()

        # Assert
        self.assertIn(expected_page, self.driver.title)
