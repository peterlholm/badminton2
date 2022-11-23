from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings

# Create your views here.


def home(request):
    "home"
    return render(request, 'page.html')
    #return HttpResponse("Hello, Django!")

def service_worker(request):
    "service worker"
    sw_path = settings.BASE_DIR / "static/js" / "serviceworker.js"
    response = HttpResponse(open(sw_path, encoding='utf-8').read(), content_type='application/javascript')
    return response

def manifest(request):
    "service worker"
    sw_path = settings.BASE_DIR / "static" / "manifest.json"
    response = HttpResponse(open(sw_path, encoding='utf-8').read())
    return response
