import os
from bs4 import BeautifulSoup
import json
import shutil
import csv
import fileinput
import re

p = re.compile("'lblScreenName':'.+?'")

#tarDir = r'C:\Users\cjackng\Desktop\Work\LCSD-PCS-2017Revamp\trunk\Prototype\screens\rename'
tarDir = r'D:\tmp\rename'
fieldNames = ['fileName', 'screenName']
reorderDict = {}

with open('pcs_screen_ids_html2.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')    
    for row in spamreader:
        if row[0] == 'fileName':
            continue
        fileName = row[0]
        screenID = row[1]
        reorderDict[fileName] = screenID

os.chdir(tarDir)
for filename in os.listdir(tarDir):
    if filename.endswith('.htm.png'):
        trimName = filename.replace('.png','')
        if trimName  in reorderDict:
            print(filename)
            screenID = reorderDict[trimName]
            os.rename(filename, screenID+'_'+filename)

            
        
            

        
       
