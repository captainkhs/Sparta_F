import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

x = np.linspace(0, 1000, 150)
plt.plot(x, np.sin(x))
plt.show()