
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from portfolio import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # portfolioのurls.pyを読み込み
    path('', include('portfolio.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)