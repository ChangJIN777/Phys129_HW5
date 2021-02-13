import sys
import os
import numpy as np
from matplotlib import pylab as plt
import cmath


def deterMandelbrot(c):
    """
        function used to determine whether the number c is in the Mandelbrot set
        c is a complex number
    """
    maxNum = 2
    limit = 250
    try:
        z = 0
        i = 0
        while i < limit:
            if abs(z) <= 2:
                z = z**2 + c
                i += 1
            else:
                return i
                break
        return 0
    except ValueError:
        print('Invalid input.')

# specify the size of the image
X = 512
Y = 384

pvals = np.zeros((X,Y), dtype='uint')

xinc = 3/X 
yinc = 2/Y 

for j in range(Y):
    for i in range(X):
        c = complex(i*xinc-2,j*yinc-1)
        pvals[i,j] = deterMandelbrot(c)

plotarr = np.flipud(pvals.transpose())

f1, ax1 = plt.subplots()
picture = ax1.imshow(plotarr, interpolation='none', cmap='twilight_shifted')
ax1.axis('off')
f1.show()
input('\nPress enter the exit\n')