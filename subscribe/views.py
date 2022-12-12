from django.shortcuts import render, redirect
from subscribe.models import Subscribe
from subscribe.forms import SubscribeForm
from django.urls import reverse
# Create your views here.

def subscribe(request):
    subscribe_form = SubscribeForm()

    # In case of not using Django facility:
    # email_error = ""
    # if request.POST:
    #     first_name = request.POST['firstname']
    #     last_name = request.POST['lastname']
    #     email = request.POST['email']
    #     print(f"post REQ: {email}")
    #     if email == "":
    #         email_error = "Email field is empty"
    #     subscribe = Subscribe(first_name = first_name, last_name = last_name, email = email)
    #     subscribe.save()

    # Using Django:
    if request.POST:
        subscribe_form = SubscribeForm(request.POST)
        if subscribe_form.is_valid():
            print("Valid Form!!")
            print(subscribe_form.cleaned_data)
            first_name = subscribe_form.cleaned_data["first_name"]
            last_name = subscribe_form.cleaned_data["last_name"]
            email = subscribe_form.cleaned_data["email"]
            subscribe = Subscribe(first_name = first_name, last_name = last_name, email = email)
            subscribe.save()
            return redirect(reverse("thank_you"))
    context = {"form":subscribe_form}
    return render(request, 'subscribe/subscribe.html', context)


def thank_you(request):
    context = {}
    return render(request, 'subscribe/thank_you.html', context)
