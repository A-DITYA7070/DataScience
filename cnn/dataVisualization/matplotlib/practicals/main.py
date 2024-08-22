import matplotlib.pyplot as plt
import numpy as np

# x = np.linspace(0,10,200)

# y = np.sin(x)

# plt.plot(x,y)

# plt.xlabel("this is my x data")
# plt.ylabel("this is my y data")
# plt.title("this is sin graph")

# plt.show()


# x = np.random.rand(50)
# y = np.random.rand(50)

# colors = np.random.rand(50)
# sizes = 1000 * np.random.rand(50)

# plt.scatter(x,y, c=colors, s=sizes, alpha=.5)
# plt.show()

# x = np.random.rand(500)
# y = np.random.rand(500)

# colors = np.random.rand(500)
# sizes = np.random.rand(50)

# plt.scatter(x,y,c=colors,alpha=.5)

# plt.show()

# x = ['a','b','c','d','e']
# y = np.random.rand(5)
# plt.bar(x,y)
# plt.xlabel("x axis")
# plt.ylabel("y axis")
# plt.title("bar graph")
# plt.show()

# x = ['a','b','c','d','e']
# y = np.random.rand(5)

# plt.barh(x,y)
# plt.xlabel("x axis")
# plt.ylabel("y axis")
# plt.title("bar graph")

# plt.show()

# x = np.random.rand(5)
# y = np.random.rand(5)


# plt.figure(figsize=(6,2))
# plt.plot(x,y,'--b')
# plt.xlabel("this is x data")
# plt.ylabel("this is y data")
# plt.title("graph")
# plt.grid()
# plt.show()


# x = np.random.rand(50)
# y = np.random.rand(50)
# colors = np.random.rand(50)
# sizes = 1000*np.random.rand(50)

# plt.scatter(x,y,c=colors,s=sizes,alpha=.5,marker='*')
# plt.xlabel("this is x axis")
# plt.ylabel("this is y axis")
# plt.title("scattered graph")
# plt.show()


# x = [4,5,2,4,5,23,42,4]
# y = [2,3,4,5,6,7,8,9]

# plt.plot(x,y)
# plt.show()

# x = [1,23,43,5,4,5,344]
# y = [1,34,32,34,32,34,2]
# plt.scatter(x,y)
# plt.show()


# data = [1,23,34,3,24,32,34,23,2,2,2,4]
# plt.hist(data)
# plt.show()






# Data
company = np.array(["Apple", "Microsoft", "Google", "AMD"])
profit = np.array([3000, 8000, 1000, 10000])

# Create a figure and a set of subplots
fig, axs = plt.subplots(1, 2, figsize=(14, 6))

# Vertical bar plot
axs[0].bar(company, profit, color=['red', 'blue', 'green', 'purple'])
axs[0].set_title('Vertical Bar Plot')
axs[0].set_xlabel('Company')
axs[0].set_ylabel('Profit')
axs[0].set_ylim(0, 11000)  # Set y-axis limit for better visualization

# Horizontal bar plot
axs[1].barh(company, profit, color=['red', 'blue', 'green', 'purple'])
axs[1].set_title('Horizontal Bar Plot')
axs[1].set_xlabel('Profit')
axs[1].set_ylabel('Company')
axs[1].set_xlim(0, 11000)  # Set x-axis limit for better visualization

# Adjust layout
plt.tight_layout()

# Display the plots
plt.show()