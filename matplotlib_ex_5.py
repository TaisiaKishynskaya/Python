import matplotlib.pyplot as plt

x_values = range(1, 13)
y_values_fc = [2500, 2600, 2200, 3400, 3600, 2750, 2200, 2900, 3750, 3550, 2000, 2350]
y_values_fw = [1500, 1290, 1350, 1200, 1750, 1600, 1200, 1400, 1780, 1800, 2150, 1750]
BAR_WIDTH = 0.4

plt.bar(x_values, y_values_fc, color='blue', width=BAR_WIDTH, label='Facecream Sales Data')
plt.bar([x + BAR_WIDTH for x in x_values], y_values_fw, color='yellow', width=BAR_WIDTH, label='Facewash Sales Data')
plt.title('Facewash and Facecream Sales data')
plt.xlabel('Month Number')
plt.ylabel('Sales units in number')
plt.xticks([x + BAR_WIDTH / 2 for x in x_values], x_values)
plt.yticks(range(0, 4001, 500))
plt.grid(linestyle='--')
plt.show()
