import pandas as pd
import numpy as np
from scipy import stats
from sys import argv[1]
a=pd.read_table(argv[1],header=0,index_col=0)
b=pd.read_table(argv[2],header=0,index_col=0)

out= open(argv[3],"wt")
for i in range(1,len(a)+1):
    out.write("ID1"+"\t"+"ID2"+"\t"+"pearsonr"+"\t"+"pvalue"+"\n")
    for j in range(1,len(b)+1):
        x=a.iloc[i-1]
        x=x.tolist()
        y=b.iloc[j-1]
        y=y.tolist()
        (p,q)=stats.pearsonr(x,y)
        print(p)
        out.write(a.index[i-1]+"\t"+b.index[j-1]+"\t"+str(p)+"\t"+str(q)+"\n")
        
    
out.close()    