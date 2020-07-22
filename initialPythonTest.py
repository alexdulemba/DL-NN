# runs well on WSL2 for windows
# in order to use matplotlib normally, need to launch XLaunch first before running code in order to display plot

import numpy as np
import matplotlib.pyplot as plt

print("Initial Git Test") 

t = np.arange(0, 25, 0.1)
f = np.sin(t)

fig = plt.subplots()
plt.plot(t, f)
plt.show()
 