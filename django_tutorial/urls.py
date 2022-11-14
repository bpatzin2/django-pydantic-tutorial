"""django_tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from typing import List
from django.contrib import admin
from django.http import HttpRequest
from django.urls import include, path
from ninja import NinjaAPI, Schema

api = NinjaAPI()

class HiMomResponse(Schema):
    an_int: int

@api.get("/himom", response=HiMomResponse)
def himom(request: HttpRequest, a: int) -> HiMomResponse:
    return HiMomResponse(an_int=a)

weapons = ["Ninjato", "Shuriken", "Katana", "Kama", "Kunai", "Naginata", "Yari"]

@api.get("/weapons", response=List[str])
def list_weapons(request: HttpRequest, limit: int = 10, offset: int = 0) -> List[str]:
    return weapons[offset: offset + limit]

urlpatterns = [ # type: ignore
    path('polls/', include('polls.urls')),
    path("admin/", admin.site.urls),
    path("api/", api.urls),  # type: ignore
]   
