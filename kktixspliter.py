import pandas as pd
filename = 'kktix.csv'
content = pd.read_csv(filename, sep = ',', decimal = '.', header = None, names = ['city', 'category', 'date', 'title'], encoding = 'utf-8')
Entertainment = pd.DataFrame(columns = ('city','category','date','title'))
Food = pd.DataFrame(columns = ('city','category','date','title'))
Sports = pd.DataFrame(columns = ('city','category','date','title'))
Uncategorized = pd.DataFrame(columns = ('city','category','date','title'))
Learning = pd.DataFrame(columns = ('city','category','date','title'))
Outdoors = pd.DataFrame(columns = ('city','category','date','title'))
Networking = pd.DataFrame(columns = ('city','category','date','title'))
Gathering = pd.DataFrame(columns = ('city','category','date','title'))
categoryList = [
    'Entertainment',
    'Food',
    'Sports',
    'Uncategorized',
    'Learning',
    'Outdoors',
    'Networking',
    'Gathering'
]
Entertainment.loc[len(Entertainment)] = content.values[0];
Food.loc[len(Food)] = content.values[0];
Sports.loc[len(Sports)] = content.values[0];
Uncategorized.loc[len(Uncategorized)] = content.values[0];
Learning.loc[len(Learning)] = content.values[0];
Outdoors.loc[len(Outdoors)] = content.values[0];
Networking.loc[len(Networking)] = content.values[0];
Gathering.loc[len(Gathering)] = content.values[0];
for i in range(1, 2219):
    if content.category[i] == categoryList[0]:
        Entertainment.loc[len(Entertainment)] = content.values[i]
for i in range(1, 2219):
    if content.category[i] == categoryList[1]:
        Food.loc[len(Food)] = content.values[i]
for i in range(1, 2219):
    if content.category[i] == categoryList[2]:
        Sports.loc[len(Sports)] = content.values[i]
for i in range(1, 2219):
    if content.category[i] == categoryList[3]:
        Uncategorized.loc[len(Uncategorized)] = content.values[i]
for i in range(1, 2219):
    if content.category[i] == categoryList[4]:
        Learning.loc[len(Learning)] = content.values[i]
for i in range(1, 2219):
    if content.category[i] == categoryList[5]:
        Outdoors.loc[len(Outdoors)] = content.values[i]
for i in range(1, 2219):
    if content.category[i] == categoryList[6]:
        Networking.loc[len(Networking)] = content.values[i]
for i in range(1, 2219):
    if content.category[i] == categoryList[7]:
        Gathering.loc[len(Gathering)] = content.values[i]
Entertainment.to_csv("Entertainment.csv", index = False, sep = ',', decimal = '.', header = None, columns = ['city', 'category', 'date', 'title'], encoding = 'utf-8')
Food.to_csv("Food.csv", index = False, sep = ',', decimal = '.', header = None, columns = ['city', 'category', 'date', 'title'], encoding = 'utf-8')
Sports.to_csv("Sports.csv", index = False, sep = ',', decimal = '.', header = None, columns = ['city', 'category', 'date', 'title'], encoding = 'utf-8')
Uncategorized.to_csv("Uncategorized.csv", index = False, sep = ',', decimal = '.', header = None, columns = ['city', 'category', 'date', 'title'], encoding = 'utf-8')
Learning.to_csv("Learning.csv", index = False, sep = ',', decimal = '.', header = None, columns = ['city', 'category', 'date', 'title'], encoding = 'utf-8')
Outdoors.to_csv("Outdoors.csv", index = False, sep = ',', decimal = '.', header = None, columns = ['city', 'category', 'date', 'title'], encoding = 'utf-8')
Networking.to_csv("Networking.csv", index = False, sep = ',', decimal = '.', header = None, columns = ['city', 'category', 'date', 'title'], encoding = 'utf-8')
Gathering.to_csv("Gathering.csv", index = False, sep = ',', decimal = '.', header = None, columns = ['city', 'category', 'date', 'title'], encoding = 'utf-8')
