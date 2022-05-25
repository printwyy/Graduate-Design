import pandas as pd
from datetime import datetime
from dateutil import parser
import xlwt

data=pd.read_excel('./saledata.xlsx')
res=[]
tim=list(data['outside_time'])
for i in tim:
    res.append(datetime.strptime(i, '%m/%d/%Y'))

print(res)
path=pd.ExcelWriter('out.xlsx')
w=pd.DataFrame(res)
w.to_excel(path,index=False)
path.save()