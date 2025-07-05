from django.shortcuts import render, HttpResponse
from goods.models import Categories

def index(request):
    context = {
        'title': 'Home - Главная',
        'content' : 'Магазин мебели HOME',
        
        'categories':Categories.objects.all()


    }
    return render(request, 'shop/index.html', context)


def about(request):
    context = {
        'title': 'Home - О нас',
        'content': 'О нас',
        'text_on_page': 'Самый классный интернет магазин'
    }
    return render(request, 'shop/about.html', context)
