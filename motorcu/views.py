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
    if request.POST:
        if request.POST["hava"]:
            hava_sicakligi = request.POST["hava"]

            if int(hava_sicakligi) > -10 and int(hava_sicakligi) < 40:
                secim = "10-40"
            elif int(hava_sicakligi) < -10:
                secim = "5-40"
            elif int(hava_sicakligi) > 40 :
                secim = "10-50"
            else:
                secim = "10-40"

            c = {"request": request,
                 "secim": secim}

            c.update(csrf(request))

            return render_to_response("oil/index.html", c)

    c = {"request": request}
    c.update(csrf(request))

    return render_to_response("oil/index.html", c)


def tire(request):
    if request.POST:
            if request.POST["motosikletkg"] and request.POST["yolcukg"]:
                motosiklet_kg = request.POST["motosikletkg"]
                yolcu_kg = request.POST["yolcukg"]

                toplam_kg = int(motosiklet_kg) + int(yolcu_kg)

                if int(toplam_kg) > 200 and int(toplam_kg) < 300:
                    on_lastik = "25-27"
                    arka_lastik = "32-34"
                elif int(toplam_kg) > 300 and int(toplam_kg) < 400:
                    on_lastik = "27-29"
                    arka_lastik = "34-37"
                elif int(toplam_kg) > 400:
                    on_lastik = "28-30"
                    arka_lastik = "36-38"
                else:
                    on_lastik = "Hesaplanamadi"
                    arka_lastik = "Hesaplanamadi"

            c = {"request": request,
                 "onlastik": on_lastik,
                 "arkalastik": arka_lastik}

            c.update(csrf(request))

            return render_to_response("tire/tire-pressure-calculator.html", c)

    c = {"request": request}
    c.update(csrf(request))

    return render_to_response("tire/tire-pressure-calculator.html", c)