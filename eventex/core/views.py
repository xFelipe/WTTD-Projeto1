from django.shortcuts import render


# Create your views here.
def home(request):
    speakers = [
                {'name': 'Grace Hopper', 'photo': 'http://hbn.link/hopper-pic'},
                {'name': 'Alan Turing', 'photo': 'http://hbn.link/turing-pic'},
            ]
    return render(request, 'index.html', context={'speakers': speakers})


def speaker_detail(request, slug):
    return render(request, 'core/speaker_detail.html')