from djongo.models import json


def retrieve_classifier(request):
    return ''

def get_from_dataset(request):
    return ''

def import_dataset(request):
    return ''

def export_dataset(request):
    return ''

def add_input_dataset(request):
    data = json.loads(request.body)
    input = data.get('input')
    return ''

def remove_from_dataset(request):
    data = json.loads(request.body)
    entry = data.get('entry')
    return ''