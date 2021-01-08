"""
form classes for the enquiry creator
"""

from django import forms
from .models import Enquiry


class CustomerDetailsForm(forms.ModelForm):
    """
    Page 1 of the oDip Enquiry journey
    """

    class Meta:
        model = Enquiry
        fields = ['first_name', 'last_name', 'address_building', 'address_street', 'address_town',
        'address_county', 'address_postcode', 'telephone_number', 'email', 'preferred_time_to_call']


class PropertyDetailsForm(forms.ModelForm):
    """
    Page 2 of the oDip Enquiry journey
    """

    class Meta():
        model = Enquiry
        fields = ['annual_income', 'loan_amount', 'property_value', 'mortgage_type']


# class EnquiryForm(CustomerDetailsForm, PropertyDetailsForm):
#     class Meta(CustomerDetailsForm.Meta, PropertyDetailsForm.Meta):
#         model = Enquiry
#         # fields = ['annual_income', 'loan_amount', 'property_value', 'mortgage_type']
#         fields = CustomerDetailsForm.Meta.fields + PropertyDetailsForm.Meta.fields
