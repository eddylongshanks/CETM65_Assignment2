"""
The main view file, handles all get and post requests to create an Enquiry.
"""

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CustomerDetailsForm, PropertyDetailsForm
from .models import Customer, Address


def index(request):
    """
    Site index.
    """

    return HttpResponse("Hello, world. You're at the user index.")

def customer_details(request):
    """
    Customer Details form, first page of Enquiry.
    """

    if request.method == "POST":
        form = CustomerDetailsForm(request.POST, use_required_attribute=False)
        if form.is_valid():
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

    if request.method =="POST":
        form = PropertyDetailsForm(request.POST, use_required_attribute=False)
        if form.is_valid():
            customer_details_form = CustomerDetailsForm(request.session["customer_details"])
            address = Address(customer_details_form.save())


            full_enquiry = Customer(customer_details_form, form)
            # full_enquiry.address_id = address.address_id
            # foo = full_enquiry.save()
            print(address)
            
            # full_enquiry.save()
       


            # new_enquiry = Enquiry(customer_details_form)
            # print(new_enquiry)
            # new_enquiry = Enquiry(property_details_form)
            # print(new_enquiry)

            return redirect("/")
    else:
        form = PropertyDetailsForm(use_required_attribute=False)

    return render(request, "property_details.html", {"form": form})





# def customer_details(request):
#     if request.method == "POST":        
#         customer = Customer(request.POST)

#         customer.address

#         print(customer_form)

#         # customer_form.save()
#         return redirect("index")

#     customer_form = Customer()

#     context = {
#         "form": customer_form
#     }

#     return render(request, "customer_details.html", context)


    


# def customer_details_old(request):
#     """
#     Customer Details form, first page of Enquiry.
#     """

#     if request.method == "POST":
#         form = CustomerDetailsForm(request.POST, use_required_attribute=False)
#         if form.is_valid():
#             request.session["customer_details_form"] = form.cleaned_data
#             return redirect("property_details")
#     else:
#         form = CustomerDetailsForm(use_required_attribute=False)

#     context = {
#         "form": form
#     }

#     return render(request, "customer_details.html", context)












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


