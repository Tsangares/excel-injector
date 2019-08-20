"""Utility to get the excel column and row from a keyword"""
import pandas as pd

#Input dataframe(excelfile) and keyword(string)
#Return list of associated columns
def searchColumns(df,key,strict=False):
    if strict:
        result=df.apply(lambda row: row.astype(str).str.equals(key)).any()
    else:
        result=df.apply(lambda row: row.astype(str).str.contains(key)).any()
    hits=[column for column,value in result.items() if value ]
    if len(hits) == 0: return None
    else: return hits

#Input a panda.Series and keyword(string)
#Return the row index(int) of associated row
def searchSeries(row,key,strict=False):
    assert(type(row)==pd.Series,"Use a pandas.Series")
    if strict:
        res=[index for index,k in row.astype(str).str.equals(key).items() if k]
    else:
        res=[index for index,k in row.astype(str).str.contains(key).items() if k]
    if len(res) != 0: return res
    else: return None

#Input a dataframe(excelfile) and keyword(string)
#Return tuple(column(str),row(int)) of the location of keyboword
#Return None,None if string is not found
#Set n=None to get a list, defaults to first hit)
def searchDataFrame(df,key,n=0,strict=False):
    assert(type(df)==pd.DataFrame,"Use a pandas.DataFrame.")    
    columns=searchColumns(df,key,strict)
    if columns is not None:
        column=columns[0]
        index=searchSeries(column,key,strict)
        if index is not None:
            if n is None: return column, index
            else: return column, index[n]
    return None,None

#Input the path to an excel file and a keyword(str)
#Return a tuple (column(str),row(int)) of the location of the word
#Return None,None if the string is not found.
#Set n=None to get a list, defaults to first hit)
def searchExcel(filename,key,n=0,strict=False):
    df=pd.read_excel(filename)
    return searchDataFrame(df,key,n,strict)
