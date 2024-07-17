import matplotlib.pyplot as plt
import  numpy as np

# x = 3 + np.random.normal(0, 2, 50)
# y = 3 + np.random.normal(0, 2, len(x))

# plt.scatter(x,y)
# plt.xlabel("x-axis")
# plt.ylabel("y-axis")
# plt.title("scatter plot")
# plt.show()

# x1 = np.array([0, 1, 2, 3, 4, 5])
# y1 = np.array([0, 100, 200, 300, 400, 500])

# x2 = np.array([0, 1, 2, 3, 4, 5])
# y2 = np.array([50, 20, 40, 20, 60, 70])

# x3 = np.array([0, 1, 2, 3, 4, 5])
# y3 = np.array([10, 20, 30, 40, 50, 60])

# x4 = np.array([0, 1, 2, 3, 4, 5])
# y4 = np.array([200, 350, 250, 550, 450, 150])

# fig, axs = plt.subplots(2, 2, figsize=(10, 8))

# axs[0, 0].plot(x1, y1, label='Line 1')
# axs[0, 0].set_title('Plot 1')
# axs[0, 0].legend()

# axs[0, 1].plot(x2, y2, label='Line 2')
# axs[0, 1].set_title('Plot 2')
# axs[0, 1].legend()

# axs[1, 0].plot(x3, y3, label='Line 3')
# axs[1, 0].set_title('Plot 3')
# axs[1, 0].legend()

# axs[1, 1].plot(x4, y4, label='Line 4')
# axs[1, 1].set_title('Plot 4')
# axs[1, 1].legend()

# plt.tight_layout()

# plt.show()

box1 = np.random.normal(100, 10, 200)
box2 = np.random.normal(90, 20, 200)

plt.bar(box1,box2)
plt.show()
