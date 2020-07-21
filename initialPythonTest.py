# in order to use matplotlib normally, need to launch XLaunch first before running code 
import numpy as np
import matplotlib.pyplot as plt

print("Initial Git Test") 

t = np.arange(0, 25, 0.1)
f = np.sin(t)

fig = plt.subplots()
plt.plot(t, f)
plt.show()
 