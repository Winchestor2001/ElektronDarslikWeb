from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),

    path('themes/', views.themes_page, name='themes'),
    path('theme_detail/<int:pk>/', views.theme_detail, name='theme_detail'),

    path('video_page/', views.video_page, name='video_page'),
    path('posts_detail/<int:pk>', views.posts_detail, name='posts_detail'),

    path('resources_page/', views.resources_page, name='resources_page'),

    path('glossary_page/', views.glossary_page, name='glossary_page'),

    path('code_editor/', views.code_editor, name='code_editor'),

    path('practis_themes_page/', views.practis_themes_page, name='practis_themes_page'),
    path('practis_page/<slug:slug>', views.practis_page, name='practis_page'),

    path('quiz_page/', views.quiz_page, name='quiz_page'),

    path('quiz_api/', views.quiz_api, name='quiz_api'),

    path('sign_up/', views.sign_up, name='sign_up'),
    path('sign_in/', views.sign_in, name='sign_in'),
    path('logout/', views.logout_user, name='logout'),

]
