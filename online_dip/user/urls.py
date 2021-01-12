"""
url mapping for the enquiry creator
"""

from django.urls import path
from .views import EnquiryListView, EnquiryDetailView
from . import views

urlpatterns = [
    # remove
    # path('testroute/', views.testroute, name='testroute'),
    path('emailtest/', views.emailtest, name='emailtest'),
    path('advisertest/', views.advisertest, name='adviser-test'),


    path('customer_details/', views.customer_details, name='customer_details'),
    path('property_details/', views.property_details, name='property_details'),
    path('thank_you/', views.thank_you, name='thank_you'),

    # path('adviser/', views.adviser, name='adviser-home'),
    path('adviser/enquiries', EnquiryListView.as_view() , name='adviser-home'),
    path('adviser/enquiry/<int:pk>/', EnquiryDetailView.as_view() , name='adviser-detail'),

]
