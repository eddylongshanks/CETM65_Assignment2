""" Tests using the Django Client """

from django.test import TestCase, Client, tag

@tag('client_tests')
class TestClientCreateEnquiry(TestCase):
    """ Tests for verifying HttpResponses using Client """

    def setUp(self):
        self.client = Client()

    def tearDown(self):
        self.client = None


    def test_httpget_customer_details_should_return_200_response(self):
        """ Test for customer details httpGet """

        # Arrange
        expected_status_code = 200
        address = '/customer_details/'

        # Act
        response = self.client.get(address)

        # Assert
        self.assertEqual(response.status_code, expected_status_code)


    def test_httpget_property_details_with_customer_details_saved_should_return_200_response(self):
        """ Test for property details httpGet """

        # Arrange
        expected_status_code = 200
        address = '/property_details/'
        customer_details_data = {
                'first_name': 'client_firstname',
                'last_name': 'client_lastname',
                'address_building': 'building',
                'address_street': 'street',
                'address_town': 'town',
                'address_county': 'county',
                'address_postcode': 'test_postcode',
                'telephone_number': '0123',
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

    def test_httpget_property_details_without_customer_details_in_session_should_return_302_response(self):
        """ Test for property details httpGet """

        # Arrange
        expected_status_code = 302
        address = '/property_details/'

        # Act
        response = self.client.get(address)

        # Assert
        self.assertEqual(response.status_code, expected_status_code)

    def test_create_enquiry_with_all_valid_fields_should_create_entry_in_db(self):
        """ Creates a full Enquiry using the Client """

        # Arrange

        expected_status_code = 302
        address = '/property_details/'

        customer_details_data = {
                'first_name': 'client_firstname',
                'last_name': 'client_lastname',
                'address_building': 'building',
                'address_street': 'street',
                'address_town': 'town',
                'address_county': 'county',
                'address_postcode': 'test_postcode',
                'telephone_number': '0123',
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
