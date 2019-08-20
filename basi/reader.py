from search import findString
from random import random,gauss
import pandas as pd
import math
def excelFind(filename,condition):
    df=pd.read_excel(filename)
    df=df.where(condition)
    dropColumns=[name for name,value in df.any().items() if not value]
    df=df.drop(columns=dropColumns)
    return df.dropna()


def view(filename):
    sheets=pd.read_excel(filename,None)
    for sheet in sheets:
        df=pd.read_excel(filename,sheet)
        below=getBelow(df,'-V')
        if below is not None:
            list(below)

    
if __name__ == '__main__':
    fileName="example_data.xlsx"
    v=view(fileName)
    print(v)
    
    #condition=lambda a: issubclass(type(a),float) and int(a*10)==999
    #condition=lambda a: math.floor(a*10)==999
    #condition=lambda a: a > 98
    #val=excelFind('out.xlsx',condition)
    #print(val)
