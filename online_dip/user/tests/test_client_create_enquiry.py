"""
Test file for Client tests
"""

from django.test import TestCase, Client

class TestClientCreateEnquiry(TestCase):
    """
    Test class to create enquiry using client
    """

    def setUp(self):
        self.client = Client()

    def test_create_enquiry_by_client_with_all_valid_fields_should_create_entry_in_db(self):
        """
        Creates a full Enquiry using the Client
        """

        response = self.client.post('/customer_details/',
            {
                'first_name': 'client_firstname',
                'last_name': 'client_lastname',
                'address_building': 'building',
                'address_street': 'street',
                'address_town': 'town',
                'address_county': 'county',
                'address_postcode': 'test_postcode',
                'telephone_number': '0123',
                'email': 'me@me.com',
                'preferred_time_to_call': 'S'
            })

        print(response.client.session)

        # response.client.post('/property_details/',
        #     {
        #         'annual_income': '300',
        #         'loan_amount': '400',
        #         'property_value': '500',
        #         'mortgage_type': 'RM'
        #     })

        # print(response.status_code)
