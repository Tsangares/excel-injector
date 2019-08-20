from search import searchDataFrame

def getBelow(df,key):
    name,index=searchDataFrame(df,key)
    print(name,index)
    return column[1+index:None]
