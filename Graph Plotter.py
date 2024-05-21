import matplotlib.pyplot as plt


left = [1, 2, 3, 4, 5]  
height = [10, 11, 23, 36, 4]
tick_label = ['one', 'two', 'three', 'four', 'five']


plt.bar(left, height, tick_label=tick_label, width=0.8, color='blue')


x = [2, 4, 5, 6]
y = [10, 11, 23, 36]


plt.plot(x, y, color='green', linestyle='dashed', linewidth=3, marker='o', markerfacecolor='blue', markersize=12, label="Line 1")


x2 = [1, 2, 3, 4]
y2 = [1, 2, 4, 4]


plt.plot(x2, y2, label='Line 2')


plt.ylim(0, 40)
plt.xlim(0, 6)


plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('Demo Graph - Bar Chart and Line Plot')


plt.legend()


plt.show()
