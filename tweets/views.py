from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import render
from .models import HashTag

class Index(View):
    def get(self, request):
        params = {}
        params["name"] = "Django"
        return render(request, 'base.html', params)

    def post(self, request):
        return HttpResponse("I am called from a post Request")

class HashTagCloud(View):
    """
    Hash Tag page reachable from /hashtag/<hashtag> URL
    """
    def get(self, request, hashtag):
        params = dict()
        hashtag = HashTag.objects.get(name=hashtag)
        params["tweets"] = hashtag.tweet.all()
        return render(request, 'hashtag.html', params)