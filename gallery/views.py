from django.shortcuts import render
from django.template import loader
from django.http import JsonResponse, HttpResponse

# Create your views here.
def index(request):
    template = loader.get_template('gallery/index.html')
    context = {'hello': 'world'}
    return HttpResponse(template.render(context, request))

