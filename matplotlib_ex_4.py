import matplotlib.pyplot as plt

x_values = range(1, 13)
y_values = [4500, 5000, 5500, 6000, 6500, 7000, 7500, 8000]

plt.scatter(x_values, [5200, 5100, 4500, 5850, 4550, 4900, 4800, 5800, 6100, 8400, 7400, 7450], color='blue')
plt.title('Sales per Month')
plt.xlabel('Month Number')
plt.ylabel('Sales units a number')
plt.legend(['Tooth paste Sales Data'])
plt.xticks(x_values)
plt.yticks(y_values)
plt.grid(linestyle='--')
plt.show()
