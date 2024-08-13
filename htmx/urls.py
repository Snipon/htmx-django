from django.contrib import admin
from django.urls import include, path
from htmx.views import index, page
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('page', page),
    path("__reload__/", include("django_browser_reload.urls")),
]
