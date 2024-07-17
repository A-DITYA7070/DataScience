import matplotlib.pyplot as plt
import numpy as np

# x = np.linspace(0,10,200)

# y = np.sin(x)

# plt.plot(x,y)

# plt.xlabel("this is my x data")
# plt.ylabel("this is my y data")
# plt.title("this is sin graph")

# plt.show()


x = np.random.rand(50)
y = np.random.rand(50)

colors = np.random.rand(50)
sizes = 1000 * np.random.rand(50)

plt.scatter(x,y, c=colors, s=sizes, alpha=.5)
plt.show()
