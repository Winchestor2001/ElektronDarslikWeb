from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from .forms import SignUpForm, SignInForm
from .models import *
from .serializers import QuizesSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from html2image import Html2Image


def home_page(request):
    context = {}
    return render(request, 'e_darslik/home.html', context)


def code_editor(request):
    context = {}
    return render(request, 'e_darslik/code_editor.html', context)


def themes_page(request):
    theme = Theme.objects.all()
    context = {'themes': theme}
    return render(request, 'e_darslik/themes_page.html', context)


def theme_detail(request, pk):
    theme = Theme.objects.get(id=pk)
    context = {'theme': theme}
    return render(request, 'e_darslik/theme_detail.html', context)


def practis_themes_page(request):
    practis_theme = PractisTheme.objects.all()
    context = {'practis_theme': practis_theme}
    return render(request, 'e_darslik/practis_theme.html', context)


def practis_page(request, slug):
    practis = Practis.objects.filter(practis_name__practis_slug=slug)
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
    post = Post.objects.get(id=pk)
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
            resources_with_link.append({'id': resource.pk, 'link': resource.link, 'name': resource.name})
    # for site in resources_with_link:
    #     site_name = site['name']
    #     save_pic_path = f'resource_img/{site_name}.png'
    #     hti.output_path = 'media/resource_img/'
    #     hti.screenshot(url=site['link'], save_as=f"{site_name}.png")
    #     res = Resource.objects.get(id=site['id'])
    #     res.img = save_pic_path
    #     res.save()

    context = {'books': books, 'exposures': exposures, 'useful_links': useful_links}
    return render(request, 'e_darslik/resources_page.html', context)


def glossary_page(request):
    context = {}
    return render(request, 'e_darslik/glossary_page.html', context)


def sign_up(request):
    register_form = SignUpForm()
    if request.method == 'POST':
        register_form = SignUpForm(request.POST)
        if register_form.is_valid():
            user = register_form.save()
            login(request, user)
            return redirect('home')

    context = {'register_form': register_form}
    return render(request, 'e_darslik/sign_up.html', context)


def sign_in(request):
    login_form = SignInForm()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return redirect('sign_in')

    context = {'login_form': login_form}
    return render(request, 'e_darslik/sign_in.html', context)


def logout_user(request):
    logout(request)
    return redirect('home')


@api_view(['GET'])
def quiz_api(request):
    quizes = Quizes.objects.all()
    serializer = QuizesSerializer(quizes, many=True)

    return Response(serializer.data)
