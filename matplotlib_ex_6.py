import matplotlib.pyplot as plt

x_values = range(1, 13)
y_values_fc = [9100, 6100, 9750, 8950, 7800, 7600, 8950, 9900, 8100, 10200, 13200, 14200]

plt.bar(x_values, y_values_fc, color='blue')
plt.title('Bathingsoap sales data')
plt.xlabel('Month Number')
plt.ylabel('Number of units sold')
plt.xticks(x_values)
plt.yticks(range(0, 14500, 2000))
plt.grid(linestyle='--')
plt.show()
