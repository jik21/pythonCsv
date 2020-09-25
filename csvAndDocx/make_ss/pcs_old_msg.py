import os
import csv
import re
from operator import itemgetter, attrgetter

curFile = ''
curMethod = ''
resultList = []
fieldNames = ['file','method','lvl','Content','MatchWith']
ltrim = re.compile(r'===.+?===(.+)')
rtrim = re.compile(r'(.+)\(\d.+usages? found\)')
msgP = re.compile (r'.+add(.+?)Msg\((.+)\)')
screenIDs = {}

def myTrim(s):    
    s = ltrim.sub(r'\1',s)    
    s = rtrim.sub(r'\1',s)    
    return s.strip()

def getScrID(javaFileName,l):
    f = javaFileName.replace('.java','.htm').upper().strip()
    if f in l:        
        return l[f]
    return ''

with open('pcs_screen_ids.csv', 'r', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')    
    for row in spamreader:
        if row[0] == 'fileName':
            continue
        fileName = row[0].upper()
        screenID = row[1]
        screenIDs[fileName] = screenID

with open('javaSearch.txt', 'r') as f:
     for line in f:
         if line.startswith("===fileLvl==="):
            curFile = myTrim(line)
         elif line.startswith("===methodLvl==="):
            curMethod = myTrim(line)
         else:            
            msg = myTrim(line)
            m = msgP.match(msg)
            if m is not None:
                msgLvl = m.group(1)
                msgContent = m.group(2)
            elif 'add' in line:
                msgLvl = 'abnormal'
                msgContent = line
            else:
                continue

            screenID = getScrID(curFile,screenIDs)
            resultList.append({'file':curFile,'method':curMethod,
                                'lvl':msgLvl,'Content':msgContent,'MatchWith':screenID})

resultList = sorted(resultList, key = itemgetter('file', 'method'))
with open('pcs_old_msg.csv', 'w',newline='') as csvfile:    
    w = csv.DictWriter(csvfile, fieldnames=fieldNames)
    w.writeheader()
    for r in resultList:
        w.writerow(r)
        
