from django.shortcuts import render
from django.views import generic


# Create your views here.

class FrontPage(generic.ListView):
    template_name = 'front.html'


class SearchResultPage(generic.ListView):
    template_name = 'searchresult.html'


class SoftwareDetailPage(generic.DetailView):
    template_name = 'detail.html'
