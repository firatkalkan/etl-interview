from src.classes.Transformation import Transformation
import json

if __name__ == '__main__':

    rawJsonData = json.load(open('data_config.json'))

    for source, files in rawJsonData['sources'].items():

        for file in files:
            print(file + " has been selected for " + source)
            trans_obj = Transformation(file)
