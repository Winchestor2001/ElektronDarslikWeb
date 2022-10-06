from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404

from .forms import SignUpForm, SignInForm
from .models import *
from .serializers import QuizesSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from html2image import Html2Image


def home_page(request):
    users = User.objects.all().count()
    resources = Resource.objects.filter(resource__name='Kitob')
    glossaries = Glossary.objects.all()
    practis_themes = PractisTheme.objects.all().count()
    themes = Theme.objects.all().count()
    posts = Post.objects.all()
    videos = Video.objects.all().count()
    context = {
        'users': users,
        'books': resources,
        'glossaries': glossaries[:3],
        'practis_themes': practis_themes,
        'themes': themes,
        'videos': videos,
        'posts': posts,
    }
    return render(request, 'e_darslik/home.html', context)


def code_editor(request):
    context = {}
    return render(request, 'e_darslik/code_editor.html', context)


def themes_page(request):
    theme = Theme.objects.all()
    context = {'themes': theme}
    return render(request, 'e_darslik/themes_page.html', context)


def theme_detail(request, pk):
    theme = get_object_or_404(Theme, id=pk)
    context = {'theme': theme}
    return render(request, 'e_darslik/theme_detail.html', context)


def practis_themes_page(request):
    practis_theme = PractisTheme.objects.all().order_by('practis_id')
    context = {'practis_theme': practis_theme}
    return render(request, 'e_darslik/practis_theme.html', context)


def practis_page(request, slug):
    practis = get_object_or_404(Practis, practis_name__practis_slug=slug)
    practis_theme = [item.practis_name.practis_name for item in practis]
    context = {'practis': practis, 'practis_theme': practis_theme[0]}
    return render(request, 'e_darslik/practis_page.html', context)


def quiz_page(request):
    context = {}
    if request.user.is_authenticated:
        return render(request, 'e_darslik/quiz_page.html', context)
    else:
        return redirect('sign_in')


def posts_page(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'e_darslik/posts.html', context)


def posts_detail(request, pk):
    post = get_object_or_404(Post, id=pk)
    post_viwe = post.post_views + 1
    post.post_views = post_viwe
    post.save()
    context = {'post': post}
    return render(request, 'e_darslik/post_detail.html', context)


def resources_page(request):
    hti = Html2Image()
    resources = Resource.objects.all()
    books = Resource.objects.filter(resource__name='Kitob')
    exposures = Resource.objects.filter(resource__name='Taqdimot')
    useful_links = Resource.objects.filter(resource__name='Internet resurs')
    resources_with_link = []
    for resource in resources:
        if not resource.link is None:
            if resource.img is None:
                resources_with_link.append({'id': resource.pk, 'link': resource.link, 'name': resource.name})
    for site in resources_with_link:
        site_name = site['name']
        save_pic_path = f'resource_img/{site_name}.png'
        hti.output_path = 'media/resource_img/'
        hti.screenshot(url=site['link'], save_as=f"{site_name}.png")
        res = get_object_or_404(Resource, id=site['id'])
        res.img = save_pic_path
        res.save()

    context = {'books': books, 'exposures': exposures, 'useful_links': useful_links}
    return render(request, 'e_darslik/resources_page.html', context)


def glossary_page(request):
    glossaries = Glossary.objects.all()
    context = {'glossaries': glossaries}
    return render(request, 'e_darslik/glossary_page.html', context)


# def sign_up(request):
#     register_form = SignUpForm()
#     if request.method == 'POST':
#         register_form = SignUpForm(request.POST)
#         if register_form.is_valid():
#             user = register_form.save()
#             login(request, user)
#             return redirect('home')
#
#     context = {'register_form': register_form}
#     return render(request, 'e_darslik/sign_up.html', context)
def sign_up(request):
    context = {}
    if request.method == 'POST':
        ism = request.POST['ism']
        familya = request.POST['familya']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        usr = User.objects.filter(username=username)
        if len(username) < 6:
            context['message'] = 'Username kamida 6 ta belgi bolsin!'
            context['col'] = 'danger'
        elif len(password) < 8:
            context['message'] = 'Password kamida 8 ta belgi  bolsin!'
            context['col'] = 'danger'
        elif password != password2:
            context['message'] = 'Passwordlar mos kelmadi!'
            context['col'] = 'danger'
        elif usr:
            context['message'] = 'Bu foydalanuvchi avval royxatdan otgan'
            context['col'] = 'danger'
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.first_name = ism
            user.last_name = familya
            user.save()
            return redirect('sign_in')
    return render(request, 'e_darslik/sign_up.html', context)


# def sign_in(request):
#     login_form = SignInForm()
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('home')
#         else:
#             return redirect('sign_in')
#
#     context = {'login_form': login_form}
#     return render(request, 'e_darslik/sign_in.html', context)
def sign_in(request):
    context = {}
    if request.method == 'POST':
        uname = request.POST['username']
        pwd = request.POST['password']
        usr = authenticate(username=uname, password=pwd)
        if usr:
            login(request, usr)
            return redirect('/')
        else:
            context['message'] = 'username yoki password xato!!!'
            context['col'] = 'danger'
    return render(request, 'e_darslik/sign_in.html', context)


def logout_user(request):
    logout(request)
    return redirect('home')


def video_page(request):
    videos = Video.objects.all()
    context = {'videos': videos}
    return render(request, 'e_darslik/videos_page.html', context)


@api_view(['GET'])
def quiz_api(request):
    quizes = Quizes.objects.all()
    serializer = QuizesSerializer(quizes, many=True)
    return Response(serializer.data)


def error_404_view(request, exception):
    return render(request, 'e_darslik/error_pages/error_404.html')

