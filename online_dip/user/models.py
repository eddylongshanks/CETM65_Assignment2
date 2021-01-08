"""
models file for the enquiry creator
"""

from django.db import models


class Enquiry(models.Model):
    """
    Enquiry db class
    """

    first_name = models.CharField(max_length=40, verbose_name="First Name")
    last_name = models.CharField(max_length=40, verbose_name="Last Name")
    address_building = models.CharField(max_length=50, blank=True, verbose_name="Building Name/Number")
    address_street = models.CharField(max_length=50, blank=True, verbose_name="Street")
    address_town = models.CharField(max_length=50, blank=True, verbose_name="Town")
    address_county = models.CharField(max_length=50, blank=True, verbose_name="County")
    address_postcode = models.CharField(max_length=10, blank=True, verbose_name="Postcode")
    telephone_number = models.CharField(max_length=25, verbose_name="Telephone Number")
    email = models.EmailField(max_length=254, blank=True, verbose_name="Email Address")

    # refactor choices
    # radio buttons?

    MORNING = 'M'
    EARLY_AFTERNOON = 'EA'
    LATE_AFTERNOON = 'LA'
    SATURDAY = 'S'
    PREFERRED_TIME_TO_CALL_CHOICES = [
        (MORNING, '9am - 12pm (Mon-Fri)'),
        (EARLY_AFTERNOON, '12pm - 3pm (Mon-Fri)'),
        (LATE_AFTERNOON, '3pm - 5pm (Mon-Fri)'),
        (SATURDAY, '9am - 2pm (Sat)'),
    ]
    preferred_time_to_call = models.CharField(
        max_length=2,
        choices=PREFERRED_TIME_TO_CALL_CHOICES,
        default=MORNING,
        verbose_name="Preferred Time to Call"
    )

    annual_income = models.IntegerField(verbose_name="Annual Income")
    loan_amount = models.IntegerField(verbose_name="Loan Amount")
    property_value = models.IntegerField(verbose_name="Property Value")

    NEW_HOUSE = 'NH'
    REMORTGAGE = 'RM'
    MORTGAGE_TYPE_CHOICES = [
        (NEW_HOUSE, 'New House'),
        (REMORTGAGE, 'Remortgage'),
    ]
    mortgage_type = models.CharField(
        max_length=2,
        choices=MORTGAGE_TYPE_CHOICES,
        default=NEW_HOUSE,
        verbose_name="Mortgage Type"
    )

    # Define __str__ that will be called when querying e.g. 'User.objects.all()'
    def __str__(self):
        obj_str = f'First Name: {self.first_name}, ' \
                  f'Last Name: {self.last_name}, ' \
                  f'Tel: {self.telephone_number}' \

        return obj_str
