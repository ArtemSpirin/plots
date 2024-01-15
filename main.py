import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import csv

content = pd.read_csv("C:/Video_Games.csv")
jp_sales = [content['JP_Sales'][i] for i in range(len(content['JP_Sales']))]
eu_sales = [content['EU_Sales'][i] for i in range(len(content['EU_Sales']))]
global_sales = [content['Global_Sales'][i] for i in range(len(content['Global_Sales']))]
sales = [[jp_sales[i],eu_sales[i],global_sales[i]] for i in range(len(jp_sales))]


plots_data = {}
platforms = set(content['Platform'])
for i in platforms:
    plots_data[i] = [0,0,0]
for i in range(len(sales)):
    for platform in platforms:
        if platform == content['Platform'][i]:
            for j in range(len(plots_data[platform])):
                plots_data[platform][j]+=sales[i][j]
pandas_data = pd.DataFrame(plots_data)
pandas_data.rename(index={0: "Sales in Japan", 1: "Sales in Europe", 2: "Global Sales"}, inplace=True)

pandas_data.plot(kind='bar',stacked = False,figsize=(16,9))
plt.xticks(rotation=0)
plt.ylabel('Millions of dollars')
plt.show()

