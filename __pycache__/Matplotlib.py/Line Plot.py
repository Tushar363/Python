# Draw two points in the diagram, one at position (1,3) and one at position (8,10):
# import matplotlib.pyplot as plt
# import numpy as np
# xpoints = np.array([0,6])
# ypoints = np.array([0,250])
# plt.plot(xpoints, ypoints,'o')#*,+,-
# plt.show()


# #Plotting without x-points:
# import matplotlib.pyplot as plt
# import numpy as np
# ypoints = np.array([3,8,1,10,5,7])
# plt.plot(ypoints)
# plt.show()

# import numpy as np
# import matplotlib.pyplot as plt
# x = np.array([80,85,90,95,100,105,110,115,120,125])
# y = np.array([240,250,260,270,280,290,300,310,320,330])
# plt.plot(x, y)
# plt.title()
# plt.xlabel()
# plt.ylabel()

import matplotlib.pyplot as plt
import numpy as np
#Plot 1:
x = np.array([0,1,2,3])
y = np.array([3,8,1,10])
plt.subplot(1,2,1)
plt.plot(x,y)
#Plot 2:
x = np.array([0,1,2,3])
y = np.array([10,20,30,40])
plt.subplot(1,2,2)
plt.plot(x,y)
plt.show()