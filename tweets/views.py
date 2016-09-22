from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View
from django.shortcuts import render
from .models import HashTag, Tweet
from .forms import SearchForm
import json

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

class Serach(View):
    """
    Search all tweets with query /search/?query=<query> URL
    """
    def get(self, request):
        form = SearchForm()
        params = dict()
        params["search"] = form
        return render(request, 'search.html', params)

    def post(self, request):
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            tweets = Tweet.objects.filter(text__icontains=query)
            context = Context({
                "query": query,
                "tweets": tweets
            })
            return_str = render_to_string(
                'partials/_tweet_search.html',
            context
            )
            return HttpResponse(json.dumps(return_str),
                                content_type="application/json")
        else:
            HttpResponseRedirect("/search")