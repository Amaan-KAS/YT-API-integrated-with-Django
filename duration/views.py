from django.shortcuts import render
from django.shortcuts import HttpResponse, HttpResponseRedirect
from .forms import UserInfoForm
import requests
# Create your views here.

def home(request):
    return render(request,'home_page.html')

def about(request):
    return render(request, 'about_page.html')
    # return HttpResponse ("About - Yt Analysis")

def user_info_view(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = UserInfoForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # return HttpResponse("Lol")
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return render(request,"name.html",{"form": form.cleaned_data})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = UserInfoForm()

    return render(request, "home_page.html", {"form": form})
