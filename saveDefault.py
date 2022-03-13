#!/usr/bin/python3
import os,sys,random,re


def saveDataArr(path,data):
    fp = open(path,'w')
    fp.write(data)
    fp.close


def getSample(sample_file_name):
    data = ""
    with open(sample_file_name) as file:
        data = file.read()
    return data


def getCodeID(num):
    codeID = ""
    # for i in range(1,20):
    #     codeID = codeID + chr(random.randint(65,89))
    codeID = "DATAFILE_" + str(num+10000)
    return codeID


def homeFolder():
    if os.name == 'posix':
        home_folder = f"{os.environ['HOME']}/.vscode/extensions/ryanCode"
        os.system(f"mkdir -p {home_folder}/out")

    if os.name == 'nt':
        home_folder = f"{os.environ['USERPROFILE']}\\.vscode\\extensions\\ryanCode"
        os.system(f"mkdir {home_folder}\\out")

    return home_folder


def saveDefaultFile(home_folder,filename):
    data = ""
    with open(filename) as file:
        data = file.read()
    fp = open( f"{home_folder}/{filename}" ,'w')
    fp.write(data)
    fp.close

def saveDefaultFile2(path,filename,data):
    fp = open( f"{path}/{filename}" ,'w')
    fp.write(data)
    fp.close


# 讀取 所有 mainCode_*.py 檔案至 allData 裡面 , 並回傳
def getAll_mainCode():
    allData = ""
    for mainCodefile in os.listdir( "./" ):
        if re.match("mainCode_",mainCodefile):
            with os.popen("./"+ mainCodefile) as myCommand:
                allData = allData + myCommand.read()
    return allData
