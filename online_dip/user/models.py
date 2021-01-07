from django.db import models

class Enquiry(models.Model):    
    firstname = models.CharField(max_length=40)
    lastname = models.CharField(max_length=40)
    address_building = models.CharField(max_length=50)
    address_street = models.CharField(max_length=50)
    address_town = models.CharField(max_length=50)
    address_county = models.CharField(max_length=50)
    address_postcode = models.CharField(max_length=10)
    telephone_number = models.CharField(max_length=25)
    email = models.EmailField(max_length=254)

    # Define __str__ that will be called when querying e.g. 'User.objects.all()'
    def __str__(self):
        obj_str = f'First Name: {self.firstname}, ' \
                  f'Second Name: {self.lastname}, ' \
                  f'Tel: {self.telephone_number}' \

        return obj_str

    # MORNING = 'M'
    # EARLY_AFTERNOON = 'EA'
    # LATE_AFTERNOON = 'LA'
    # SATURDAY = 'S'
    # PREFERRED_TIME_TO_CALL_CHOICES = [
    #     (MORNING, '9am - 12pm (Mon-Fri)'),
    #     (EARLY_AFTERNOON, '12pm - 3pm (Mon-Fri)'),
    #     (LATE_AFTERNOON, '3pm - 5pm (Mon-Fri)'),
    #     (SATURDAY, '9am - 2pm (Sat)'),
    # ]
    # preferred_time_to_call = models.CharField(
    #     max_length=2,
    #     choices=PREFERRED_TIME_TO_CALL_CHOICES,
    #     default=MORNING,
    # )