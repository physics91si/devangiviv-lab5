#!/usr/bin/python

#The following statements are used to import numpy and matplotlib.
import numpy as np
import matplotlib.pyplot as plt


# numerically integrates values represented in array y
def integrate(y, dx):
     return np.sum((y*dx))

# Sets up arrays x and y = sin(x) and then plot them.

x1 = np.arange(0, np.pi, 0.01)
y1 = np.sin(x1)
plt.plot(x1,y1)
plt.show()

x2 = np.arange(0, np.pi, 0.01)
y2 = np.cos(x2)
plt.plot(x2,y2)
plt.show()

print(integrate(y1, 0.01))
print(integrate(y2, 0.01))

print(np.trapz(y1, x=None, dx=0.1))
print(np.trapz(y2, x=None, dx=0.1))

