from django.shortcuts import render_to_response
from django.core.context_processors import csrf


def fuel(request):
    if request.POST:
        if request.POST["mesafe"] and request.POST["tutar"]:
            mesafe = request.POST["mesafe"]
            tutar = request.POST["tutar"]

            tuketim = float(tutar) / float(mesafe)

            c = {"request": request,
                 "tuketim": tuketim}

            c.update(csrf(request))

            return render_to_response("fuel/index.html", c)

    c = {"request": request}
    c.update(csrf(request))

    return render_to_response("fuel/index.html", c)


def oilcare(request):
    c = {"request": request}
    c.update(csrf(request))

    return render_to_response("oil/index.html", c)