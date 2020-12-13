import datetime

from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render


def countdown(request: HttpRequest) -> HttpResponse:
    return render(
        request, 
        'countdown.html',
        context={
            'next_holidays': datetime.datetime(datetime.datetime.today().year + 1, 1, 1, 0, 0, 0)
         }
    )