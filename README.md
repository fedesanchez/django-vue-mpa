# Django + Vue Multi Page Application (MPA)

> A common myth is that an SPA is necessary to use a front-end framework like Vue or React.

When developers talk about using Vue with Django, they often talk about building a Vue SPA and a Django API, hosted on separate servers. This is also known as decoupled front and back ends.

Inspired by this article [
You don't have to build a separate app to use Vue with Django](https://ctrlzblog.com/add-vue-to-your-django-templates-with-vite/) i decided to test if you can get the full benefits of a JavaScript development environment without creating a separate codebase for your frontend.

## Usage

clone repo and:

```bash
cd <repo folder>
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

and in other terminal session:

```bash
npm install
npm run dev
```

Then go to [http://localhost:8080/app/](http://localhost:8080/app/)

# The journey (This is a work in progress)

## Necessary Features

The goal is to have the same benefits as if we were using _Django Template Engine_ but with a modern frontend framework like vue.

It has to have this features:

-   1. Being able to use a base layout (Header, Footer, Sidebar...)
-   2. Individual views within the layout, with parameters or props.
-   3. Have a unified routing system (django).
-   4. Inherit view permissions like authenticated user.

### 1. Being able to use a base layout.

**First: The setup**

Taking the aforementioned article as a reference, I am going to use Vue as a frontend framework using Vite and django_vite.

I'm going to try to integrate this [vue dashboard template](https://github.com/fedesanchez/windmill-dashboard-vue) with django, wich also has tailwind and other dependencies.

To make this short:

-   Create a django project (in my case its called core)
-   Create a django app (dashboard) and add it to INSTALLED_APPS
-   Install django_vite and add it to INSTALLED_APPS and add some django_vite settings (core/settings.py)

```python
# Where ViteJS assets are built.
DJANGO_VITE_ASSETS_PATH = BASE_DIR / "static" / "dist"
# If use HMR or not.
DJANGO_VITE_DEV_MODE = DEBUG
# Name of static files folder (after called python manage.py collectstatic)
STATIC_ROOT = BASE_DIR / "collectedstatic"
# Include DJANGO_VITE_ASSETS_PATH into STATICFILES_DIRS to be copied inside
# when run command python manage.py collectstatic
STATICFILES_DIRS = [DJANGO_VITE_ASSETS_PATH]
```

-   Copy src folder from [vue dashboard template](https://github.com/fedesanchez/windmill-dashboard-vue) to static/src/js
-   Add a [package.json](), [vite.config.cjs]() and tailwind.[config.js](), [postcss.config.cjs]() for tailwind. Just copy the files in this repo and make sure that the path of your static folder its right.

The most important part is to define [main.js]() as the entrypoint in [vite.config.js]()

```js
input: {
	main: resolve("./static/src/js/main.js"),
},
```

Then just run npm install and check for errors

### The problem:

At this point i realized the first big problem: With this approche i would have to do a Vue _CreateApp_ for each django view and i cannot use a single layout where a part of that layout changes for every view .... not great.

### The Solution: [inertiajs](https://inertiajs.com/)

This is the last piece of the puzzle, the one that makes everything fits together.

> Inertia allows you to create fully client-side rendered, single-page apps, without the complexity that comes with modern SPAs. It does this by leveraging existing server-side patterns that you already love.

And from the [community adapters page](https://inertiajs.com/community-adapters) we can find [inertia-django](https://pypi.org/project/inertia-django/).

-   Just install with pip, add _inertia_ to INSTALLED_APPS and add some settings:

```python
INERTIA_LAYOUT = 'base.html'

MIDDLEWARE = [
  # django middleware,
  'inertia.middleware.InertiaMiddleware',
  # your project's middleware,
]

#CSRF
CSRF_HEADER_NAME = 'HTTP_X_XSRF_TOKEN'
CSRF_COOKIE_NAME = 'XSRF-TOKEN'
```

-   Now we need to create a base.html file inside templates folder with this content:

```html
{% load django_vite %} {% vite_hmr_client %} {% vite_asset 'js/main.js' %}
<body>
	{% block inertia %}{% endblock %}
</body>
```

-   Almost there, now we need to add inertia to our frontend

```js
npm install @inertiajs/vue3
```

-   And change the content of [main.js]() to:

```js
import "./index.css";
import { createApp, h } from "vue";
import { createInertiaApp } from "@inertiajs/vue3";

createInertiaApp({
	resolve: (name) => {
		const pages = import.meta.glob("./pages/**/*.vue", { eager: true });
		return pages[`./pages/${name}.vue`];
	},
	setup({ el, App, props, plugin }) {
		createApp({ render: () => h(App, props) })
			.use(plugin)
			.mount(el);
	},
});
```

-   Now we can start our frontend server

```js
npm install @inertiajs/vue3
```

### 2. Individual views within the layout, with parameters or props.

At this point there is a bunch of errors but the most important is **RouterLink** (vue-router) and we have to use **Link** (inertia) instead.
Then we need to import Layout component on every .vue file inside [static/src/js/pages]() folder and wrap the content inside Layout, for instance:

```html
<script setup>
	import Layout from "@/containers/Layout.vue";
	import PageTitle from "@/components/Typography/PageTitle.vue";
</script>

<template>
	<Layout>
		<PageTitle>Blank</PageTitle>
	</Layout>
</template>
```

Finally we can add a view in django that points to any of our Vue pages.'

```python
#core/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', include('dashboard.urls'))
]
```

```python
#dashboard/urls.py

from django.urls import path
from dashboard.views import index

urlpatterns = [
    path('test', index, name="index")
]
```

We need to use **render** from inertia instead of django!

```python
#dahboard/views.py

from inertia import render #important!

def index(request):
    return render(request, "Blank", props={})
```

Now you can go to [localhost:8000/app/]() and we should find the Blank page with the entire layout.

### 3. Have a unified routing system (django).

We can use Django URLs as usual

```python
# urls.py
urlpatterns = [
    path("", views.index, name="index"),
    path("dashboard", views.dashboard, name="Dashboard"), # -> /app/dashboard
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
```

And in views.py the second argument of render should match the Vue page file without extension

```python
def dashboard(request):
    return render(request, "Dashboard", props={})
```

We dont need any routing system on our frontend side, everything is done by django. But what we do need is an config array to pass to our sidebar in order to have our navigation links. At this point we are using the routes array defined in our [static/src/js/router/sidebar.js]() file but we can delegate this content to django so everything is unified.

We are going to solve this on the next section too.

### 4. Inherit view permissions like authenticated user.

We need to pass the URLs to the layout in order to create the sidebar with these navigation links and the goal is to use hardcoded URLs as little as possible.

So that's when Inertia **Shared Data** comes in:

Adding a middleware we can pass data as a prop to every component. In this case we are passing de user object and an array of routes that should get to our sidebar and also using Vue provide/inject in order to avoid props drilling.

```python
 # dashboard/middleware.py
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
```

In this way we can build our routes array as we like, for instance, it may be a few endpoints that require authentification or a specific user role or permission
