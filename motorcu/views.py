from django.shortcuts import render_to_response
from django.core.context_processors import csrf


def home(request):
    if request.POST:
        if request.POST["mesafe"] and request.POST["tutar"]:
            mesafe = request.POST["mesafe"]
            tutar = request.POST["tutar"]

            tuketim = float(tutar) / float(mesafe)

            c = {"request": request,
                 "tuketim": tuketim}

            c.update(csrf(request))

            return render_to_response("index.html", c)

    c = {"request": request}
    c.update(csrf(request))

    return render_to_response("index.html", c)