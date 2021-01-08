"""
The main view file, handles all get and post requests to create an Enquiry.
"""

from django.shortcuts import render, redirect
from django.http import HttpResponse

# from .models import Enquiry
from .forms import CustomerDetailsForm, PropertyDetailsForm


def index(request):
    """
    Site index.
    """

    return HttpResponse("Hello, world. You're at the user index.")


def customer_details(request):
    """
    Customer Details form, first page of Enquiry.
    """

    if request.method =="POST":
        form = CustomerDetailsForm(request.POST, use_required_attribute=False)
        if form.is_valid():
            request.session["customer_details_form"] = form.cleaned_data
            return redirect("property_details")
    else:
        form = CustomerDetailsForm(use_required_attribute=False)

    return render(request, "customer_details.html", {"form": form})


# def customer_details(request):
#     if request.method == "POST":

#         details = {}

#         details['first-name'] = request.POST.get('first-name','')

#         invalid_input = list()

#         for i, k in details.items():
#             if k == "":
#                 invalid_input.append(i)

#         if invalid_input:
#             messages.add_message(
#                 request, messages.WARNING, f"Following information is required: {', '.join(invalid_input)}")
#             return render(request, "customer_details.html")

#         # new_user = User(firstname=details['first-name'],
#         #                  secondname=details['second-name'],
#         #                  country=details['country'])

#         # print(new_user)

#         # new_user.save()

#         return redirect("property_details")

#     return render(request, "customer_details.html")


def property_details(request):
    """
    Property Details form, second page of Enquiry.
    """

    if request.method =="POST":
        form = PropertyDetailsForm(request.POST, use_required_attribute=False)
        if form.is_valid():
            customer_details_form = request.session['customer_details_form']
            enquiry = form.save(commit=False)
            enquiry.first_name = customer_details_form['first_name']
            enquiry.last_name = customer_details_form['last_name']
            enquiry.address_building = customer_details_form['address_building']
            enquiry.address_street = customer_details_form['address_street']
            enquiry.address_town = customer_details_form['address_town']
            enquiry.address_county = customer_details_form['address_county']
            enquiry.address_postcode = customer_details_form['address_postcode']
            enquiry.telephone_number = customer_details_form['telephone_number']
            enquiry.email = customer_details_form['email']
            enquiry.preferred_time_to_call = customer_details_form['preferred_time_to_call']

            print(enquiry)

            enquiry.save()

            # new_enquiry = Enquiry(customer_details_form)
            # print(new_enquiry)
            # new_enquiry = Enquiry(property_details_form)
            # print(new_enquiry)

            return redirect("/")
    else:
        form = PropertyDetailsForm(use_required_attribute=False)

    return render(request, "property_details.html", {"form": form})
