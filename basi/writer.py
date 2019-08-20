from random import random,gauss
import pandas as pd
size=100
df=pd.DataFrame(
    {
        'voltage': [i for i in range(size)],
        'current': [gauss(i,2) for i in range(size)],
    })
df.to_excel('out.xlsx')
