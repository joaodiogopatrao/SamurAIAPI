from django.urls import path, include
from djongo import admin
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="SamurAI API",
        default_version='v1',
        description="SamurAI API",
        terms_of_service="https://your-terms-of-service-url.com/",
        contact=openapi.Contact(email="bee@bee-eng.pt"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('', include('SamurAI.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]