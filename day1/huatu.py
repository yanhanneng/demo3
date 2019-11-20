import matplotlib.pyplot as plt
import random

# # 1）创建画布(容器层)
# plt.figure(figsize=(10, 10))
# # 2）绘制折线图(图像层)
# plt.plot([1, 2, 3, 4, 5, 6 ,7], [17,17,18,15,11,11,13])
# # 3）显示图像
# plt.show()
x = range(60)
y_shanghai = [random.uniform(15, 18) for i in x]

# 1）创建画布
plt.figure(figsize=(20, 8), dpi=80)

# 2）绘制折线图
plt.plot(x, y_shanghai)

# 3）显示图像
plt.show()