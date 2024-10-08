from time import strftime

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django_htmx.middleware import HtmxDetails
from django.views.decorators.http import require_GET
from htmx.cache import fake_content, fake_content_list


class HtmxHttpRequest(HttpRequest):
    htmx: HtmxDetails

def make_content(htmx: HtmxDetails, key: str):
    content = fake_content(key)
    content['base_template'] = htmx and 'htmx.html' or 'base.html'
    content['time'] = strftime('%H:%M:%S')
    return content

@require_GET
def index(request: HtmxHttpRequest):
    return render(
        request,
        'content.html',
        make_content(request.htmx, 'index')
    )

@require_GET
def page (request: HtmxHttpRequest, **kwargs):
    return render(
        request,
        'content.html',
        make_content(request.htmx, request.path)
    )

@require_GET
def page_list(request: HtmxHttpRequest):
    return render(
        request,
        'content_list.html',
        {
            'title': 'List of Pages',
            'content': fake_content_list(),
            'base_template': request.htmx and 'htmx.html' or 'base.html',
            'time': strftime('%H:%M:%S')
        }
    )
