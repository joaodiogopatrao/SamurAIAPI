from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from drf_yasg import openapi
from rest_framework.views import APIView

from SamurAI.BusinessObjects.DatasetsBO import DatasetsBO

datasets_bo = DatasetsBO()


class DatasetsController(APIView):
    @swagger_auto_schema(
        decorators=[api_view(['POST'])],
        operation_description='Retrieve the classifier',
        responses={200: openapi.Response('Classifier', schema=openapi.Schema(type='string'))}
    )
    def retrieve_classifier(self, request):
        classifier = datasets_bo.retrieve_classifier()
        return Response({'classifier': classifier})

    @swagger_auto_schema(
        decorators=[api_view(['POST'])],
        operation_description='Get data from the dataset',
        responses={200: openapi.Response('Dataset data', schema=openapi.Schema(type='string'))}
    )
    def get_from_dataset(self, request):
        dataset_data = datasets_bo.get_from_dataset()
        return Response({'data': dataset_data})

    @swagger_auto_schema(
        decorators=[api_view(['POST'])],
        operation_description='Import dataset',
        responses={200: openapi.Response('Success')}
    )
    def import_dataset(self, request):
        datasets_bo.import_dataset()
        return Response({'message': 'Dataset imported successfully'})

    @swagger_auto_schema(
        decorators=[api_view(['POST'])],
        operation_description='Export dataset',
        responses={200: openapi.Response('Success')}
    )
    def export_dataset(self, request):
        datasets_bo.export_dataset()
        return Response({'message': 'Dataset exported successfully'})

    @swagger_auto_schema(
        decorators=[api_view(['POST'])],
        operation_description='Add input to the dataset',
        request_body=openapi.Schema(
            type='object',
            properties={
                'input': openapi.Schema(type='string')
            }
        ),
        responses={200: openapi.Response('Success')}
    )
    def add_input_dataset(self, request):
        input_data = request.data.get('input')
        datasets_bo.add_input_dataset(input_data)
        return Response({'message': 'Input added to the dataset'})