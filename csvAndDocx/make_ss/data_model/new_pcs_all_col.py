import re
import os
from bs4 import BeautifulSoup
import json
import shutil
import csv
from writeDCPlan import writeDCPlan

def IsNumType(inStr):
    return 'NUM' in inStr

   

class ColInfo:
    def __init__(self, csvRow):
        self.tableName = csvRow[0].upper()
        self.colName = csvRow[1].upper()
        self.dataType = csvRow[2].upper()
        self.dataLength = csvRow[4].replace('s',',') if IsNumType(self.dataType) else csvRow[3]
        self.isMandate = (csvRow[5] != 'Y')
        self.isPK = (csvRow[6] == 'Y')
        
    def toArray(self):
        return [self.colName,self.dataType,self.dataLength,
                'Yes' if self.isMandate else 'No',
                'Yes' if self.isPK else 'No']

    def isEqual(self, anotherCol):
        return anotherCol.tableName == self.tableName and anotherCol.colName == self.colName


def readCols(csvFileName):
    cols = []
    with open(csvFileName, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            if row[0] == 'TABLE_NAME':
                continue
            cols.append(ColInfo(row))
    return cols
                

def main():
    #p = re.compile(r'[^\d]')   
    resultList = [] #{'tableName':,'oldColList':,'newColList':}
    old_cols = readCols('old_col.csv')
    new_cols = readCols('new_col.csv')    
    rowMaps = []
    tableCols ={}
    for colO in old_cols:
        m = [colO, None]
        for colN in new_cols:
            if colO.isEqual(colN):
                m = [colO,colN]
        rowMaps.append(m)
    for m in rowMaps:
        tableName = m[0].tableName
        if m[1] is None:
            continue
        textRow = m[0].toArray() + [' '] + m[1].toArray()
        if tableName in tableCols:
            tableCols[tableName].append(textRow)
        else:            
            tableCols[tableName] = [textRow] 

    fileName = 'PCS-DC Plan_v0.0.1.xlsx'
    
    writeDCPlan(tableCols,fileName)
main()
            
                
            
                              
        
        
        
        
