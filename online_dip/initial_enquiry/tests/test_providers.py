""" EnquiryProvider Tests """

from django.test import TestCase, tag
from ..helpers.providers import EnquiryProvider

@tag('fast')
class TestEnquiryProvider(TestCase):
    """ Tests for EnquiryProvider object """

    def setUp(self):
        self.provider = EnquiryProvider()

    def tearDown(self):
        self.provider = None

    def test_add_dict_object_should_add_to_list(self):
        """ A valid dictionary object should be added to the list """

        # Arrange
        expected_dictionary = {
            'testkey1' : 'testvalue1',
            'testkey2' : 'testvalue2',
        }

        # Act
        self.provider.add(expected_dictionary)
        actual_dictionary = self.provider.get_list()

        # Assert
        self.assertDictEqual(expected_dictionary, actual_dictionary)

    def test_add_second_dict_object_should_update_list(self):
        """ Passing multiple dictionary objects should update the list """

        # Arrange
        first_dictionary = {
            'testkey1' : 'testvalue1',
            'testkey2' : 'testvalue2',
        }

        second_dictionary = {
            'testkey3' : 'testvalue3',
            'testkey4' : 'testvalue4',
        }

        expected_dictionary = {
            'testkey1' : 'testvalue1',
            'testkey2' : 'testvalue2',
            'testkey3' : 'testvalue3',
            'testkey4' : 'testvalue4',
        }

        # Act
        self.provider.add(first_dictionary)
        self.provider.add(second_dictionary)
        actual_dictionary = self.provider.get_list()

        # Assert
        self.assertDictEqual(expected_dictionary, actual_dictionary)

    def test_add_non_dict_object_should_raise_value_error_exception(self):
        """
        Attempting to add any non-dictionary object to the list
        should raise TypeError exception
        """

        # Arrange
        data = 5
        expected_message = "Object must be a Dictionary"

        # Act
        with self.assertRaises(TypeError) as context:
            self.provider.add(data)

        # Assert
        self.assertTrue(expected_message in str(context.exception))

    def test__str__should_return_dictionary_as_string(self):
        """ Ensure __str__ returns dictionary object as a string"""

        # Arrange
        dictionary = {
            'testkey1' : 'testvalue1',
            'testkey2' : 'testvalue2',
        }

        expected_string = "{'testkey1': 'testvalue1', 'testkey2': 'testvalue2'}"

        # Act
        self.provider.add(dictionary)
        actual_string = self.provider.__str__()

        # Assert
        self.assertEqual(expected_string, actual_string)
