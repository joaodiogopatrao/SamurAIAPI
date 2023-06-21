
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

from SamurAI.Controllers.DatasetsController import (import_dataset,export_dataset,retrieve_classifier,get_from_dataset,add_input_dataset)

from SamurAI.Controllers.ModelsController import (
    classify_input, create_model, delete_model, train_model, update_model,
    get_models, order_models
)


schema_view = get_schema_view(
   openapi.Info(
      title="SamurAI API",
      default_version='v1',
      description="API for SamurAI project",
      terms_of_service="https://your-terms-of-service-url.com/",
      contact=openapi.Contact(email="your-contact-email@example.com"),
      license=openapi.License(name="MIT License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('retrieve_classifier/', retrieve_classifier, name='retrieve_classifier'),
    path('get_from_dataset/', get_from_dataset, name='get_from_dataset'),
    path('import_dataset/', import_dataset, name='import_dataset'),
    path('export_dataset/', export_dataset, name='export_dataset'),
    path('add_input_dataset/', add_input_dataset, name='add_input_dataset'),

    # URLs for the model views
    path('classify_input/', classify_input, name='classify_input'),
    path('create_model/', create_model, name='create_model'),
    path('delete_model/', delete_model, name='delete_model'),
    path('train_model/', train_model, name='train_model'),
    path('update_model/', update_model, name='update_model'),
    path('get_models/', get_models, name='get_models'),
    path('order_models/', order_models, name='order_models'),
]