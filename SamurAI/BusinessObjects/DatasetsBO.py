import os
import shutil
from fileinput import filename

from django.contrib.sites import requests
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema



class DatasetsBO:

    def retrieve_classifier(self):
        try:
            # Logic to retrieve the classifier
            return "classifier" # retornar o classificador
        except Exception as e:
            raise e

    def get_from_dataset(self):
        try:
            # Logic to get data from dataset
            return "dataset_data" # retornar os dados do classificador
        except Exception as e:
            raise e

    def import_dataset(self):
        response = requests.post('http://localhost:8000/import_dataset/',
                                 files={'file': open('path/to/dataset/file.csv', 'rb')})

        if response.status_code == 200:
            print('Dataset imported successfully')
        else:
            print('Failed to import dataset')

    def export_dataset(self, filename):
        print(filename)
        dataset_path = os.path.join('Datasets', filename)

        if not os.path.isfile(dataset_path):
            return None

        export_folder = 'ExportedDatasets'
        os.makedirs(export_folder, exist_ok=True)

        exported_dataset_path = os.path.join(export_folder, f'exported_{filename}')

        shutil.copy2(dataset_path, exported_dataset_path)

        return exported_dataset_path

    def add_input_dataset(self, input):
        try:
            # Logica para adicionar input ao dataset
            if not input:
                    raise ModuleNotFoundError("Invalid input")
            return
        except Exception as e:
            raise e

    def remove_from_dataset(self, entry):
        try:
            # Logica para remover entry do dataset
            if not entry:
                raise ModuleNotFoundError("Entry not found")
            return
        except Exception as e:
            raise e