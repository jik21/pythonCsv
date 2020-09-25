import xlsxwriter


# Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook('PCS-DC Plan_v0.0.1.xlsx')
head_format = workbook.add_format({'bold': True})
tableName = 'ACCEPT'
worksheet = workbook.add_worksheet(tableName)

# Some data we want to write to the worksheet.
colsHeaders = [
    'Field Name', 'Field Format', 'Field Length', 'Mandatory', 'Primary Key','',
    'Field Name', 'Field Format', 'Field Length', 'Mandatory', 'Primary Key','Remarks'
]

worksheet.write(0, 0, 'Table Name:' ,head_format)
worksheet.write(0, 1, tableName)
worksheet.write(1, 0, 'Table Description:' ,head_format)
worksheet.write(0, 3, 'Text in Blue:' ,head_format)
worksheet.write(0, 4, 'Remain Field')
worksheet.write(1, 3, 'Text slashed:' ,head_format)
worksheet.write(1, 4, 'Deleted Field')
worksheet.write(2, 3, 'Text in Red:' ,head_format)
worksheet.write(2, 4, 'Clarification')
worksheet.write(4, 0, 'Source:' ,head_format)
worksheet.write(4, 1, tableName)
worksheet.write(4, 6, 'Converted to:' ,head_format)
worksheet.write(4, 7, tableName)

worksheet.set_column(0, 4, 15)
worksheet.set_column(5, 5, 5)
worksheet.set_column(6, 10, 15)
worksheet.set_column(11, 11, 30) 

col = 0
for h in colsHeaders:
    worksheet.write(5,col,h ,head_format)
    col+=1

row=6

workbook.close()
