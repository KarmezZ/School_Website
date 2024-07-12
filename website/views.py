from django.shortcuts import render, get_object_or_404
from .models import Nauczyciel


# Create your views here.
def rekrutacja_page(request):
    return render(request, 'website/rekrutacja.html')


def news_page(request):
    return render(request, 'website/news.html')


def info_for_parent_page(request):
    teachers = Nauczyciel.objects.all()
    return render(request, 'website/info-parents.html', {'teachers': teachers})


def sekretariat_page(request):
    return render(request, 'website/sekretariat.html')


def photos_page(request):
    return render(request, 'website/zdjęcia.html')
