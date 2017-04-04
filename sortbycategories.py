import pandas as pd
 #Your csv path
a=pd.read_csv("201404.csv",sep=',',decimal='.',header=None,names=['index','no','name','location','incharge','capital','date'],encoding='utf-8') ##read the csv file
ai=a.values[1:,2]
ac={}
t= [
    '其他',
    '投資',
    '設計',
    '餐飲',
    '化學',
    '音樂',
    '廣告'
]
##t is the categories library

def cate():
    types = []
    types.append('類型')
    for i in ai:
        if t[1] in i:
            types.append(t[1])
        elif t[2] in i:
            types.append(t[2])
        elif t[3] in i:
            types.append(t[3])
        elif t[4] in i:
            types.append(t[4])
        elif t[5] in i:
            types.append(t[5])
        elif t[6] in i:
            types.append(t[6])
        else:
            types.append(t[0])
    return types

a['type'] = pd.Series(cate())

a.to_csv("b.csv",index=False,sep=',',decimal='.',header=None,columns=['index','no','name','type','location','incharge','capital','date'],encoding='utf-8')
