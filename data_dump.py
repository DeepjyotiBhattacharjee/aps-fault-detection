import pymongo
import json
import pandas as pd

client = pymongo.MongoClient("mongodb+srv://deepjyotib:Snape%401993@cluster0.3ykmmry.mongodb.net/?retryWrites=true&w=majority")

DATA_FILE_PATH = "C:/Users/bhattade/Documents/aps-fault-detection/aps_failure_training_set1.csv"
DATABASE_NAME = "aps"
COLLECTION_NAME = "sensor"

if __name__ == "__main__":
    df = pd.read_csv(DATA_FILE_PATH)
    print("Rows and columns present in the df is : ",df.shape)

    # Convert the dataframe to json to insert it into mongo db
    df.reset_index(drop=True,inplace=True)
    json_records = list(json.loads(df.T.to_json()).values())

    # Inserting the converted json records in MongoDB
    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_records)