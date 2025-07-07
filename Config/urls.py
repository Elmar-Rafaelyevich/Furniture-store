from django.contrib import admin
from django.urls import path, include

from Config.settings import DEBUG
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # shop приложение
    path('', include('shop.urls', namespace='shop')),
    # goods приложение
    path('catalog/',include('goods.urls', namespace='catalog'))

]

if DEBUG:
    urlpatterns += [
        path('__debug__/', include('debug_toolbar.urls'))
        
    ]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)