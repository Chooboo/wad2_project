from django.shortcuts import render


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


def login(request):
    context_dict = {}
    return render(request, 'musicquiz/login.html', context=context_dict)


def register(request):
    context_dict = {}
    return render(request, 'musicquiz/register.html', context=context_dict)


def my_account(request):
    context_dict = {}
    return render(request, 'musicquiz/my-account.html', context=context_dict)


def error(request):
    context_dict = {}
    return render(request, 'musicquiz/error.html', context=context_dict)
