from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages


def index(request):
    return HttpResponse("Hello, world. You're at the user index.")

# def customer_details(request):
#     return render(request, "customer_details.html")


def customer_details(request):
    if request.method == "POST":

        details = {}

        details['first-name'] = request.POST.get('first-name','')

        invalid_input = list()

        for i, k in details.items():
            if k == "":
                invalid_input.append(i)
        
        if invalid_input:
            messages.add_message(
                request, messages.WARNING, f"Following information is required: {', '.join(invalid_input)}")
            return render(request, "customer_details.html")

        # new_user = User(firstname=details['first-name'],
        #                  secondname=details['second-name'],
        #                  country=details['country'])

        # print(new_user)
        
        # new_user.save()

        return redirect("property_details")

    return render(request, "customer_details.html")


def property_details(request):
    if request.method == "POST":

        details = {}

        details['annual-income'] = request.POST.get('annual-income','')

        return redirect("/")

    return render(request, "property_details.html")