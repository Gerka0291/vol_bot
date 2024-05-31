import json
from settings import*




def readJson(name):
    r = open(name , 'r') 
    try:
        file_content = r.read()
        result = json.loads(file_content)
    finally: r.close()
    return result


def writeJson(name, jsonW):
    w = open(name, 'w')
    try:
        json.dump(jsonW, w,indent=2 )   # sort_keys=True,
    finally: w.close()
    


if __name__ == '__main__':
    settingsList = readJson(settingsName)

    pass