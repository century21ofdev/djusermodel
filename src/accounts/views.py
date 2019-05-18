from django.contrib.auth import login, get_user_model, logout
from django.shortcuts import render
from .forms import UserCreationForm, UserLoginForm
from django.http import HttpResponseRedirect

User = get_user_model()


# Create your views here.

def register(request):
    form = UserCreationForm(request.POST or None)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/login')
    return render(request, 'accounts/register.html', {'form': form})


def login_view(request, *args, **kwargs):
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        # form.save()
        username = form.cleaned_data.get('username')
        usr_obj = User.objects.get(username__iexact=username)
        login(request, usr_obj)
        return HttpResponseRedirect('/')
    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/login')
