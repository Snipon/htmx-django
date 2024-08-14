from django.urls import include, path
from htmx.views import index, page
urlpatterns = [
    path('', index),
    path('page', page),
    path("__reload__/", include("django_browser_reload.urls")),
]
