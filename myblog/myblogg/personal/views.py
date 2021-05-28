from django.shortcuts import render
from useraccount.models import Account


def home_screen_view(request):
    context = {}
    # list_of_values = []
    # list_of_values.append("1 entry")
    # list_of_values.append("2 entry")
    # list_of_values.append("3 entry")
    # context['list_of_values'] = list_of_values

    accounts = Account.objects.all()
    context['users'] = accounts
    return render(request, "personal/home.html", context)