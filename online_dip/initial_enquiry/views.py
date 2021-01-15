""" The main view file, handles all get and post requests to create an Enquiry. """

from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, UpdateView
from django.conf import settings
from django.http import JsonResponse
from .forms import CustomerDetailsForm, PropertyDetailsForm, EnquiryForm
from .models import Enquiry
from .helpers.providers import EnquiryProvider
from .helpers.mailer import EmailSender


def customer_details(request):
    """ Customer Details form, first page of Enquiry """

    # Set initial response code for testing purposes
    response_code = 200

    if request.method == "POST":
        form = CustomerDetailsForm(request.POST, use_required_attribute=False)

        if form.is_valid():
            # Save to the session to be retreived later
            request.session["customer_details"] = form.cleaned_data
            return redirect("property_details")
        response_code = 400
    else:
        form = CustomerDetailsForm(use_required_attribute=False)

    context = {
        "form": form
    }
    return render(request, "customer_details.html", context, status=response_code)


def property_details(request):
    """ Property Details form, second page of Enquiry """

    # Set initial response code for testing purposes
    response_code = 400

    # Session check to verify journey integrity
    if not "customer_details" in request.session:
        return redirect("customer_details")

    if request.method =="POST":
        # Smell: need to validate ltv value
        # doesnt need passing in because ill receive the loan value and the property value!
        # can just pass values into what will be the LtvValidator
        form = PropertyDetailsForm(request.POST, use_required_attribute=False)
        if form.is_valid():
            property_details_data = form.cleaned_data
            customer_details_data = request.session["customer_details"]

            # Consolidate data from other pages to prep for db entry
            enquiry_data = EnquiryProvider()
            enquiry_data.add(property_details_data)
            enquiry_data.add(customer_details_data)
            completed_data = enquiry_data.get_list()

            enquiry = EnquiryForm(completed_data)

            # Perform final validation, redirect to start if there is invalid data
            if not enquiry.is_valid():
                return redirect("customer_details")

            enquiry.save()

            # Check if email functionality is enabled
            # Send a confirmation email to the customer
            email_enabled = settings.ENABLE_EMAIL
            if email_enabled:
                mailer = EmailSender(enquiry_data.get_list(), email_enabled)
                mailer.send()

            return redirect("thank_you")

    else:
        # Generate a new form page and set response code
        form = PropertyDetailsForm(use_required_attribute=False)
        response_code = 200

    context = {
        "form": form
    }
    return render(request, "property_details.html", context, status=response_code)


def calculate_ltv(request):

    # convert to int?
    try:
        loan_amount = int(request.GET.get('loanamount', None))
        property_value = int(request.GET.get('propertyvalue', None))
    except:
        loan_amount = 0
        property_value = 0

    # Calculate ratio of loan to value, then cap at 0.1 (≡100%)
    ltv_result = min(float(loan_amount) / float(property_value), 1.0)
    ltv_percentage = "{:.0%}".format(ltv_result)

    if ltv_result <= 0.5:
        ltv_css = "ltv_acceptable"
        visibility_css = "hidden"
    else:
        ltv_css = "ltv_unacceptable"
        visibility_css = "visible"

    data = {
        'ltv': ltv_percentage,
        'ltv_css': ltv_css,
        'visibility_css': visibility_css,
    }
    return JsonResponse(data)

def thank_you(request):
    """ Page displayed on submission complete """

    # Session check to verify journey integrity
    if not "customer_details" in request.session:
        return redirect("customer_details")

    # Clean the session
    del request.session["customer_details"]

    return render(request, "thank_you.html")


class EnquiryListView(LoginRequiredMixin, ListView): # pylint: disable=too-many-ancestors
    """ Class-based view, to show the List of Enquiries """

    model = Enquiry
    template_name = "adviser/enquiry_list.html"
    context_object_name = "customers"

    # Only return customers who have not yet been contacted
    queryset = Enquiry.objects.filter(has_been_contacted="False")


class EnquiryUpdateView(LoginRequiredMixin, UpdateView):
    """ Class-based view, to show a detailed view of a chosen Enquiry """

    model = Enquiry
    template_name = "adviser/enquiry_form.html"
    fields = [ 'has_been_contacted' ]


def error_404(request, exception):
    """ Custom 404 error handler """
    return render(request, 'error/404.html', status=404)

def error_500(request):
    """ Custom 500 error handler """
    return render(request, 'error/500.html', status=500)
