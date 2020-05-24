from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('igarden.urls')),
    path('admin/', admin.site.urls),
    path('lists/', include('lists.urls')),
    path('users/', include('users.urls')),
    path('reminders/', include('reminders.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
