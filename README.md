# Django + Vue Multi Page Application (MPA)

> A common myth is that an SPA is necessary to use a front-end framework like Vue or React.

When developers talk about using Vue with Django, they often talk about building a Vue SPA and a Django API, hosted on separate servers. This is also known as decoupled front and back ends.

Inspired by this article [
You don't have to build a separate app to use Vue with Django](https://ctrlzblog.com/add-vue-to-your-django-templates-with-vite/) i decided to test if you can get the full benefits of a JavaScript development environment without creating a separate codebase for your frontend.

## Necessary Features

The goal is to have the same benefits as if we were using _Django Template Engine_ but with a modern frontend framework like vue.

It has to have this features:

-   1. Being able to use a base layout (Header, Footer, Sidebar...)
-   2. Individual views within the layout, with parameters or props.
-   3. Have a unified routing system (django).
-   4. Inherit view permissions like authenticated user.

## The journey (This is a work in progress)

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

At this point i realized the first big problem: With this approche i would have to do a Vue _CreateApp_ for each django view and i cannot use a single layout where a part of that layout changes for every view .... not acceptable

### The Solution: [inertiajs](https://inertiajs.com/)

This is the last piece of the puzzle, the one that makes everything fits together.

> Inertia allows you to create fully client-side rendered, single-page apps, without the complexity that comes with modern SPAs. It does this by leveraging existing server-side patterns that you already love.

And from the [community adapters page](https://inertiajs.com/community-adapters) we can find [inertia-django](https://pypi.org/project/inertia-django/).

-   Just install with pip, add _inertia_ to INSTALLED_APPS and add some settings:

```python
INERTIA_LAYOUT = 'base.html'
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

-   Now we need to replace **RouterLink** (vue-router) to **Link** (inertia) on a few components (Sidebar, Login, CreateAccount)
-   Then we need to import Layout component on every .vue file inside [static/src/js/pages]() folder and wrap the content inside Layout, for instance:

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

-   Now we can start our frontend server

```js
npm install @inertiajs/vue3
```

-   Finally we can add a view in django that points to any of our vue pages file'

```python
#core/urls.py

from django.urls import path
from dashboard.views import index

urlpatterns = [
    path('<page>', index, name="index")
]
```

```python
#dashboard/urls.py

from django.urls import path
from dashboard.views import index

urlpatterns = [
    path('<page>', index, name="index")
]
```

We need to use **render** from inertia instead of django!

```python
#dahboard/views.py

from inertia import render #important!

def index(request, page):
    return render(request, page, props={})
```

-   Now you can go to any vue page like [localhost:8000/app/Blank]() and everything should look fine.

**NOTICE:** the name of the page param should match to the name of the file .vue. We are going ti chabge that later.

### 2. Individual views within the layout, with parameters or props.

### 3. Have a unified routing system (django).

### 4. Inherit view permissions like authenticated user.
