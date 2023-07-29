import os
from datetime import datetime
import sys
from sensor.logger import logging
from sensor.exception import SensorException

'''
This is the config entity
'''

FILE_NAME = "sensor.csv"
TRAIN_FILE_NAME = "train.csv"
TEST_FILE_NAME = "test.csv"

class TrainingPipelineConfig:
    def __init__(self):
        self.artifact_dir = os.path.join(os.getcwd(),"artifacts",f"{datetime.now().strftime('%d%m%Y_%H%M%S')}")
class DataIngestionConfig:
    def __init__(self,training_pipeline_config:TrainingPipelineConfig):
        self.database_name = "aps"
        self.collection_name = "sensor"
        self.data_ingestion_dir = os.path.join(training_pipeline_config,"data_ingestion")
        self.feature_store_dir = os.path.join(self.data_ingestion_dir,"feature_store_dir")
        self.train_file_path = os.path.join(self.data_ingestion_dir,"dataset",TRAIN_FILE_NAME)
        self.test_file_path = os.path.join(self.data_ingestion_dir,"dataset",TEST_FILE_NAME)
    
    def to_dict(self)->dict:
        try:
            return self.__dict__
        except Exception as e:
            raise SensorException(e,sys)
    
class DataValidationConfig:...
class DataTransformationConfig:...
class ModelTrainerConfig:...
class ModelEvaluationConfig:...
class ModelPusherConfig:...