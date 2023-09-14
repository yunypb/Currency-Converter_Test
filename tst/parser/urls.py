from django.contrib import admin
from django.urls import path, include

from parser.views import money

urlpatterns = [
    path('rates/from=<slug:c_from>/to=<slug:c_to>/value=<int:value>', money),
]
