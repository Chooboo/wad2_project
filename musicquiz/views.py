from django.shortcuts import render, redirect
from django.db.models import Count

from musicquiz.forms import UserProfileForm
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, AnonymousUser
from musicquiz.models import UserProfile, MusicCategory, Comment, QuizQuestion


def index(request):
    return render(request, 'musicquiz/index.html')


def about(request):
    return render(request, 'musicquiz/about.html')


def categories(request):
    context_dict = {'categories': MusicCategory.objects.all()}
    return render(request, 'musicquiz/categories.html', context=context_dict)


# View for rendering the category page (or parts of it)
def show_category(request, category_slug):
    context_dict = {}

    # If a POST request is made, it's an ajax call, render only the comments component
    if request.method == 'POST':
        category = MusicCategory.objects.get(slug=category_slug)
        user = User.objects.get(id=request.POST['user-id'])
        author = UserProfile.objects.get(user=user)

        comment = Comment.objects.create(category=category, author=author)
        comment.body = request.POST['body']
        comment.save()
        return render_comments(request, category_slug)

    # If a request is not POST, render the whole page as it should be
    else:
        try:
            category = MusicCategory.objects.get(slug=category_slug)
            comments = Comment.objects.filter(category=category) \
                                      .annotate(like_count=Count('likes')) \
                                      .order_by('-like_count')
            context_dict['category'] = category
            context_dict['comments'] = comments

        except MusicCategory.DoesNotExist:
            context_dict['category'] = None
            context_dict['comments'] = None

        return render(request, 'musicquiz/category.html', context=context_dict)


# Removes the comment when triggered
def remove_comment(request, category_slug, comment_id):
    Comment.objects.filter(id=comment_id).delete()
    return render_comments(request, category_slug)


# Manages liking/disliking. Adds or removes users from the comment's likes ManyToMany field
def toggle_like(request, category_slug, comment_id):
    comment = Comment.objects.get(id=comment_id)
    userprofile = User.objects.get(id=request.GET['user-id']).userprofile
    if userprofile in comment.likes.all():
        comment.likes.remove(userprofile)
    else:
        comment.likes.add(userprofile)

    return render_comments(request, category_slug)


# Helper function that renders the comments component, useful for AJAX calls
def render_comments(request, category_slug):
    context_dict = {}
    # Fetch the category based on the slug and its corresponding comments
    try:
        category = MusicCategory.objects.get(slug=category_slug)
        comments = Comment.objects.filter(category=category) \
            .annotate(like_count=Count('likes')) \
            .order_by('-like_count')
        context_dict['category'] = category
        context_dict['comments'] = comments
    except MusicCategory.DoesNotExist:
        context_dict['category'] = None
        context_dict['comments'] = None

    return render(request, 'musicquiz/components/comments.html', context=context_dict)


def quiz(request):
    return render(request, 'musicquiz/quiz.html')


def show_question(request, question_id):
    context_dict = {}
    try:
        question = QuizQuestion.objects.get(question_id=int(question_id))
        context_dict['question'] = question
        context_dict['points'] = request.GET.get('points')
    except QuizQuestion.DoesNotExist:
        context_dict['question'] = None

    return render(request, 'musicquiz/components/quiz-question.html', context=context_dict)


def quiz_results(request, points):
    points = int(points)
    if points < 20:
        category_slug = 'innocent-baby'
    elif points < 27:
        category_slug = 'the-awakening'
    elif points < 35:
        category_slug = 'the-child'
    elif points < 35:
        category_slug = 'the-faded-adult'
    else:
        category_slug = 'transcendence'

    # If user is logged in, set his category
    if request.user.is_authenticated:
        category = MusicCategory.objects.get(slug=category_slug)
        userprofile = UserProfile.objects.get(user=request.user)
        userprofile.category = category
        userprofile.save()

    return redirect(reverse('musicquiz:category', args=[category_slug]))


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('logout'))


@login_required
def register_profile(request):
    form = UserProfileForm()
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            user_profile = form.save(commit=False)
            user_profile.user = request.user
            user_profile.save()
            return redirect('musicquiz:index')
        else:
            print(form.errors)
    context_dict = {'form': form}
    return render(request, 'musicquiz/profile_registration.html', context_dict)


def profile(request, username):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return redirect('index')

    userprofile = UserProfile.objects.get_or_create(user=user)[0]
    form = UserProfileForm({
        'picture': userprofile.picture
    })

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=userprofile)

        if form.is_valid():
            form.save(commit=True)
            return redirect('musicquiz:profile', user.username)

        else:
            print(form.errors)

    return render(request, 'musicquiz/profile.html', {'userprofile': userprofile, 'selecteduser': user, 'form': form})


def error(request):
    return render(request, 'musicquiz/error.html')
