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
        try:
            # Logica para importar dataset
            return
        except Exception as e:
            raise e

    def export_dataset(self):
        try:
            # Logica para export dataset
            return
        except Exception as e:
            raise e

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