from inertia import render
from django.http import HttpRequest, HttpResponse

def index(request, page):
    return render(request, page, props={})
