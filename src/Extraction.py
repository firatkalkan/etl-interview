import pandas as pd
import json

class Extract:

    # load json file which includes data sources
    def __init__(self):
        jsonSource = json.load(open('../data_config.json'))
        self.csvFile = jsonSource['sources']['csv']

    # fetch the CSV data.
    def getCsvData(self, fileName):
        return pd.read_csv(self.csvFile[fileName])

