from . import views
from django.urls import path


urlpatterns = [
    path("", views.index, name='index'),
    path("forms/", views.forms, name='forms'),
    path("forum/", views.forum, name='forum'),
    path("support/", views.support, name='support'),
    path("portal/admin/", views.admin, name='admin'),
    path("portal/admin/overview/", views.adminOverview, name='admin_overview'),
    path("portal/admin/tickets/", views.adminTickets, name='admin_tickets'),
    path("portal/admin/tickets/add/", views.adminTicketAdd, name='admin_tickets_add')
]
