from .models import Enquiry
from django.forms import ModelForm


class CustomerDetailsForm(ModelForm):
    class Meta:
        model = Enquiry
        fields = ['first_name', 'last_name', 'address_building', 'address_street', 'address_town', 'address_county', 'address_postcode', 'telephone_number', 'email', 'preferred_time_to_call']        
        # fields = ['first_name']        


class PropertyDetailsForm(ModelForm):
    class Meta():
        model = Enquiry
        fields = ['annual_income', 'loan_amount', 'property_value', 'mortgage_type']
        # fields = ['annual_income']


# class EnquiryForm(CustomerDetailsForm, PropertyDetailsForm):
#     class Meta(CustomerDetailsForm.Meta, PropertyDetailsForm.Meta):
#         model = Enquiry
#         # fields = ['annual_income', 'loan_amount', 'property_value', 'mortgage_type']
#         fields = CustomerDetailsForm.Meta.fields + PropertyDetailsForm.Meta.fields

