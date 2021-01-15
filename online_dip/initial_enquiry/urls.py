""" url mapping for the enquiry creator """

from django.urls import path
from .views import (
    customer_details,
    property_details,
    calculate_ltv,
    thank_you,
    EnquiryListView,
    EnquiryUpdateView,
)

urlpatterns = [
    path('yourdetails/', customer_details, name='customer_details'),
    path('propertydetails/', property_details, name='property_details'),
    path('ajax/calculate_ltv/', calculate_ltv, name='calculate_ltv'),
    path('thankyou/', thank_you, name='thank_you'),
    path('adviser/enquiries', EnquiryListView.as_view() , name='adviser-list'),
    path('adviser/enquiry/<int:pk>/update/', EnquiryUpdateView.as_view() , name='adviser-update'),
]
