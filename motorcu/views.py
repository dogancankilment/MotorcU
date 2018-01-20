from django.shortcuts import render_to_response
from django.core.context_processors import csrf


def home(request):
    return render_to_response("home/index.html")