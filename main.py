#!/usr/bin/python3
import random,os,sys,re
from saveDefault import *

saveDefaultFile( homeFolder() , "README.md"    )
saveDefaultFile( homeFolder() , "CHANGELOG.md" )
package_json = getSample("sample_package.json")       ## 讀取範本檔案，最後位置 %HOME%/.vscode/extensions/ryanCode/package.json
extension_js = getSample("sample_extension.js")       ## 讀取範本檔案，最後位置 %HOME%/.vscode/extensions/ryanCode/out/extension.js
dataArr      = getAll_mainCode().split(",,,,,,,,,,")  ## 讀取 所有 mainCode_*.py 檔案至 dataArr[]

codeID = ""
for i in range(len(dataArr)-1):
    if i%2 == 0:
        codeID = getCodeID(i)
        text   = dataArr[i].replace("\n","")
        data1 = '"onCommand:extension.sayHello"'
        data2 = f'"onCommand:extension.{codeID}",'+"\n"+"		"+data1
        package_json = package_json.replace(data1,data2)

        data1 = '{"command": "extension.sayHello","title": "Hello World"}'
        data2 = '{"command": "extension.'+codeID+'","title": "'+text+'"},'+"\n"+"			"+data1
        package_json = package_json.replace(data1,data2)

    if i%2 != 0:
        text   = dataArr[i]
        fileName = f"{homeFolder()}/out/{codeID}.txt"
        data1 = '///REPLACE HERE///'
        data2 = """
        context.subscriptions.push(vscode.commands.registerCommand('extension."""+codeID+"""', () => {
        const codeStr = fs.readFileSync('"""+fileName+"""', 'utf8')
        pasteData(codeStr)
        }));""" + data1
        extension_js = extension_js.replace(data1,data2)
        saveDataArr(f"{homeFolder()}/out/{codeID}.txt",text)


saveDefaultFile2( homeFolder()       , "package.json", package_json )
saveDefaultFile2( homeFolder()+"/out", "extension.js", extension_js )
