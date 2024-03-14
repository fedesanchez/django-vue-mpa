from inertia import share
from django.urls import reverse


def inertia_share(get_response):

    def get_route(item):
        if not item.get("routes"):
            return dict(
                name=item.get("name"),
                icon=item.get("icon"),
                path=reverse(item.get("name")),
            )
        else:
            return dict(
                name=item.get("name"),
                icon=item.get("icon"),
                routes=[get_route(i) for i in item.get("routes")],
            )

    sidebar = [
        {
            "icon": "HomeIcon",
            "name": "Dashboard",
        },
        {
            "icon": "FormsIcon",
            "name": "Forms",
        },
        {
            "icon": "CardsIcon",
            "name": "Cards",
        },
        {
            "icon": "ChartsIcon",
            "name": "Charts",
        },
        {
            "icon": "ButtonsIcon",
            "name": "Buttons",
        },
        {
            "icon": "ModalsIcon",
            "name": "Modals",
        },
        {
            "icon": "TablesIcon",
            "name": "Tables",
        },
        {
            "name": "Pages",
            "icon": "PagesIcon",
            "routes": [
                {
                    "name": "Login",
                },
                {
                    "name": "CreateAccount",
                },
                {
                    "name": "ForgotPassword",
                },
                {
                    "name": "404",
                },
                {
                    "name": "Blank",
                },
            ],
        },
    ]
    routes = [get_route(item) for item in sidebar]

    def middleware(request):
        share(
            request,
            user=lambda: (
                None if request.user.is_anonymous else request.user
            ),  # evaluated lazily at render time
            routes=routes,
        )
        return get_response(request)

    return middleware
