"""
The main view file, handles all get and post requests to create an Enquiry.
"""

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CustomerDetailsForm, PropertyDetailsForm, CustomerForm
from .models import Customer
from .helpers.providers import EnquiryProvider


def index(request):
    """
    Site index.
    """

    return HttpResponse("Hello, world. You're at the user index.")

def testroute(request):
    """
    Test form
    """
    
    cust = {
        "first_name": "steve",
        "last_name": "smith",
        "telephone_number": "123",
        "preferred_time_to_contact": "S",
    }
    prop = {
        "annual_income": "2",
        "loan_amount": "3",
        "property_value": "4",
        "mortgage_type": "RM",
    }

    custfull = {
        "first_name": "steve",
        "last_name": "smith",
        "telephone_number": "123",
        "preferred_time_to_contact": "S",
        "annual_income": "2",
        "loan_amount": "3",
        "property_value": "4",
        "mortgage_type": "RM",
    }


    cust_form = CustomerDetailsForm(cust).save(commit=False)
    prop_form = PropertyDetailsForm(prop).save(commit=False)

    customer_data = EnquiryProvider()
    customer_data.add(cust)
    customer_data.add(prop)
    print(customer_data)

    # enq = CustomerForm(custfull).save(commit=False)
    



    # print(enq)


    # cust = Customer.objects.create(**cust, **prop)
    # cust.save()
    # print(cust)

    return HttpResponse(customer_data)


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
            property_details_data = form.cleaned_data
            customer_details_data = request.session["customer_details"]
            enquiry_data = EnquiryProvider()
            enquiry_data.add(property_details_data)
            enquiry_data.add(customer_details_data)

            print(f"enquiry_data: {enquiry_data}")

            enquiry = CustomerForm(enquiry_data.get_list()).save(commit=False)
            print(enquiry)



            # full_enquiry.address_id = address.address_id
            # foo = full_enquiry.save()
            
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


