from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from djangochat import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('chat.urls'))
]