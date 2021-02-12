from scipy import special 
from matplotlib import pyplot as plt
import sys
import os
import math 
import numpy as np
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.colors import LogNorm


def Airy_pattern_gen(x):
    I_0 = 1
    J_1 = special.j1(x)
    I = I_0*((2*J_1)/(x))**2
    return I

# f1,ax = plt.subplot()
fig = plt.figure(num=1, clear=True)
ax1 = fig.add_subplot(1, 1, 1, projection='3d')

r = np.linspace(10**(-10),3.5*10**(-7),10000,endpoint=True) # normalized radius
theta = np.linspace(0,2*np.pi,10000)

R, T = np.meshgrid(r,theta)
X, Y = R*np.cos(T), R*np.sin(T)
f = 1 # m -- the focal length of the telescope
a = 10 # m -- the diameter of the lense 
Lambda = 7*(10**(-7)) # m -- assume we are looking at IR
x = np.pi*a*r/(Lambda*f)
R, T = np.meshgrid(x,theta)
X, Y = R*np.cos(T), R*np.sin(T)
I = Airy_pattern_gen(R)
surf = ax1.plot_surface(X,Y,I,cmap='binary',norm=LogNorm())
# ax1.set_zscale('log')
ax1.set_xlabel(r'x = r$\cdot cos\theta$')
ax1.set_ylabel(r'y = r$\cdot sin\theta$')
ax1.set_zlabel('Normalized Intensity')
fig.colorbar(surf,ax=ax1)
plt.show()