from django.core.serializers import json
from django.http import JsonResponse
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view

from SamurAI.BusinessObjects.ModelsBO import ModelsBO

model_bo = ModelsBO()


@api_view(['POST'])
def classify_input(request):
    data = json.loads(request.body)
    input_data = data.get('input')
    classification_result = model_bo.classify_input(input_data)
    return JsonResponse({'classification': classification_result})


@api_view(['POST'])
def create_model(request):
    created_model = model_bo.create_model()
    return JsonResponse({'model': created_model})


@api_view(['POST'])
def delete_model(request):
    data = json.loads(request.body)
    model_uuid = data.get('modelUuid')
    model_bo.delete_model(model_uuid)
    return JsonResponse({'message': 'Model deleted successfully'})


@api_view(['POST'])
def train_model(request):
    data = json.loads(request.body)
    model_uuid = data.get('modelUuid')
    trained_model = model_bo.train_model(model_uuid)
    return JsonResponse({'model': trained_model})


@api_view(['POST'])
def update_model(request):
    updated_model = model_bo.update_model()
    return JsonResponse({'model': updated_model})


@api_view(['GET'])
def get_models(request):
    models = model_bo.get_models()
    return JsonResponse({'models': models})


@api_view(['POST'])
def order_models(request):
    ordered_models = model_bo.order_models()
    return JsonResponse({'models': ordered_models})
