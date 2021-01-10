
class EnquiryProvider:
    """
    
    """

    def __init__(self):
        self.data = {}

    def get_name(self, field_name):
        return self.data.get(field_name)

    def add(self, data_to_add):

        try:
            dict(data_to_add)
        except ValueError:
            print("invalid type")

        self.data.update(data_to_add)

    def get_list(self):
        return self.data

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return "EnquiryProvider()"
