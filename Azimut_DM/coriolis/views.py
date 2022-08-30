from django.shortcuts import render
from django.http import HttpResponse

from .models import *


def index(request):
    advantage = Advantage.objects.all()
    advantage_type = AdvantageType.objects.all()
    regulation = Regulation.objects.all()
    description = Description.objects.all()
    banner = Banner.objects.all()

    return render(
        request,
        'coriolis/index.html',
        {'advantage': advantage,
         'advantage_type': advantage_type,
         'regulation': regulation,
         'description': description,
         'banner': banner,
         })
