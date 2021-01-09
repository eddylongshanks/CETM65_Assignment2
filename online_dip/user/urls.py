"""
url mapping for the enquiry creator
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('testroute/', views.testroute, name='testroute'),
    path('customer_details/', views.customer_details, name='customer_details'),
    path('property_details/', views.property_details, name='property_details'),
]
