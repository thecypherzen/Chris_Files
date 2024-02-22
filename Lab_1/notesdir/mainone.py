import numpy as np
import matplotlib.pyplot as plt

x_data = np.random.randint(1, 100 + 1, 50)
y_data = np.random.randint(1, 101 + 1, 50)

# generate a scatterplot
#plt.scatter(x_data, y_data, c="#222", marker="x", s=10,
#			alpha=0.3)

# generate a line chart
plt.plot(x_data, y_data, "r--", c="#00f", marker="*", lw=.7 )

# display
plt.show()
