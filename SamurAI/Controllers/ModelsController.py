from djongo.models import json


def classify_input(request):
    return ''


def create_model(request):
    return ''


def delete_model(request):
    data = json.loads(request.body)
    modelUuid = data.get('modelUuid')

    return ''


def train_model(request):
    data = json.loads(request.body)
    modelUuid = data.get('modelUuid')

    return ''


def update_model(request):
    return ''


def get_models(request):
    return ''


def order_models(request):
    return ''
