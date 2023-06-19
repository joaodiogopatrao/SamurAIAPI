from django.core.serializers import json
from django.http import JsonResponse
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from SamurAI.BusinessObjects.ModelsBO import ModelsBO

model_bo = ModelsBO()


@swagger_auto_schema(
    operation_description='Classify input',
    responses={200: openapi.Response('Classification result', schema=openapi.Schema(type='string'))}
)
def classify_input(request):
    data = json.loads(request.body)
    input_data = data.get('input')
    classification_result = model_bo.classify_input(input_data)
    return JsonResponse({'classification': classification_result})


@swagger_auto_schema(
    operation_description='Create a new model',
    responses={200: openapi.Response('Success')}
)
def create_model(request):
    created_model = model_bo.create_model()
    return JsonResponse({'model': created_model})


@swagger_auto_schema(
    operation_description='Delete a model',
    request_body=openapi.Schema(
        type='object',
        properties={
            'modelUuid': openapi.Schema(type='string')
        }
    ),
    responses={200: openapi.Response('Success')}
)
def delete_model(request):
    data = json.loads(request.body)
    model_uuid = data.get('modelUuid')
    model_bo.delete_model(model_uuid)
    return JsonResponse({'message': 'Model deleted successfully'})


@swagger_auto_schema(
    operation_description='Train a model',
    request_body=openapi.Schema(
        type='object',
        properties={
            'modelUuid': openapi.Schema(type='string')
        }
    ),
    responses={200: openapi.Response('Success')}
)
def train_model(request):
    data = json.loads(request.body)
    model_uuid = data.get('modelUuid')
    trained_model = model_bo.train_model(model_uuid)
    return JsonResponse({'model': trained_model})


@swagger_auto_schema(
    operation_description='Update a model',
    responses={200: openapi.Response('Success')}
)
def update_model(request):
    updated_model = model_bo.update_model()
    return JsonResponse({'model': updated_model})


@swagger_auto_schema(
    operation_description='Get all models',
    responses={200: openapi.Response('List of models', schema=openapi.Schema(type='string'))}
)
def get_models(request):
    models = model_bo.get_models()
    return JsonResponse({'models': models})


@swagger_auto_schema(
    operation_description='Order models',
    responses={200: openapi.Response('Ordered models', schema=openapi.Schema(type='string'))}
)
def order_models(request):
    ordered_models = model_bo.order_models()
    return JsonResponse({'models': ordered_models})
