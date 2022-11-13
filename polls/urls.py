from django.urls import path
from django.http import HttpRequest
from . import views
from ninja import NinjaAPI

api = NinjaAPI(urls_namespace='pollsapi')


@api.get("/himom")
def add(request: HttpRequest, a: int):
    return {"result": a}

urlpatterns = [  # type: ignore
    path('', views.index, name='index'),
    path("api/", api.urls),  # type: ignore
]