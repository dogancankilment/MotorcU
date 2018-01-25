from django.shortcuts import redirect, render, render_to_response
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from .forms import UserCreateForm, LoginForm


@login_required()
def motorcu_logout(request):
    auth.logout(request)
    return redirect(reverse('home'))


def motorcu_register(request, template_name="auth/register.html"):
    form = UserCreateForm(request.POST or None)

    if request.POST:
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse(motorcu_login_url))

    return render(request,
                  template_name,
                  {'form': form})