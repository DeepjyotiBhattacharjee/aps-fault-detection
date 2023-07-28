import pymongo
import json
import pandas as pd
from dataclasses import dataclass
import os

@dataclass
class EnvironmentVariable:
    mongo_db_url :str = os.getenv("MONGO_DB_URL")

env_var = EnvironmentVariable()

mongo_client = pymongo.MongoClient(env_var.mongo_db_url)
DATA_FILE_PATH = "C:/Users/bhattade/Documents/aps-fault-detection/aps_failure_training_set1.csv"
DATABASE_NAME = "aps"
COLLECTION_NAME = "sensor"

def get_collection_as_dataframe() -> pd.DataFrame:
    pass