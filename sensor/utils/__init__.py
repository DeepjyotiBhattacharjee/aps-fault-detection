import pandas as pd
from sensor.config import mongo_client
from sensor.logger import logging
from sensor.exception import SensorException
import sys

def get_collection_as_dataframe(database_name:str, collection_name:str) -> pd.DataFrame:
    '''
    This function returns a mongo db collection as pandas dataframe
    database name = database_name
    collection name = collection_name
    
    ===============================================================

    parameters : database_name:str, collection_name:str
    ===============================================================
    
    returns : pandas Dataframe

    '''
    try:
        logging.info(f"Reading data from database : {database_name} and collection : {collection_name}")
        df = pd.DataFrame(list(mongo_client[database_name][collection_name].find()))
        logging.info(f"Found columns : {df.columns}")

        if "_id" in df.columns:
            logging.info("Dropping column : '_id'")
            df.drop("_id",axis=1,inplace=True)
        logging.info(f"Rows and columns in dataframe : Rows & Columns : {df.shape}")
        return df
    except Exception as e:
        raise(e,sys)