""" Tests using the Django Client """

from django.test import TestCase, Client, tag
from ..models import Enquiry

@tag('fast')
class TestClientPropertyDetails(TestCase):
    """ Tests for verifying HttpResponses using Client """

    def setUp(self):
        self.client = Client()

    def tearDown(self):
        self.client = None

    def test_httpget_without_customer_details_in_session_should_return_302_response(self):
        """ Test for property details httpGet """

        # Arrange
        expected_status_code = 302
        address = '/propertydetails/'

        # Act
        response = self.client.get(address)

        # Assert
        self.assertEqual(response.status_code, expected_status_code)

    def test_httppost_with_invalid_session_data_should_return_302(self):
        """ Property Details POST request with invalid session data """

        # Arrange
        expected_status_code = 302
        address = '/propertydetails/'

        customer_details_data = {
                'first_name': 'client_34546576',
                # 'last_name': 'client_lastname',
                'building': 'building',
                'street': 'street',
                'town': 'town',
                'county': 'county',
                'postcode': 'postcode',
                'telephone_number': '07777777777',
                'email': 'me@me.com',
                'preferred_time_to_contact': 'S'
            }
        property_details_data = {
                'annual_income': '300',
                'loan_amount': '400',
                'property_value': '500',
                'mortgage_type': 'RM'
            }
        session = self.client.session
        session['customer_details'] = customer_details_data
        session.save()

        # Act
        response = self.client.post(address, property_details_data)

        # Assert
        self.assertEqual(response.status_code, expected_status_code)

    def test_httpget_with_customer_details_in_session_should_return_200_response(self):
        """ Test for property details httpGet """

        # Arrange
        expected_status_code = 200
        address = '/propertydetails/'
        customer_details_data = {
                'first_name': 'client_firstname',
                'last_name': 'client_lastname',
                'building': 'building',
                'street': 'street',
                'town': 'town',
                'county': 'county',
                'postcode': 'postcode',
                'telephone_number': '07777777777',
                'email': 'me@me.com',
                'preferred_time_to_contact': 'S'
            }
        session = self.client.session
        session['customer_details'] = customer_details_data
        session.save()

        # Act
        response = self.client.get(address)

        # Assert
        self.assertEqual(response.status_code, expected_status_code)

    def test_httppost_with_all_valid_fields_should_create_entry_in_db(self):
        """ Creates a full Enquiry using the Client """

        # Arrange
        expected_status_code = 302
        expected_first_name = 'client_34546576'
        address = '/propertydetails/'

        customer_details_data = {
                'first_name': 'client_34546576',
                'last_name': 'client_lastname',
                'building': 'building',
                'street': 'street',
                'town': 'town',
                'county': 'county',
                'postcode': 'postcode',
                'telephone_number': '07777777777',
                'email': 'me@me.com',
                'preferred_time_to_contact': 'S'
            }
        property_details_data = {
                'annual_income': '300',
                'loan_amount': '400',
                'property_value': '500',
                'mortgage_type': 'RM'
            }
        session = self.client.session
        session['customer_details'] = customer_details_data
        session.save()

        # Act
        response = self.client.post(address, property_details_data)

        # Assert
        self.assertEqual(response.status_code, expected_status_code)
        try:
            enquiry = Enquiry.objects.get(first_name=expected_first_name)
        except Enquiry.DoesNotExist:
            self.fail(f'{expected_first_name} was not found in the database')
