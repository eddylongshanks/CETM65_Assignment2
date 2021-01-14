""" Tests using the Django Client """

from django.test import TestCase, Client, tag

@tag('fast')
class TestClientThankYou(TestCase):
    """ Tests for verifying HttpResponses using Client """

    def setUp(self):
        self.client = Client()

    def tearDown(self):
        self.client = None

    def test_httpget_with_no_customer_details_session_data_should_return_302_response(self):
        """ Test to ensure user is redirected when attempting access page directly """

        # Arrange
        expected_status_code_accepted = 302
        address = '/thankyou/'

        # Act
        response = self.client.get(address)

        # Assert
        self.assertEqual(response.status_code, expected_status_code_accepted)

    def test_httpget_with_customer_details_in_session_should_return_200_response(self):
        """ Test for valid httpGet """

        # Arrange
        expected_status_code = 200
        address = '/thankyou/'
        customer_details_data = {
                'first_name': 'client_firstname',
                'last_name': 'client_lastname',
                'building': 'building',
                'street': 'street',
                'town': 'town',
                'county': 'county',
                'postcode': 'postcode',
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

    def test_httpget_with_customer_details_in_session_should_clear_the_session_data(self):
        """ Test for clearing the session data """

        # Arrange
        expected_status_code = 200
        session_key = 'customer_details'
        address = '/thankyou/'
        customer_details_data = {
                'first_name': 'client_firstname',
                'last_name': 'client_lastname',
                'building': 'building',
                'street': 'street',
                'town': 'town',
                'county': 'county',
                'postcode': 'postcode',
                'telephone_number': '0123',
                'email': 'me@me.com',
                'preferred_time_to_contact': 'S'
            }
        session = self.client.session
        session[session_key] = customer_details_data
        session.save()

        # Act
        response = self.client.get(address)        

        # Assert
        self.assertEqual(response.status_code, expected_status_code)
        self.assertNotIn(session_key, response.client.session)
