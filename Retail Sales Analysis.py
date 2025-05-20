from cProfile import label
from itertools import count

import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
from packaging.markers import Marker

filenames = os.listdir('SalesData')
edf = pd.DataFrame()
for filename in filenames:
    df = pd.read_csv(f'SalesData/{filename}')
    edf = pd.concat([edf, df])
edf.to_csv('Sales.csv', index=False)

df = pd.read_csv('Sales.csv')
df = df.dropna(how='all')
df = df.loc[df['Quantity Ordered'] != 'Quantity Ordered']
df['Quantity Ordered'] = df['Quantity Ordered'].astype(int)
df['Price Each'] = df['Price Each'].astype(float)
df['Order Date'] = pd.to_datetime(df['Order Date'])
df.to_csv('Sales.csv', index=False)
df['amount'] = df['Quantity Ordered'] * df['Price Each']


def findcity(address):
    return address.split(",")[1]


df['City'] = df['Purchase Address'].apply(findcity)

df['City'] = df['Purchase Address'].str.split(',', expand=True)[1]
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['month'] = df['Order Date'].dt.month
df['month name'] = df['Order Date'].dt.month_name()
df['day name'] = df['Order Date'].dt.day_name()
df.to_csv('Sales.csv', index=False)

revenue = df['amount'].sum()
ndf = df.groupby(['month', 'month name']).agg(
    total=('amount', 'sum'),
    avg=('amount', 'mean'))
ndf = ndf.reset_index()
ndf.to_csv("Analysis/MontlySales.CSV", index=False)

df = pd.read_csv('Analysis/MontlySales.csv')
plt.figure(figsize=(15, 10))
plt.plot(df['month name'], df['total'], marker='o', label='Sale')
plt.title('Monthly Sales')
plt.xlabel("Month")
plt.ylabel("Sale")
for x, y in zip(df['month name'], df['total']):
    plt.text(x, y, y)
plt.legend
plt.grid()
plt.savefig('Analysis/MonthlySales.png')
s = df['day name'].value_counts()
plt.figure(figsize=(15, 10))
plt.bar(s.index, s.values, color='green')
plt.title('Number of orders')
plt.grid()
plt.xlabel('days')
plt.ylabel('orders')
for x, y in zip(s.index, s.values):
    plt.text(x, y, y)
s.to_csv('Analysis/Ordersbyday.csv')
plt.savefig('Analysis/Ordersbyday.png')

df['IsHoliday'] = False
df.loc[df['day name'].isin(['Saturday', 'Sunday']), 'IsHoliday'] = True
ndf = df.groupby('IsHoliday').agg(
    avgsale=('amount', 'mean')
)
ndf = df.groupby('City').agg(
    order=('City', 'count'),
    qunatity=('Quantity Ordered', 'sum'),
    revenue=('amount', 'sum')
)
ndf.reset_index()
ndf.to_csv('Analysis/City.csv')
df = pd.read_csv('Analysis/City.csv')
x_pos = np.arange(0, 9)
plt.figure(figsize=(10, 5))
plt.bar(x_pos, df['order'], color='green', label='Order')
plt.bar(x_pos + .2, df['qunatity'], color='blue', label='qunatity', width=.4)
plt.title('City-wise Order Analysis')
plt.xlabel('City')
plt.ylabel('Order Count')
plt.xticks(x_pos, df['City'])
rotate
city
names if too
long
plt.grid()
plt.legend()
plt.tight_layout()
plt.savefig('Analysis/City.png')
plt.show()

ndf = df.loc[df['Order ID'].duplicated(keep=False)]

ndf = ndf.groupby('Order ID').agg(group=('Product', lambda x: ','.join(x.astype(str))))

ndf['group'] = ndf['group'].str.strip(',')

ndf.reset_index()
ndf.to_csv('Analysis/duplicate.csv')

from itertools import combinations
from collections import Counter

df = pd.read_csv('analysis/duplicate.csv')
df['group'] = df['group'].str.split(',')
l = list(df['group'])
count = Counter()

for sublist in l:
    count.update(Counter(combinations(sublist, 2)))
print(count)





