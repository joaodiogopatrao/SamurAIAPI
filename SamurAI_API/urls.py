from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi, views
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="SamurAI",
        default_version='v1',
        description="SamurAI",
        terms_of_service="https://your-terms-of-service-url.com/",
        contact=openapi.Contact(email="bee@bee-eng.pt"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('', include('SamurAI.urls')),
]