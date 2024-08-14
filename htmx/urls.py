from django.urls import include, path
from htmx.views import index, page, page_list
from rest_framework import routers, serializers, viewsets
import django_eventstream
from django.contrib import admin

router = routers.DefaultRouter()
urlpatterns = [
    path('', index),
    path('page', page),
    path('list', page_list),
    path('content/<slug>', page),
    path("__reload__", include("django_browser_reload.urls")),
    path("events", include(django_eventstream.urls), {"channels": ["test"]}),
    path('admin', admin.site.urls),
]
