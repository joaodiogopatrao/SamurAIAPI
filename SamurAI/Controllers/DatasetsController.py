import os

from django.http import FileResponse, HttpResponse
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action, api_view, parser_classes, authentication_classes, permission_classes
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from drf_yasg import openapi
from rest_framework.views import APIView

from SamurAI.BusinessObjects.DatasetsBO import DatasetsBO
from SamurAI_API import settings

datasets_bo = DatasetsBO()


@api_view(['GET'])
def retrieve_classifier(self, request):
    classifier = datasets_bo.retrieve_classifier()
    return Response({'classifier': classifier})


@api_view(['GET'])
def get_from_dataset(self, request):
    dataset_data = datasets_bo.get_from_dataset()
    return Response({'data': dataset_data})


@api_view(['POST'])
def import_dataset(request):
    uploaded_file = request.FILES.get('file')

    if not uploaded_file:
        return Response({'error': 'No file uploaded'})

    dataset_dir = os.path.join(settings.BASE_DIR, 'Datasets')
    os.makedirs(dataset_dir, exist_ok=True)

    dataset_path = os.path.join(dataset_dir, uploaded_file.name)

    with open(dataset_path, 'wb') as destination:
        for chunk in uploaded_file.chunks():
            destination.write(chunk)

    return Response({'message': 'Dataset imported successfully'})


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def export_dataset(request):
    filename = request.data.get('filename')

    if not filename:
        return Response({'error': 'No filename provided'})

    dataset_path = os.path.join('Datasets', filename)

    if not os.path.isfile(dataset_path):
        return Response({'error': 'Dataset not found'})

    with open(dataset_path, 'rb') as dataset_file:
        dataset_content = dataset_file.read()

    response = HttpResponse(dataset_content, content_type='application/octet-stream')
    response['Content-Disposition'] = f'attachment; filename="{filename}"'
    return response


@api_view(['POST'])
def add_input_dataset(self, request):
    input_data = request.data.get('input')
    datasets_bo.add_input_dataset(input_data)
    return Response({'message': 'Input added to the dataset'})
