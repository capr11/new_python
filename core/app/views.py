from django.shortcuts import render
from .models import Music


def index_views(request):
    musics = Music.objects.all()

    return render(request, 'app/index.html', {"musics": musics})



def music_detail_view(request, pk):
    music = Music.objects.get(id=pk)
    return render(request, 'app/detail.html', {"music": music})
def __getattr__(name):
    return
print("hello guys")