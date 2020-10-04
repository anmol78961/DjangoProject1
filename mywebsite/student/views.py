# from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.


def index(request):
    name = "Yuvraj"
    return render(request, 'index.html', {"name": name})
    # return HttpResponse("Hi this is my new website")


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
    return render(request, 'contact.html', {"name": name, "email": email, "subject": subject, "message": message})
