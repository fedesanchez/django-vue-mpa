from inertia import render


def index(request):
    return render(request, "Dashboard", props={})


def dashboard(request):
    return render(request, "Dashboard", props={})


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
