from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context = {
        'title': 'Home',
        'context': 'Главная страница магазина',
        'list': ['item1', 'item2', 'item3'],
        'dict':{'key1': 'value1'},
        'bool': False,
    }
    return render(request, 'shop/index.html', context)


def about(request):
    return HttpResponse('about page')
