"""
form classes for the enquiry creator
"""

from django import forms
from .models import Customer, PersonalDetails, PropertyDetails, Address


# class AddressForm(forms.ModelForm):

#     class Meta:
#         model = Address
#         fields = ['building', 'street', 'town', 'county', 'postcode']

class CustomerDetailsForm(forms.ModelForm):
    """
    Page 1 of the oDip Enquiry journey
    """

    class Meta:
        model = Customer
        fields = ['address_id', 'first_name', 'last_name', 'building', 'street', 'town', 'county', 'postcode', 'telephone_number', 'email', 'preferred_time_to_contact']
        widgets = {
            'preferred_time_to_contact': forms.RadioSelect(),
        }


class PropertyDetailsForm(forms.ModelForm):
    """
    Page 2 of the oDip Enquiry journey
    """

    class Meta():
        model = Customer
        fields = ['annual_income', 'loan_amount', 'property_value', 'mortgage_type']
        widgets = {
            'mortgage_type': forms.RadioSelect(),
        }


# class EnquiryForm(CustomerDetailsForm, PropertyDetailsForm):
#     class Meta(CustomerDetailsForm.Meta, PropertyDetailsForm.Meta):
#         model = Enquiry
#         # fields = ['annual_income', 'loan_amount', 'property_value', 'mortgage_type']
#         fields = CustomerDetailsForm.Meta.fields + PropertyDetailsForm.Meta.fields
