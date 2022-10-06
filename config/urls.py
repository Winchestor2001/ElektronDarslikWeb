from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import handler404, handler500
from e_darslik.views import error_404_view

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('e_darslik.urls')),
                  path('ckeditor/', include('ckeditor_uploader.urls')),
                path('error/', error_404_view, name='error_404'),
              ]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = "e_darslik.views.error_404_view"
