from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # shop приложение
    path('', include('shop.urls', namespace='shop')),
    # goods приложение
    path('catalog/',include('goods.urls', namespace='catalog'))

]
