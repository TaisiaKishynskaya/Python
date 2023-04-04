import matplotlib.pyplot as plt
import pandas as pd


# read the data from the CSV file into a Pandas DataFrame
df = pd.read_csv('total_profit_data.csv')

# extract the Month Number and Total Profit columns from the DataFrame
month_numbers = df['Month Number']
total_profits = df['Total Profit']

# create a line plot
plt.plot(month_numbers, total_profits, linestyle='dotted', marker='o', markersize=8, markerfacecolor='red',
         linewidth=3, color='red', label='Sold units')

# set the X label name and Y label name
plt.xlabel('Month Number')
plt.ylabel('Sold units number')

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

# show the legend at the lower right location
plt.legend(loc='lower right')

# show the plot
plt.show()
