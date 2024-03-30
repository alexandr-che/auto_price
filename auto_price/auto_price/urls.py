from django.contrib import admin
from django.urls import include, path
from auto_price import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('index.urls', namespace='index')),
    # path('catalog/', include('cars.urls', namespace='cars')),
    path('user/', include('users.urls', namespace='users')),
    path('advert/', include('adverts.urls', namespace='adverts')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
