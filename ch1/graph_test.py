import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0,12,0.01)
y = np.sin(t)

plt.figure(figsize=(10,6))

s1 = np.random.normal(loc=0, scale=1, size=1000)
s2 = np.random.normal(loc=5, scale=0.5, size=1000)

plt.grid()

plt.plot(s1, label='s1')
plt.plot(s2, label='s2')

plt.show()