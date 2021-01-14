""" form classes for the enquiry creator """

from django import forms
from .models import Enquiry


class CustomerDetailsForm(forms.ModelForm):
    """ Page 1 of the Initial Enquiry journey """

    class Meta:
        model = Enquiry
        fields = ['first_name', 'last_name', 'building', 'street', 'town', 'county', 'postcode', 'telephone_number', 'email', 'preferred_time_to_contact']
        widgets = {
            'preferred_time_to_contact': forms.RadioSelect(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Override default "required" validation message to mention the field name
        for field in self.fields.values():
            field.error_messages = {'required' : f'{field.label} is required'}


class PropertyDetailsForm(forms.ModelForm):
    """ Page 2 of the Initial Enquiry journey """

    class Meta:
        model = Enquiry
        fields = ['annual_income', 'loan_amount', 'property_value', 'mortgage_type']
        widgets = {
            'mortgage_type': forms.RadioSelect(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Override default "required" validation message to mention the field name
        for field in self.fields.values():
            field.error_messages = {'required' : f'{field.label} is required'}


class EnquiryForm(forms.ModelForm):
    """ Final full enquiry model """

    class Meta:
        model = Enquiry
        fields = ['first_name', 'last_name', 'building', 'street', 'town', 'county', 'postcode', 'telephone_number', 'email', 'preferred_time_to_contact',
                  'annual_income', 'loan_amount', 'property_value', 'mortgage_type' ]
