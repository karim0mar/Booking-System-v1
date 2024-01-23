import json


def readData(fileName):
    file_path = f"Data/{fileName}.json"
    file = open(file_path)
    data = json.load(file)
    file.close()
    return data
