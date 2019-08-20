""" Injects lists or dictionaries into dataframes/excel files
 _____
|1   2|
|     | Mapping for loc variable
|3___4|

"""

import pandas as pd
from search import searchExcel,searchDataFrame

class Injector:
    _tl=TOP_LEFT=1
    _tr=TOP_RIGHT=2
    _bl=BOTTOM_LEFT=3
    _br=BOTTOM_RIGHT=4
    LOC_DEFAULT=TOP_LEFT
    #Source is either the path to a excel file or a dataframe
    def __init__(self,source):
        if type(source)==str:
            source=pd.read_excel(source)
        self.df=source

    def inject(self,obj,key,loc=LOC_DEFAULT,offset=(0,0),strict=False):
        if type(obj)==pd.DataFrame:
            return self.injectDataFrame(obj,key,loc,offset,strict)
        elif type(obj)==dict:
            return self.injectDictionary(obj,key,loc,offset,strict)
        else:
            print("Failed to inject")
            return None

    def injectDictionary(self,dictionary,key,loc=LOC_DEFAULT,offset=(0,0),strict=False):
        return self.injectDataFrame(source,pd.DataFrame(dictionary),key,loc,offset,strict)

    def injectDataFrame(self,df,key,loc=LOC_DEFAULT,offset=(0,0),strict=False):
        column,row=searchDataFrame(self.df,key,strict)
        x,y=offset
        if x != 0:
            column=self.df.columns[self.df.columns.at(column)+x)]
        row+=y
        
        pass


            
if __name__=='__main__':
    #For testing
    ## PRESETS ##
    from random import gauss
    N=100
    filename="example_data.xlsx"
    snipped={
        'voltage': [i for i in range(N)],
        'current': [i*gauss(5,1) for i in range(N)],
    }
    ## EXECUTE ##
    excel=Injector(filename)


    #Will inject the snipped overlapping the box that is equal to 'V'
    #If strict=False then boxes that contain a V are also vaild.
    #The injector will find the first box that matches the condition.
    #-# excel.inject(snippet,key='V',strict=True)
