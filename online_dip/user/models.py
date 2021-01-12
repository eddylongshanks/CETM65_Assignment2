"""
models file for the enquiry creator
"""

from django.db import models
from django.utils import timezone


class Address(models.Model):
    """ Address Model """

    address_id = models.AutoField(primary_key=True)
    building = models.CharField(max_length=50, blank=True, verbose_name="Building and Street")
    street = models.CharField(max_length=50, blank=True, verbose_name="Street")
    town = models.CharField(max_length=50, blank=True, verbose_name="Town")
    county = models.CharField(max_length=50, blank=True, verbose_name="County")
    postcode = models.CharField(max_length=10, blank=True, verbose_name="Postcode")

    def __str__(self):
        obj_str = f'Street: {self.building} {self.street}, ' \
                  f'Postcode: {self.postcode}, ' \

        return obj_str


class PersonalDetails(Address):
    """ Personal Details Model, holding customer information from page 1 """

    personal_details_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=40, verbose_name="First Name")
    last_name = models.CharField(max_length=40, verbose_name="Last Name")
    telephone_number = models.CharField(max_length=25, verbose_name="Telephone Number")
    email = models.EmailField(max_length=254, blank=True, verbose_name="Email Address")

    MORNING = 'M'
    EARLY_AFTERNOON = 'EA'
    LATE_AFTERNOON = 'LA'
    SATURDAY = 'S'
    PREFERRED_TIME_TO_CONTACT_CHOICES = [
        (MORNING, '9am - 12pm (Mon-Fri)'),
        (EARLY_AFTERNOON, '12pm - 3pm (Mon-Fri)'),
        (LATE_AFTERNOON, '3pm - 5pm (Mon-Fri)'),
        (SATURDAY, '9am - 2pm (Sat)'),
    ]
    preferred_time_to_contact = models.CharField(
        max_length=2,
        choices=PREFERRED_TIME_TO_CONTACT_CHOICES,
        default=MORNING,
        verbose_name="Preferred Time to Call"
    )

    # Add preferred time to be contacted?

    def __str__(self):
        obj_str = f'Tel: {self.telephone_number}, ' \
                  f'First Name: {self.first_name}, ' \
                  f'Last Name: {self.last_name}, ' \

        return obj_str


class PropertyDetails(models.Model):
    """ Property Details Model, holding information from page 2 """

    property_details_id = models.AutoField(primary_key=True)
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

    def __str__(self):
        obj_str = f'Loan Amount: {self.loan_amount}, ' \
                  f'Property Value: {self.property_value}, ' \

        return obj_str


class Enquiry(PersonalDetails, PropertyDetails):
    """ Full Enquiry Model, consolidate all information and add extra non-user fields """

    date_created = models.DateField(default=timezone.now, verbose_name="Date Created")
    has_been_contacted = models.BooleanField(default=False, verbose_name="Has been Contacted?")

    def __str__(self):
        obj_str = f'{self.first_name} {self.last_name} - ' \
                  f'Tel: {self.telephone_number}, ' \

        return obj_str
