import matplotlib.pyplot as plt

# 定义x轴和y轴的值
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# 创建一个图形
plt.figure()

# 绘制折线图
plt.plot(x, y, marker='o', linestyle='-', label='Line 1')

# 设置x轴和y轴的标签
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# 设置图例
plt.legend()

# 显示图形
plt.show()
