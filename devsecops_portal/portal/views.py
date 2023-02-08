import json
import requests
from datetime import date
from django.shortcuts import render
from django.http import HttpResponseRedirect

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
    res_notes = requests.get('http://localhost:8181/api/v1/notes')
    res_idErros = requests.get('http://localhost:8181/api/v1/errors')
    res_customers = requests.get('http://localhost:8181/api/v1/customers')
    res_cases = requests.get('http://localhost:8181/api/v1/cases')
    return render(request, 'portal/segments/admin_page/admin_overview.html', {
        "notes": res_notes.json(),
        "id_errors": res_idErros.json(),
        "customers": res_customers.json(),
        "cases": res_cases.json(),
        "page": "admin"
    })


def adminTickets(request):
    res_tickets = requests.get('http://localhost:8181/api/v1/tickets/list')
    return render(request, 'portal/segments/admin_page/admin_tickets.html', {
        "tickets": res_tickets.json(),
        "page": "admin"
    })


def adminTicketAdd(request):
    try:
        res = requests.get('http://localhost:8181/api/v1/tickets/list')
        length_tickets = len(res.json()) +1
    except Exception:
        pass
    
    payload = {
        "id": f"#{date.today()}-{length_tickets}",
        "description": str(request.POST.get("desc")).title(),
        "customer": str(request.POST.get("client")).upper(),
        "owner": str(request.POST.get("owner")).title(),
        "priority": str(request.POST.get("priority")).title(),
        "status": str(request.POST.get("status")).title(),
        "create_date": f"{date.today()}"
    }

    HEADERS = {"Content-Type": "application/json"}
    res = requests.post("http://localhost:8181/api/v1/add/tickets/list", json=payload, headers=HEADERS)

    #res_tickets = requests.get('http://localhost:8181/api/v1/tickets/list')
    return HttpResponseRedirect('/portal/admin/tickets/')
