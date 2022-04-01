from Extraction import Extract
from Load import MongoDB
import pandas as pd
from pymongo import MongoClient


class Transformation:

    def __init__(self, file):

        # extract object ready to fetch CSV data
        extractObj = Extract()
        data = extractObj.getCsvData(file)
        self.csvItemTransformation(data)

    # Item transformation
    def csvItemTransformation(self, data):

        data['value'] = list(map(lambda x: (int(x) * 10 if x.isnumeric() else x), data['value']))
        transformedData = data.to_dict('records')
        print("Item transformation has been completed")

        dbConn = MongoDB()
        dbConn.insert_into_db(transformedData)

