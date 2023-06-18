
class ModelsBO:
    def classify_input(self, input):
        try:
            # Logica para classificar input tendo em conta o modelo
            return "classification_result"
        except Exception as e:
            raise e

    def create_model(self):
        try:
            # Logica para criar novo modelo
            return "created_model"
        except Exception as e:
            raise e

    def delete_model(self, model_uuid):
        try:
            # Logica para apagar um modelo em especifico

            if "model_does_not_exist":
                raise ModuleNotFoundError("Model not found")
            return
        except Exception as e:
            raise e  # Handle specific exceptions if needed

    def train_model(self, model_uuid):
        try:
            # Logic to train the specified model
            # Check if the model exists
            if "model_does_not_exist":
                raise ModuleNotFoundError("Model not found")

            # Perform model training
            return "trained_model"
        except Exception as e:
            raise e  # Handle specific exceptions if needed

    def update_model(self, model_uuid):
        try:
            # Logic to update the specified model
            # Check if the model exists
            if "model_does_not_exist":
                raise ModuleNotFoundError("Model not found")

            # Perform model update
            return "updated_model"
        except Exception as e:
            raise e  # Handle specific exceptions if needed

    def get_models(self):
        try:
            # Logic to retrieve all models
            return "models"
        except Exception as e:
            raise e  # Handle specific exceptions if needed

    def order_models(self):
        try:
            # Logic to order models based on certain criteria
            return "ordered_models"
        except Exception as e:
            raise e  # Handle specific exceptions if needed