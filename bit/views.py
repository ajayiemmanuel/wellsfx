from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

# Create your views here.
from .models import *
from .forms import CreateUserForm, CustomerForm

from .decorators import unauthenticated_user, allowed_users, admin_only



# Create your views here.

def about(request):
    context = {}
    return render (request, "bit/about.html", context)


def contact(request):
    context = {}
    return render (request, "bit/contact.html", context)


@login_required (login_url = "login")
def crypto_exchange(request):
    context = {}
    return render (request, "bit/crypto_exchange.html", context)


@login_required (login_url = "login")
def deposit(request):
    context = {}

    return render (request, "bit/deposit.html", context)


def faq(request):
    context = {}
    return render (request, "bit/faq.html", context)


@login_required (login_url = "login")
def status(request):
    context = {}
    return render (request, "bit/status.html", context)


@login_required (login_url = "login")
def home(request):
    context = {}
    return render (request, "bit/home.html", context)


def index(request):
    context = {}
    return render (request, "bit/index.html", context)


def LoginPage(request):
    if request.user.is_authenticated:
        return redirect ('home')
    else:
        if request.method == 'POST':
            username = request.POST.get ('username')
            password = request.POST.get ('password')

            user = authenticate (request, username = username, password = password)

            if user is not None:
                login (request, user)
                return redirect ('home')
            else:
                messages.info (request, 'Username OR password is incorrect')

    context = {}
    return render (request, "bit/login.html", context)


def logoutUser(request):
    logout (request)
    return redirect ('login')


@login_required (login_url = "login")
def plan1(request):
    context = {}
    return render (request, "bit/plan1.html", context)


@login_required (login_url = "login")
def plan2(request):
    context = {}
    return render (request, "bit/plan2.html", context)


@login_required (login_url = "login")
def plan3(request):
    context = {}
    return render (request, "bit/plan3.html", context)


@login_required (login_url = "login")
def plan4(request):
    context = {}
    return render (request, "bit/plan4.html", context)


def pricing(request):
    context = {}
    return render (request, "bit/pricing.html", context)


@login_required (login_url = "login")
def profile(request):
    customer = request.user.customer
    form = CustomerForm (instance = customer)

    if request.method == 'POST':
        form = CustomerForm (request.POST, request.FILES, instance = customer)
        if form.is_valid ():
            form.save ()

    context = {'form': form}
    return render (request, "bit/profile.html", context)


@login_required (login_url = "login")
def profit(request):
    context = {}
    return render (request, "bit/profit.html", context)


@login_required (login_url = "login")
def refer(request):
    context = {}
    return render (request, "bit/refer.html", context)


@unauthenticated_user
def registerPage(request):
    form = CreateUserForm ()
    if request.method == 'POST':
        form = CreateUserForm (request.POST)
        if form.is_valid ():
            user = form.save ()
            username = form.cleaned_data.get ('username')

            messages.success (request, 'Account was created for ' + username)

            return redirect ('login')

    context = {'form': form}
    return render (request, "bit/register.html", context)


def services(request):
    context = {}
    return render (request, "bit/services.html", context)


@login_required (login_url = "login")
def settings(request):
    context = {}
    return render (request, "bit/settings.html", context)


def terms(request):
    context = {}
    return render (request, "bit/terms.html", context)


@login_required (login_url = "login")
def transaction(request):
    context = {}
    return render (request, "bit/transaction.html", context)


@login_required (login_url = "login")
def withdraw(request):
    context = {}
    return render (request, "bit/withdraw.html", context)


def forgotten_password(request):
    context = {}
    return render (request, "bit/forgotten_password.html", context)


def reset_password(request):
    context = {}
    return render (request, "bit/reset_password.html", context)
