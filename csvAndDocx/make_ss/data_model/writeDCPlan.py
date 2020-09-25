import xlsxwriter


def writeDCPlan(tableCols,fileName):
    # Create a workbook and add a worksheet.
    workbook = xlsxwriter.Workbook(fileName)
    head_format = workbook.add_format({'bold': True})
    colHead_format = workbook.add_format({'bg_color':'#1F497D',
                                          'bold': True,
                                          'font_color': 'white',
                                          'border':1})
    colContent_format = workbook.add_format({'border':1})
    
    for tableName,cols in tableCols.items():        
        worksheet = workbook.add_worksheet(tableName)

        # Some data we want to write to the worksheet.
        colsHeaders = [
            'Field Name', 'Field Format', 'Field Length', 'Mandatory', 'Primary Key','',
            'Field Name', 'Field Format', 'Field Length', 'Mandatory', 'Primary Key','Remarks'
        ]

        worksheet.write(0, 0, 'Table Name:' ,head_format)
        worksheet.write(0, 1, tableName)
        worksheet.write(1, 0, 'Table Description:' ,head_format)
        worksheet.write(1, 1, 'Data for ' +tableName)
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

        worksheet.set_column(0, 0, 20)
        worksheet.set_column(1, 4, 15)
        worksheet.set_column(5, 5, 5)
        worksheet.set_column(6, 6, 20)
        worksheet.set_column(7, 10, 15)
        worksheet.set_column(11, 11, 50) 

        col = 0
        for h in colsHeaders:
            worksheet.write(5,col,h ,colHead_format)
            col+=1

        row=6
        for colToWrite in cols:
            col = 0
            for txt in colToWrite:                    
                worksheet.write(row,col,txt,colContent_format)
                col = col + 1
            worksheet.write(row,col,'',colContent_format)#Remarks
            
            row = row + 1


    workbook.close()
