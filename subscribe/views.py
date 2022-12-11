from django.shortcuts import render
from subscribe.models import Subscribe
# Create your views here.

def subscribe(request):
    email_error = ""
    if request.POST:
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        email = request.POST['email']
        print(f"post REQ: {email}")
        if email == "":
            email_error = "Email field is empty"

        subscribe = Subscribe(first_name = first_name, last_name = last_name, email = email)
        subscribe.save()
    context = {"email_error": email_error}
    return render(request, 'subscribe/subscribe.html', context)
