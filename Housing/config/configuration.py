

class Configuration:
    def __init__(self) ->None:
        pass
    
    def get_data_ingestion_config(self)->DataIngestionConfig:
        pass

    def get_data_validation_config(self)->DataValidationConfig:
        pass

    def get_data_transformation_config(self)->DataTransformationConfig:
        pass

    def get_model_trainer_config(self)->ModelTrainerConfig:
        pass

    def get_model_evaluation_config(self)->ModelEvaluationConfig:
        pass

    def get_model_pusher_confg(self)->ModelPusherConfig:
        pass