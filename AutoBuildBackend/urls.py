from django.contrib import admin
from django.urls import path, include

from configurator import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('authentication.urls', namespace='authentication')),
    path('', include(urls))
]
