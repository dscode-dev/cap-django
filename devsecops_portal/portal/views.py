from django.shortcuts import render
import requests
import json

def index(request):
    return render(request, 'portal/pages/dashboard.html', {"teste": 'response.text'})

def forms(request):
    return render(request, 'portal/pages/forms.html', {
        "page": "forms"
    })

def forum(request):
    return render(request, 'portal/pages/forum.html', {
        "page": "forum"
    })

def support(request):
    return render(request, 'portal/pages/support.html', {
        "page": "support"
    })

def admin(request):
    pass

def adminOverview(request):
    res_notes = requests.get('http://localhost:8080/api/v1/notes')
    res_idErros = requests.get('http://localhost:8080/api/v1/errors')
    res_customers = requests.get('http://localhost:8080/api/v1/customers')
    res_cases = requests.get('http://localhost:8080/api/v1/cases')
    return render(request, 'portal/segments/admin_page/admin_overview.html', {
        "notes": res_notes.json(),
        "id_errors": res_idErros.json(),
        "customers": res_customers.json(),
        "cases": res_cases.json(),
        "page": "admin"
    })

def adminTickets(request):
    res_tickets = requests.get('http://localhost:8080/api/v1/tickets/list')
    return render(request, 'portal/segments/admin_page/admin_tickets.html', {
        "tickets": res_tickets.json(),
        "page": "admin"
    })

