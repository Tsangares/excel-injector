""" Injects lists or dictionaries into dataframes/excel files"""

import pandas as pd
from search import searchExcel,searchDataFrame
from collections import OrderedDict

class Injector:
    #filepath is the path to an excel file
    def __init__(self,filepath,sheet=None):
        self.excel=pd.read_excel(filepath,None)
        self.sheets=[s for s in self.excel]
        if type(sheet)==int:
            sheet=self.sheets[sheet]
        self.sheet=sheet
        self.filepath=filepath
                
    #Returns the pd.DataFrame of a specific sheet
    #sheet is either an integer or a name
    def getSheet(self,sheet=None):
        if sheet is not None: self.selectSheet(sheet)
        return self.excel[self.sheet]

    def setSheet(self,df,sheet=None):
        if sheet is not None: self.selectSheet(sheet)
        self.excel[self.sheet]=df

    def selectSheet(self,sheet):
        if type(sheet)==int:
            try:
                sheet=self.sheets[sheet]
            except IndexError:
                raise IndexError(f"Sheet index out of range. Sheet {sheet} does not exist.")
        if sheet in self.sheets:
            self.sheet=sheet
            return True
        return False

    def nextSheet(self):
        return self.selectSheet(list(self.excel).index(self.sheet)+1)
    

    #Inject data(list) wherever key is in the dataframe.
    #offset is the verticle dispacement from wherever the key is
    def injectList(self,data,key,offsetRow=1,offsetColumn=0,strict=False):
        sheet=self.getSheet()
        _column,_row=searchDataFrame(sheet,key,strict=strict)
        column=_column
        row=_row
        df=OrderedDict()
        for col in sheet.columns:
            df[col]=list(sheet[col])
            
        if offsetColumn != 0:
            column=sheet.columns[list(sheet.columns).index(column)+offsetColumn]
            
        if offsetRow is None: row=len(df[column])
        else: row+=offsetRow

        extension=row+len(data) - len(df[column])
        if extension > 0:
            #Pad the rest of the columns
            padding=['' for i in range(extension)]
            for col in sheet.columns:
                df[col]+=padding
                
        df[column][row:]=data
        
        self.setSheet(pd.DataFrame(df))
        return _column,_row

    def injectMatrix(self,arr_arr,key,offsetRow=1,offsetColumn=0,strict=False):
        for i,arr in enumerate(arr_arr):
            col,row=self.injectList(arr,key,offsetRow,i+offsetColumn,strict)

    def injectDict(self,dictionary,offsetRow=1,offsetColumn=0):
        for key,arr in dictionary.items():
            self.injectList(arr,key,offsetRow,offsetColumn,strict=True)

    #Sorting is a complex operation
    #Input a `dictionray` to be sorted.
    # The `key` is the string contents of a cell in the excel file used as the origin location
    # The `sortKey` is the column in the `dictionry` that will be sorted against the excel column at `key`
    # `offsetRow` lets you offset vertically the sorting start location based on cell with the contents of `key`
    # `offsetColumn` lets you offest horizonally the sorting start location
    # If `strict` is False then the search will only look for cells that CONTAIN `key`
    # If `strict` is  True then the search will only look for cells that  EQUALS `key`
    #Sorting simply tries to match two columns
    def sortDictionary(self,dictionary,key,sortKey,offsetRow=1,offsetColumn=0,strict=False):
        """Match one of the columns in the matrix with one in the excel."""
        return sortDataFrame(self,pd.DataFrame(dictionary),key,,sortKey,offsetRow,offsetColumn,strict)

    def sortDataFrame(self,df,key,column,offsetRow=1,offsetColumn=0,strict=False):
        sheet=self.getSheet()
        _column,_row=searchDataFrame(sheet,key,strict=strict)
        
        

    def save(self,duplicate=False,dryrun=False):
        filepath=self.filepath
        if duplicate:
            namePieces=filepath.split('.')
            namePieces[-2]+='_duplicate'
            filepath='.'.join(namePieces)
        if not dryrun:
            writer=pd.ExcelWriter(filepath)
            for sheet in self.excel:
                df=self.excel[sheet]
                columns=['' if 'Unnamed: ' in c else c for c in df.columns]
                df.to_excel(writer,sheet,index=False,header=columns)
            writer.close()
        print(f'Wrote to {filepath}')
    #What do I do about sorting?
    
if __name__=='__main__':
    #For testing
    ## PRESETS ##
    from random import gauss
    N=100
    filepath="example_data.xlsx"
    snippet=OrderedDict()
    snippet['voltage']=[i for i in range(N)]
    snippet['current']=[i*gauss(5,1) for i in range(N)]

    ## EXECUTE ##
    excel=Injector(filepath,sheet=0)
    for i in range(10):
        excel.nextSheet()
    import time
    excel.injectList(snippet['current'],'V',offsetRow=None,offsetColumn=1,strict=True)
    excel.save(duplicate=True)
    #Will inject the snipped overlapping the box that is equal to 'V'
    #If strict=False then boxes that contain a V are also vaild.
    #The injector will find the first box that matches the condition.
    #-# excel.inject(snippet,key='V',strict=True)
