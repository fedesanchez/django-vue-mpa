from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.db.models import Sum
from inertia import render
from .models import Client

PAGINATE_BY = 10


def index(request):
    return HttpResponseRedirect("/app/dashboard")

def dashboard(request):
    client_list = Client.objects.all()
    q = client_list.aggregate(Sum("amount"))
    paginator = Paginator(client_list, PAGINATE_BY)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    cards = [
        dict(
            title="Total clients",
            color="orange",
            icon="PeopleIcon",
            value=client_list.count(),
        ),
        dict(
            title="Account balance",
            color="green",
            icon="MoneyIcon",
            value=round(q.get("amount__sum")),
        ),
        dict(title="New sales", color="blue", icon="CartIcon", value="376"),
        dict(title="Pending contacts", color="teal", icon="ChatIcon", value="55"),
    ]
    return render(request, "Dashboard", props={"page_obj": page_obj, "cards": cards})


def forms(request):
    return render(request, "Forms", props={})


def cards(request):
    return render(request, "Cards", props={})


def charts(request):
    return render(request, "Charts", props={})


def buttons(request):
    return render(request, "Buttons", props={})


def modals(request):
    return render(request, "Modals", props={})


def tables(request):
    return render(request, "Tables", props={})


def login(request):
    return render(request, "Login", props={})


def create_account(request):
    return render(request, "CreateAccount", props={})


def forgot_password(request):
    return render(request, "ForgotPassword", props={})


def not_found(request):
    return render(request, "404", props={})


def blank(request):
    return render(request, "Blank", props={})
