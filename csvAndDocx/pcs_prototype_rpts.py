import re
import os
from bs4 import BeautifulSoup
import json
import shutil
import csv

def appendParts(parent,partName):
    partsHtm = r"components/rpt_parts/"+partName+".htm"
    parts_tag = soup.new_tag("div" )
    parts_tag['p-include']=partsHtm
    parts_tag['p-param']="{}"
    parent.append(parts_tag)


p = re.compile(r'[^\d]')
tarDir = r'C:\Users\cjackng\Desktop\Work\LCSD-PCS-2017Revamp\trunk\Prototype\Latest'
rptBase = os.path.join(tarDir,r'rptBase.htm')


with open('pcs_prototype_rpts.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        rptTitle = row[0] + ' - ' + row[1]
        rptParts = row[2].split('|')
        rptScreen = 'PCS-RPT-' + p.sub('', row[0])
        #filename = row[0]+"_"+row[1].replace(" ","_").replace("_/_","_") +".htm"
        filename = row[0] +".htm"
        soup = BeautifulSoup(open(rptBase,encoding='utf-8'),"html.parser")
        header = soup.find("div", {"id": "header"})
        header['p-param'] = header['p-param'].replace('rpt_title',rptTitle)
        rptCrt = soup.find("div", {"id": "rptCrt"})
        for part in rptParts:
            appendParts(rptCrt,part)
        appendParts(rptCrt,'format')  
        #rptCrt['p-include'] = rptCrt['p-include'].replace('rpt_type',rptType)
        footer = soup.find("div", {"id": "footer"})
        footer['p-param'] = footer['p-param'].replace('rpt_screen',rptScreen)
        with open(os.path.join(tarDir,filename), "wb") as file:
            file.write(soup.prettify("utf-8"))
            print(filename)



    
