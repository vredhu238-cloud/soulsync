from django.contrib import admin
from django.urls import path, include
from accounts import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('accounts/', include('accounts.urls')),
    path('discover/', include('matching.urls')), # <--- Ye nayi line add karein
]


# Image uploads ko development mein dikhane ke liye
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)