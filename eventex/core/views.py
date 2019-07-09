from django.shortcuts import render, get_object_or_404
from eventex.core.models import Speaker, Talk
from django.http import HttpResponse


def home(request):
    speakers = Speaker.objects.all()
    return render(request, 'index.html', context={'speakers': speakers})


def speaker_detail(request, slug):
    speaker = get_object_or_404(Speaker, slug=slug)
    return render(request, 'core/speaker_detail.html', {'speaker': speaker})


def talk_list(request):
    context = {
        'morning_talks': Talk.objects.filter(start__lt='12:00'),  # menor
        'afternoon_talks': Talk.objects.filter(start__gte='12:00'),  # maior ou igual
    }
    return render(request, 'core/talk_list.html', context)




















