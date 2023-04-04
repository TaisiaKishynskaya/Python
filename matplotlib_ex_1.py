import csv
import matplotlib.pyplot as plt
import pandas as pd

# define the data as a list of tuples
data = [(1, 20000), (2, 15000), (3, 25000), (4, 24000), (5, 23000), (6, 20000), (7, 30000), (8, 35000), (9, 21000),
        (10, 25000), (11, 41000), (12, 29000)]

# write the data to a CSV file
with open('total_profit_data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Month Number', 'Total Profit'])
    writer.writerows(data)

# read the data from the CSV file into a Pandas DataFrame
df = pd.read_csv('total_profit_data.csv')

# extract the Month Number and Total Profit columns from the DataFrame
month_numbers = df['Month Number']
total_profits = df['Total Profit']

# create a line plot
plt.plot(month_numbers, total_profits, marker='o')

# set the X label name and Y label name
plt.xlabel('Month Number')
plt.ylabel('Total profit')

# set the Y axis limits to display only profits between 10000 and 50000
plt.ylim([10000, 50000])

# set the X axis limits to display only the first 12 months
plt.xlim([0, 13])

# set the tick values for the Y axis
plt.yticks([10000, 20000, 30000, 40000, 50000])

# set the tick values for the X axis
plt.xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

# set the title of the plot
plt.title('Company profit per month')

# show the plot
plt.show()
