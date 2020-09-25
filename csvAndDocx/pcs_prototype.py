import os
from bs4 import BeautifulSoup
import json
import shutil

ignoreList = ['rptBase.htm']
tarDir = r'C:\Users\cjackng\Desktop\Work\LCSD-PCS-2017Revamp\trunk\Prototype\Latest'
os.chdir(tarDir)
if os.path.exists("out"):
    shutil.rmtree('out')    
os.makedirs("out")
    
for filename in os.listdir(tarDir):
    if(filename.endswith('.htm') and filename not in ignoreList):
        print(filename)
        soup = BeautifulSoup(open(filename,encoding='utf-8'),"html.parser")
        allDiv = soup.findAll('div')
        for div in allDiv:
            if div.has_attr('p-include'):
                compo = div['p-include']
                compoSoup = BeautifulSoup(open(compo,encoding='utf-8'),"html.parser")
                if (div['p-param']!=""):
                    params = json.loads(div['p-param'].replace("'","\""))
                    for k,v in params.items():                    
                        element = compoSoup.find("span",{'id':k})                    
                        if element is not None:                        
                            element.replace_with(v)
                div.append(compoSoup)
                
                
        #with open('out\\'+filename, "w",encoding = 'utf-8') as file:            
            #file.write(str(soup))
        with open('out\\'+filename, "wb") as file:            
            file.write(soup.prettify("utf-8"))
    elif(os.path.isdir(filename)) and filename!="out":
        shutil.copytree(filename, "out\\"+filename)
        
                
