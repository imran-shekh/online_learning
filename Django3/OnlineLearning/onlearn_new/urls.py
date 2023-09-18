from django.contrib import admin
from django.urls import path

# we also need to know about this one or learn
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path("contact", views.contact, name='contact'),
    path("signup", views.sign_up , name='signup'),
    path("login", views.login , name='login'),
    path("logout", views.logout , name='logout'),
    path('course/<str:slug>/', views.course , name='course'),
]


# This codes comes from the previous project so you need to copy this code from here or learn

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)