import matplotlib.pyplot as plt
from numpy import loadtxt

data = loadtxt("circular.txt",float)
plt.imshow(data)
plt.show()
