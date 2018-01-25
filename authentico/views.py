from django.shortcuts import redirect, render, render_to_response
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from .forms import UserCreateForm, LoginForm
from django.utils.translation import ugettext as _


@login_required()
def motorcu_logout(request):
    auth.logout(request)
    return redirect(reverse('home'))


def motorcu_register(request, template_name="auth/register.html"):
    form = UserCreateForm(request.POST or None)

    if request.POST:
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse(motorcu_login))

    return render(request,
                  template_name,
                  {'form': form})


def motorcu_login(request):
    form = LoginForm(request.POST or None)

    if form.is_valid():
        user = authenticate(username=form.cleaned_data['username'],
                            password=form.cleaned_data['password'])

        if user:
                auth.login(request, user)

                return HttpResponseRedirect(reverse('home'))

        else:
            messages.error(request,
                           (_('Boyle bir kullanici sistemde kayitli degil')))

    return render_to_response('auth/login.html',
                  {'login_form': form})