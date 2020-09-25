import os
import shutil
import csv
from operator import itemgetter, attrgetter
from docx import Document
from docxtpl import DocxTemplate, InlineImage
from docx.shared import Mm, Inches, Pt

imgDir = r'C:\Users\cjackng\Desktop\Work\LCSD-PCS-2017Revamp\trunk\Prototype\screens\rename'

def myMain():
    tpl=DocxTemplate('ss_template.docx')
    pcsFuncList = []
    TraL=[]
    EnqL=[]
    rptL=[]
    SysL=[]
    GenL=[]
        
    
    with open('pcs_screen_ids.csv', newline='') as csvfile:                   
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')      

        for row in spamreader:
            if row[1] == 'screenName':
                continue 
            pcsFuncList.append({'funcID':'F-'+row[1],
                                'funcName':row[2],
                                'screenShot':getScreenShot(tpl,row[1]),
                                'idx':getIdx(row[1])
                                })

    context = {'pcsFuncList':sorted(pcsFuncList, key=itemgetter('idx','funcID'))}
    tpl.render(context)
    tpl.save('ss_test.docx')      

def getScreenShot(tpl, screenID):
    for file in os.listdir(imgDir):
        if file.startswith(screenID):
            return InlineImage(tpl,os.path.join(imgDir,file),width=Mm(100))        
    return None

def getIdx(screenID):
    if 'GEN' in screenID:
        return 0
    elif 'SYS' in screenID:
        return 1
    elif 'ENQ' in screenID:
        return 2
    elif 'TRN' in screenID:
        return 3
    elif 'RPT' in screenID:
        return 4
    elif 'HSK' in screenID:
        return 5
    else:
        return 6
 
if __name__ == '__main__':
    myMain()

        
