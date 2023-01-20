from . import views
from django.urls import path


urlpatterns = [
    path("", views.index, name='index'),
    path("forms/", views.forms, name='forms'),
    path("forum/", views.forum, name='forum'),
    path("support/", views.support, name='support'),
    path("admin/", views.admin, name='admin'),
]
