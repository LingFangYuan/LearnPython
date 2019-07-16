import matplotlib.pyplot as plt
#from mpl_toolkits import mplot3d
import numpy as np

x = np.arange(-10, 10, 0.01)
y = np.arange(-5, 5, 0.01)
x, y = np.meshgrid(x, y)
z = x**2 / 20.0 + y**2
mask = z > 7
z[mask] = 0

#ax = plt.axes(projection='3d')
plt.contour(x, y, z)
plt.ylim(-10, 10)
plt.xlim(-10, 10)
plt.show()
