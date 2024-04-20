import os
import json
BASE_DIRECTORY = 'data/'
def CreateFile(fileName : str):
    with open(BASE_DIRECTORY+fileName,'w') as fw:
        json.dump({},fw,indent=4)

def UpdateFile(*param):
    with open(BASE_DIRECTORY+param[0],'w') as fw:
        json.dump(param[1],fw,indent=4)

def ReadFile(*params):
    data = list(params)
    with open(BASE_DIRECTORY+data[0],'r') as fr:
        return json.load(fr)

def AddData(*param):
    with open(BASE_DIRECTORY+param[0], "r+") as rwf:
        data_file=json.load(rwf)
        if (len(param) > 1):
            data_file.update(param[1])
        rwf.seek(0)
        json.dump(data_file,rwf, indent=4)

def checkFile(archivo : str)-> bool: 
    if(not(os.path.isfile(BASE_DIRECTORY+archivo))):
        return False
    else: 
        return True
