from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import  include, url

admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),
    path('api/', include('base.api.urls')),
    url(r'^admin/', include(admin.site.urls)),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
