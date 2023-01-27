from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'portal/pages/dashboard.html', {
        "page": "dash"
    })

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
    return render(request, 'portal/pages/admin.html', {
        "page": "admin",
        "count": +3.35,
        "count_two": +6.28,
        "count_three": -1.5,
        "count_four": +10.35,
    })

