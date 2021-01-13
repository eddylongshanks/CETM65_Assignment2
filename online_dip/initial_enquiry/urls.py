"""
url mapping for the enquiry creator
"""

from django.urls import path
from .views import (
    customer_details,
    property_details,
    thank_you,
    EnquiryListView,
    EnquiryUpdateView,
)

urlpatterns = [
    # remove
    # path('emailtest/', views.emailtest, name='emailtest'),
    # path('advisertest/', views.advisertest, name='adviser-test'),

    path('yourdetails/', customer_details, name='customer_details'),
    path('propertydetails/', property_details, name='property_details'),
    path('thankyou/', thank_you, name='thank_you'),
    path('adviser/enquiries', EnquiryListView.as_view() , name='adviser-list'),
    path('adviser/enquiry/<int:pk>/update/', EnquiryUpdateView.as_view() , name='adviser-update'),
]
