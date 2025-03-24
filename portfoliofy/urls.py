from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("api/v1/blog/", include("blog.urls")),
    path("api/v1/", include("core.urls")),
    path('accounts/', include('allauth.urls')),
    path("", admin.site.urls),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
