import re
import os
from bs4 import BeautifulSoup
import json
import shutil
import csv

p = re.compile(r'[^\d]')
tarDir = r'C:\Users\cjackng\Desktop\Work\LCSD-PCS-2017Revamp\trunk\Prototype\Latest'
rptBase = os.path.join(tarDir,r'rptBase.htm')


with open('pcs_all_col.csv', newline='') as csvfile:
    with open('pcs_all_col_2.csv', 'w',newline='') as csvfile_out:
        spamwriter = csv.writer(csvfile_out, delimiter=',',
        quotechar='|', quoting=csv.QUOTE_NONE)
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            dType = row[2]            
            if 'VARCHAR2' in dType:
                row[2] = row[2].replace('VARCHAR2','VARCHAR2'+ '('+ row[3] + ')' )            
            spamwriter.writerow(row)

        
                
