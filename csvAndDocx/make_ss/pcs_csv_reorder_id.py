import os
from bs4 import BeautifulSoup
import json
import shutil
import csv
import fileinput
import re

p = re.compile("'lblScreenName':'.+?'")

ignoreList = ['rptBase.htm']
tarDir = r'C:\Users\cjackng\Desktop\Work\LCSD-PCS-2017Revamp\trunk\Prototype\Latest'
fieldNames = ['fileName', 'screenName']
reorderDict = {}

with open('pcs_screen_ids.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')    
    for row in spamreader:
        if row[0] == 'fileName':
            continue
        fileName = row[0]
        screenID = row[1]
        reorderDict[fileName] = screenID

os.chdir(tarDir)
for filename in os.listdir(tarDir):
    if(filename.endswith('.htm') and filename not in ignoreList) and filename in reorderDict:        
        print(filename)
        screenID = reorderDict[filename]
        with open(filename, 'r',encoding="utf-8") as file :
            filedata = file.read()

        filedata = p.sub("'lblScreenName':'"+screenID+ "'",filedata)
        with open(filename, 'w',encoding="utf-8") as file:
            file.write(filedata)
            
        
            

        
       
