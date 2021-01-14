""" Tests using the Django Client """

from django.test import TestCase, Client, tag

@tag('fast')
class TestClientCustomerDetails(TestCase):
    """ Tests for verifying HttpResponses using Client """

    def setUp(self):
        self.client = Client()

    def tearDown(self):
        self.client = None

    def test_httpget_should_return_200_response(self):
        """ Test for customer details httpGet """

        # Arrange
        expected_status_code_accepted = 200
        address = '/yourdetails/'

        # Act
        response = self.client.get(address)

        # Assert
        self.assertEqual(response.status_code, expected_status_code_accepted)

    def test_httppost_with_missing_data_should_return_400_response(self):
        """ Test httppost with missing data """

        # Arrange
        expected_status_code = 400
        address = '/yourdetails/'
        customer_details_data = {
                'first_name': 'client_firstname'
            }

        # Act
        response = self.client.post(address, customer_details_data)

        # Assert
        self.assertEqual(response.status_code, expected_status_code)

    def test_httppost_with_valid_data_should_return_200_response(self):
        """ Test httppost with valid data """

        # Arrange
        expected_status_code = 302
        address = '/yourdetails/'
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

        # Act
        response = self.client.post(address, customer_details_data)

        # Assert
        self.assertEqual(response.status_code, expected_status_code)
