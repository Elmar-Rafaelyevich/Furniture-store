from django.urls import path
from shop.views import index, about

app_name = 'shop'


urlpatterns = [
    path("", index, name='index'),
    path("about/", about, name='about'),
]
