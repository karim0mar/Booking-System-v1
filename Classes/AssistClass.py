import json


def readData(fileName):
    file_path = f"Data/{fileName}.json"
    file = open(file_path)
    data = json.load(file)
    file.close()
    return data


def writeData(fileName, data):
    writeFile = open(f"Data/{fileName}.json", "w")
    release = json.dumps(data, indent=4, separators=(',', ': '))
    writeFile.write(release)
    writeFile.close()
