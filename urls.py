from django.urls import path
from django.http import HttpRequest, HttpResponse


def home(request: HttpRequest) -> HttpResponse:
    return HttpResponse("OK")


urlpatterns = [
    path("", home),
]
