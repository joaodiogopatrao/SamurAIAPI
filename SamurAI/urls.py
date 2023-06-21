"""SamurAI_API URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi, views
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from SamurAI.Controllers.DatasetsController import DatasetsController

from SamurAI.Controllers.ModelsController import (
    classify_input, create_model, delete_model, train_model, update_model,
    get_models, order_models
)
datasetscontroller = DatasetsController()

urlpatterns = [
    path('retrieve_classifier/', datasetscontroller.retrieve_classifier, name='retrieve_classifier'),
    path('get_from_dataset/', datasetscontroller.get_from_dataset, name='get_from_dataset'),
    path('import_dataset/', datasetscontroller.import_dataset, name='import_dataset'),
    path('export_dataset/', datasetscontroller.export_dataset, name='export_dataset'),
    path('add_input_dataset/', datasetscontroller.add_input_dataset, name='add_input_dataset'),

    # URLs for the model views
    path('classify_input/', classify_input, name='classify_input'),
    path('create_model/', create_model, name='create_model'),
    path('delete_model/', delete_model, name='delete_model'),
    path('train_model/', train_model, name='train_model'),
    path('update_model/', update_model, name='update_model'),
    path('get_models/', get_models, name='get_models'),
    path('order_models/', order_models, name='order_models'),
]