from django.urls import path
from dashboard.views import index

urlpatterns = [
    path('<page>', index, name="index")
]