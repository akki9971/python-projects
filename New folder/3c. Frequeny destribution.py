# create empty csv file using pandas
import csv
from sqlite3 import DateFromTicks
import pandas as pd

# df = pd.read_csv(r'news.csv')

ClassInterval = []
dict = {}

for i in range(10):
    l = 10*i
    h = 10*(i+1)
    ClassInterval.append(f'{l}-{h}')
    dict[i]=0

print(dict)

with open ("ungroupedData.txt", "r") as file:
    for num in file:
        n=int(num)
        for a in range(10,110,10):
            if (a-10)<n<a:
                dict[(a/10)-1]+=1
        # if n<10:
        #     dict[0]+=1
        # elif 10<=n<20:
        #     dict[1]+=1
        # elif 20<=n<30:
        #     dict[2]+=1
        # elif 30<=n<40:
        #     dict[3]+=1
        # elif 40<=n<50:
        #     dict[4]+=1
        # elif 50<=n<60:
        #     dict[5]+=1
        # elif 60<=n<70:
        #     dict[6]+=1
        # elif 70<=n<80:
        #     dict[7]+=1
        # elif 80<=n<90:
        #     dict[8]+=1
        # else:
        #     dict[9]+=1
            
print(dict)

Freq = list(dict.values())
print(Freq)


data={}

sno=[]
for a in range(10):
    sno.append(a+1)

data['S. No.'] = sno
data['Class Interval'] = ClassInterval
data['Frequency'] = Freq

dataframe = pd.DataFrame(data)
print(dataframe)

dataframe.to_csv(r'Frequency destribution.csv')