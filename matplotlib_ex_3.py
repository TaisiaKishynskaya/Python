import csv
import matplotlib.pyplot as plt
import pandas as pd

# define the data as a list of dictionaries
data = [
    {'Month Number': '1', 'Product A': 9500, 'Product B': 5500, 'Product C': 1500, 'Face cream Sales Data': 2400,
     'Product E': 1100},
    {'Month Number': '2', 'Product A': 6000, 'Product B': 5400, 'Product C': 1000, 'Face cream Sales Data': 2500,
     'Product E': 2000},
    {'Month Number': '3', 'Product A': 10000, 'Product B': 4100, 'Product C': 1100, 'Face cream Sales Data': 2000,
     'Product E': 3800},
    {'Month Number': '4', 'Product A': 9000, 'Product B': 6000, 'Product C': 900, 'Face cream Sales Data': 3800,
     'Product E': 1900},
    {'Month Number': '5', 'Product A': 8000, 'Product B': 4100, 'Product C': 1900, 'Face cream Sales Data': 3900,
     'Product E': 1800},
    {'Month Number': '6', 'Product A': 6500, 'Product B': 4200, 'Product C': 1800, 'Face cream Sales Data': 2800,
     'Product E': 1900},
    {'Month Number': '7', 'Product A': 8500, 'Product B': 4250, 'Product C': 1100, 'Face cream Sales Data': 3900,
     'Product E': 1850},
    {'Month Number': '8', 'Product A': 9550, 'Product B': 6000, 'Product C': 1300, 'Face cream Sales Data': 3700,
     'Product E': 2400},
    {'Month Number': '9', 'Product A': 7900, 'Product B': 6100, 'Product C': 1600, 'Face cream Sales Data': 3800,
     'Product E': 2100},
    {'Month Number': '10', 'Product A': 10100, 'Product B': 8100, 'Product C': 2000, 'Face cream Sales Data': 2000,
     'Product E': 2200},
    {'Month Number': '11', 'Product A': 13000, 'Product B': 7000, 'Product C': 2100, 'Face cream Sales Data': 2100,
     'Product E': 2250},
    {'Month Number': '12', 'Product A': 14900, 'Product B': 7100, 'Product C': 1900, 'Face cream Sales Data': 1900,
     'Product E': 2600},
]

# write the data to a CSV file
with open('product_sales.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=['Month Number', 'Product A', 'Product B', 'Product C',
                                              'Face cream Sales Data', 'Product E'])
    writer.writeheader()
    writer.writerows(data)

# load the data from the CSV file
data = pd.read_csv('product_sales.csv')

# set the tick values for the X axis
plt.xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
plt.yticks([1000, 2000, 4000, 6000, 8000, 10000, 12000, 15000, 18000])

# plot the data
plt.plot(data['Month Number'], data['Product A'], 'ro-', label='ToothPaste Sales Data', linewidth=3)
plt.plot(data['Month Number'], data['Product B'], 'gv-', label='ToothPaste Sales Data', linewidth=3)
plt.plot(data['Month Number'], data['Product C'], 'bs-', label='ToothPaste Sales Data', linewidth=3)
plt.plot(data['Month Number'], data['Face cream Sales Data'], 'c^-', label='Face cream Sales Data', linewidth=3)
plt.plot(data['Month Number'], data['Product E'], 'm*-', label='ToothPaste Sales Data', linewidth=3)

# set the axis labels and title
plt.xlabel('Month Number')
plt.ylabel('Sales units a number')
plt.title('Sales Data')

# add a legend
plt.legend()

#  display the plot
plt.show()
