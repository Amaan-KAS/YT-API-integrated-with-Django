from django.shortcuts import render
from django.shortcuts import HttpResponse, HttpResponseRedirect
from .forms import UserInfoForm
from ytAnalysis.settings import youtube_api_key
from humanize import naturaltime
from datetime import datetime
import json
import requests
import pytz
# Create your views here.

def home(request):
    return render(request,'home_page.html')

def about(request):
    return render(request, 'about_page.html')
    # return HttpResponse ("About - Yt Analysis")

def modify_response(response):
    for item in response["items"]:
        published_at = item['contentDetails']['videoPublishedAt']
        published_datetime = datetime.strptime(published_at, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=pytz.UTC)
        current_datetime = datetime.now(pytz.UTC)
        time_difference = current_datetime - published_datetime
        formatted_time_difference = naturaltime(time_difference)
        item['contentDetails']['videoPublishedAt'] = formatted_time_difference
    return response

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
            playlist_search_url = 'https://www.googleapis.com/youtube/v3/playlistItems'
            url = form.cleaned_data['url_link']
            # url_link_playlistId = url.url_link
            url_link_playlistId = url.split("list=")
            print(url_link_playlistId[1])
            param = {
                'part':"contentDetails,snippet",
                'playlistId': url_link_playlistId[1],
                'maxResults':25,
                'key' :youtube_api_key
            }
            response = requests.get(playlist_search_url, params=param)
            # response = modify_response(response.json)
            data = response.json()
            for item in data['items']:
                published_at = item['contentDetails']['videoPublishedAt']
                published_datetime = datetime.strptime(published_at, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=pytz.UTC)
                current_datetime = datetime.now(pytz.UTC)
                time_difference = current_datetime - published_datetime
                formatted_time_difference = naturaltime(time_difference)
                item['contentDetails']['videoPublishedAt'] = formatted_time_difference
                print(item['contentDetails']['videoPublishedAt'])

            return render(request,"playlist.html",{"form": data})
    # if a GET (or any other method) we'll create a blank form
    else:
        form = UserInfoForm()

    return render(request, "home_page.html", {"form": form})

