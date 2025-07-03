from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context = {
        'title': 'Home - Главная',
        'content' : 'Магазин мебели HOME'
    }
    return render(request, 'shop/index.html', context)


def about(request):
    context = {
        'title': 'Home - О нас',
        'content': 'О нас',
        'text_on_page': 'Самый классный интернет магазин'
    }
    return render(request, 'shop/about.html', context)
