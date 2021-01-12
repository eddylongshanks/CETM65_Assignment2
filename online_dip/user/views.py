"""
The main view file, handles all get and post requests to create an Enquiry.
"""

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, UpdateView
from .forms import CustomerDetailsForm, PropertyDetailsForm, CustomerForm
from .models import Enquiry
from .helpers.providers import EnquiryProvider
from .helpers.mailer import EmailSender


def customer_details(request):
    """
    Customer Details form, first page of Enquiry.
    """

    if request.method == "POST":
        form = CustomerDetailsForm(request.POST, use_required_attribute=False)
        if form.is_valid():
            # Save to the session to be retreived later
            request.session["customer_details"] = form.cleaned_data
            return redirect("property_details")
    else:
        form = CustomerDetailsForm(use_required_attribute=False)

    context = {
        "form": form
    }

    return render(request, "customer_details.html", context)


def property_details(request):
    """
    Property Details form, second page of Enquiry.
    """

    # Session check to verify customer details are available
    if not "customer_details" in request.session:
        return redirect("customer_details")

    if request.method =="POST":
        form = PropertyDetailsForm(request.POST, use_required_attribute=False)
        if form.is_valid():
            property_details_data = form.cleaned_data
            customer_details_data = request.session["customer_details"]

            # Consolidate data from other pages to prep for db entry
            enquiry_data = EnquiryProvider()
            enquiry_data.add(property_details_data)
            enquiry_data.add(customer_details_data)
            completed_data = enquiry_data.get_list()

            enquiry = CustomerForm(completed_data)

            # Perform final validation, redirect to start if there is invalid data
            if not enquiry.is_valid():
                return redirect("customer_details")

            enquiry.save()

            # Send a confirmation email to the customer only after saving the enquiry
            mailer = EmailSender(enquiry_data.get_list())
            mailer.send()

            return redirect("thank_you")
    else:
        form = PropertyDetailsForm(use_required_attribute=False)

    context = {
        "form": form
    }
    return render(request, "property_details.html", context)


def thank_you(request):
    """ Page displayed on submission complete """

    # Clean the session
    request.session["customer_details"] = {}

    return render(request, "thank_you.html")

# @login_required
# def adviser(request):
#     customers =  Customer.objects.all()

#     context = {
#         "customers": customers
#     }
#     return render(request, "adviser/enquiry_list.html", context)

class EnquiryListView(LoginRequiredMixin, ListView):
    model = Enquiry
    template_name = "adviser/enquiry_list.html"
    context_object_name = "customers"

    # Only return customers who have not yet been contacted
    queryset = Enquiry.objects.filter(has_been_contacted="False")


class EnquiryUpdateView(LoginRequiredMixin, UpdateView):
    model = Enquiry
    fields = [ 'has_been_contacted' ]



# to remove

def advisertest(request):
    customers =  Enquiry.objects.all()

    context = {
        "customers": customers
    }
    return render(request, "adviser/enquiry_list.html", context)


def emailtest(request):

    customer_details_data = {
                'first_name': 'Katie',
                'email': 'chris@holmescentral.co.uk',
                'preferred_time_to_contact': 'S',
            }
    mailer = EmailSender(customer_details_data)

    mailer.send()
    return HttpResponse(mailer)

# def testroute(request):
#     """
#     Test form
#     """

#     cust = {
#         "first_name": "steve",
#         "last_name": "smith",
#         "telephone_number": "123",
#         "preferred_time_to_contact": "S",
#     }
#     prop = {
#         "annual_income": "2",
#         "loan_amount": "3",
#         "property_value": "4",
#         "mortgage_type": "RM",
#     }

#     custfull = {
#         "first_name": "steve",
#         "last_name": "smith",
#         "telephone_number": "123",
#         "preferred_time_to_contact": "S",
#         "annual_income": "2",
#         "loan_amount": "3",
#         "property_value": "4",
#         "mortgage_type": "RM",
#     }


#     cust_form = CustomerDetailsForm(cust).save(commit=False)
#     prop_form = PropertyDetailsForm(prop).save(commit=False)

#     customer_data = EnquiryProvider()
#     customer_data.add(cust)
#     customer_data.add(prop)
#     print(customer_data)

#     # enq = CustomerForm(custfull).save(commit=False)
#     # cust = Customer.objects.create(**cust, **prop)
#     # cust.save()
#     # print(cust)

#     return HttpResponse(customer_data)
