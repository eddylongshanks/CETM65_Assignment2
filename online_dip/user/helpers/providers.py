""" Provider objects for building data sets """

class EnquiryProvider:
    """ Stores a dictionary list of form values to be retrieved later """

    def __init__(self):
        self.data = {}

    def add(self, data_to_add):
        """ Add a dictionary object to the existing list """

        if not isinstance(data_to_add, dict):
            raise TypeError("Object must be a Dictionary")

        self.data.update(data_to_add)

    def get_list(self):
        """ Return the list as a dictionary object """
        return self.data

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return "EnquiryProvider()"
