from pymongo import MongoClient
import pandas as pd
import json

class MongoDB:

    def __init__(self):
        self.set_database_connection()


    # insert data in MongoDB
    def insert_into_db(self, data):
            try:
                self.collection.insert_many(data)
                print('Data Inserted Successfully')
            except Exception as e:
                print('There is some ERROR for inserting data')
                print(e)

    # fetch data from MongoDB
    def read_from_db(self, collection):
        try:
            data = pd.DataFrame(list(self.db[collection].find()))
            print('Data Fetched Successfully')
            return data
        except Exception as e:
            print('There is some ERROR for reading data')
            print(e)

    # set database connection
    def set_database_connection(self):

        # loading json file which includes mongodb credentials
        rawJsonData = json.load(open('../data_config.json'))
        credentials = rawJsonData['credentials']['mongo']

        host = credentials['host']
        user = credentials['user']
        password = credentials['password']
        dbname = credentials['dbname']
        params = credentials['params']

        target = "mongodb://" + user + ":" + password + "@" + host + "/" + dbname + '?' + params

        try:
            self.client = MongoClient(target)
            self.db = self.client[dbname]
            self.collection = self.db['test']
            print('MongoDB Connection Successful.')
        except Exception as e:
            print('MongoDB Connection Error')
            print(e)

















