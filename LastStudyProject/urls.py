from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

schema_view = get_schema_view(
    openapi.Info(
        title="Last study project",
        default_version='808',
        description="Swagger for my latest learning project in a junior Python course",
        terms_of_service="https://ru.pinterest.com/pin/921408405016495987/",
        contact=openapi.Contact(email="https://t.me/snowa8snowa"),
        license=openapi.License(name="snowa?"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('appone.urls')),
    path('auth/', include('rest_framework.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0),name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',cache_timeout=0), name='schema-redoc'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
