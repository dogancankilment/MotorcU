from django.shortcuts import render_to_response
from django.core.context_processors import csrf


def home(request):
    c = {"request": request}
    c.update(csrf(request))
    return render_to_response("home/new-dashboard.html", c)


# def test_new_dashboard(request):
#     c = {"request": request}
#     c.update(csrf(request))
#
#     return render_to_response("home/new-dashboard.html", c)
