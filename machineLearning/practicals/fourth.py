#  Data interpolation technique ...
"""data interpolation is the process of estimating unknown values within a dataset based on the known values, many libraries can be
used for data interpolation such as numpy,scipy and pandas
1. Linear interpolation
2. Cubic interpolation with scipy
3. Polynomial interpolation """


# Linear interpolation...

import numpy as np
import matplotlib.pyplot as plt

# x = np.array([1,2,3,4,5])
# y = np.array([2,4,6,8,10])

# plt.scatter(x,y)
# plt.show()

# data interpolation using linear interpolation technique..

# x_new = np.linspace(1,5,10) #create new x values
# y_interp = np.interp(x_new,x,y)

# plt.scatter(x_new,y_interp)
# plt.show()


# Cubic interpolation with scipy.

from scipy.interpolate import interp1d

# create a cubic interpolation function.
# x = np.array([1,2,3,4,5])
# y = np.array([1,8,27,64,125])

# f = interp1d(x,y,kind='cubic')

# x_new = np.linspace(1,5,10)
# y_interp = f(x_new)

# plt.scatter(x_new,y_interp)
# plt.show()

# 3. polynomial interpolation..

x = np.array([1,2,3,4,5])
y = np.array([1,4,9,16,25])

p = np.polyfit(x,y,2)
x_new = np.linspace(1,5,10)
y_interp = np.polyval(p,x_new)

# plt.scatter(x,y)
plt.scatter(x_new,y_interp)
plt.show()








