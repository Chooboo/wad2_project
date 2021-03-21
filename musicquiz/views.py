from django.shortcuts import render, redirect
from musicquiz.forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def index(request):
    context_dict = {}
    return render(request, 'musicquiz/index.html', context=context_dict)


def about(request):
    context_dict = {}
    return render(request, 'musicquiz/about.html', context=context_dict)


def categories(request):
    context_dict = {}
    return render(request, 'musicquiz/categories.html', context=context_dict)


def quiz(request):
    context_dict = {}
    return render(request, 'musicquiz/quiz.html', context=context_dict)

           
def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            
            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            profile.save()

            registered = True
            messages.success(request, f'Account created!')
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    ctx = {
        'user_form': user_form,
        'profile_form': profile_form,
        'registered': registered}

    return render(request, 'musicquiz/register.html', context=ctx)


def user_login(request):
    error = None
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                error = "Your account is disabled."

        else:
            print("Invalid login details: {0}, {1}".format(username, password))
            error = "Invalid login details supplied."

    return render(request, 'musicquiz/login.html', {'error': error})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
    
@login_required
def my_account(request):
    context_dict = {}
    return render(request, 'musicquiz/my_account.html', context=context_dict)


def error(request):
    context_dict = {}
    return render(request, 'musicquiz/error.html', context=context_dict)
