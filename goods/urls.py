from django.urls import path
from goods.views import product, catalog

app_name = 'goods'


urlpatterns = [
    path("", catalog, name='index'),
    path("product/", product, name='product'),
]
