from django.urls import path
from dashboard import views

urlpatterns = [
    path("", views.index, name="index"),
    path("dashboard", views.dashboard, name="Dashboard"),
    path("forms", views.forms, name="Forms"),
    path("charts", views.charts, name="Charts"),
    path("cards", views.cards, name="Cards"),
    path("modals", views.modals, name="Modals"),
    path("tables", views.tables, name="Tables"),
    path("buttons", views.buttons, name="Buttons"),
    path("login", views.login, name="Login"),
    path("create-account", views.create_account, name="CreateAccount"),
    path("forgot-password", views.forgot_password, name="ForgotPassword"),
    path("404", views.not_found, name="404"),
    path("blank", views.blank, name="Blank"),
]
