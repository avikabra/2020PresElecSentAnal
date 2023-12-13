import numpy as np 
import matplotlib.pyplot as plot 
 
# Make a data definition
a1 = [2.2, 2.7, 3.2, 3.7, 4.2, 4.7]
b1 = [2, 5, 8, 11, 14, 17]
 
a2 = [4, 10, 14, 20, 24, 32]
b2 = [2.3, 5.5, 11, 18, 8.9, 10.2]
 
r1 = np.arange(6)
width1 = 0.5
 
# Create the first subplot
plot.subplot(1, 2, 2)
plot.bar(r1, a1, width=width1)
plot.bar(r1 + width1, b1, width=width1)
 
# Create the second subplot
plot.subplot(1, 2, 1)
plot.bar(r1, a2, width=width1)
plot.bar(r1 + width1, b2, width=width1)
 
# Display the plot
plot.show()