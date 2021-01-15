""" form classes for the enquiry creator """

from django import forms
from .models import Enquiry
from django.conf import settings


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

    ltv_value = forms.FloatField(max_value=100, min_value=0, label="LTV")

    class Meta:
        model = Enquiry
        fields = ['annual_income', 'loan_amount', 'property_value', 'mortgage_type', 'ltv_value']
        widgets = {
            'mortgage_type': forms.RadioSelect(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Override default "required" validation message to mention the field name
        for field in self.fields.values():
            field.error_messages = {'required' : f'{field.label} is required'}

    def clean_ltv_value(self):
        """ Validates LTV against MAX_LTV """
        max_ltv = settings.MAX_LTV
        ltv = self.cleaned_data['ltv_value']

        if ltv > max_ltv:
            raise forms.ValidationError("LTV is too high, consider reducing your Loan Amount")


class EnquiryForm(forms.ModelForm):
    """ Final full enquiry model """

    class Meta:
        model = Enquiry
        fields = ['first_name', 'last_name', 'building', 'street', 'town', 'county', 'postcode', 'telephone_number', 'email', 'preferred_time_to_contact',
                  'annual_income', 'loan_amount', 'property_value', 'mortgage_type' ]
