import os
from bs4 import BeautifulSoup
import json
import shutil
import csv

ignoreList = ['rptBase.htm']
#tarDir = r'C:\Users\cjackng\Desktop\Work\LCSD-PCS-2017Revamp\trunk\Prototype\Latest'
tarDir = r'C:\Users\cjackng\Desktop\Work\LCSD-PCS-2017Revamp\trunk\Prototype\html'
fieldNames = ['fileName', 'screenName','funcName']
resultList = []

def getpParam(soup,id,paramKey):
    tarDivs = soup.find_all("div", { "id" :id })        
    if len(tarDivs) > 1:
        print("===what==="+id)
    elif len(tarDivs) < 1:
        print("===No "+id+"===")
        return None
    tarDiv = tarDivs[0]
    if tarDiv.has_attr('p-param'):
        params = json.loads(tarDiv['p-param'].replace("'","\""))
        return params[paramKey]


for filename in os.listdir(tarDir):
    if(filename.endswith('.htm') and filename not in ignoreList):
        print(filename)
        soup = BeautifulSoup(open(os.path.join(tarDir,filename),encoding='utf-8'),"html.parser")
        scrName = getpParam(soup,'footer','lblScreenName')
        funcName = getpParam(soup,'header','lblCurPos')
        if scrName is not None and funcName is not None:            
            tmpDict = {'fileName':filename,'screenName':scrName,'funcName':funcName}
            resultList.append(tmpDict)

resultList = sorted(resultList, key = lambda k: k['screenName'])
with open('pcs_screen_ids_html2.csv', 'w',newline='') as csvfile:    
    w = csv.DictWriter(csvfile, fieldnames=fieldNames)
    w.writeheader()
    for r in resultList:
        w.writerow(r)
