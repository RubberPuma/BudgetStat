from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render

from .forms import NewUserForm


# handle register request
def register_request(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    else:
        form = NewUserForm()
        if request.method == "POST":
            form = NewUserForm(request.POST)
            if form.is_valid():
                form.save()
                form.cleaned_data.get("username")

                return redirect("login")

        context = {"form": form}
        return render(request, "authentication/register.html", context)


# handle login form
def login_request(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    else:
        form = AuthenticationForm()
        if request.method == "POST":
            form = AuthenticationForm(request, data=request.POST)

            username = request.POST.get("username")
            password = request.POST.get("password")

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("dashboard")

        context = {"form": form}
        return render(request, "authentication/login.html", context)


# logout
def logout_request(request):
    logout(request)
    return redirect("login")


# temporary view for testing
@login_required(login_url="login")
def dashboard(request):
    context = {}
    return render(request, "authentication/dashboard.html", context)
