import sys
import os
import numpy as np
from matplotlib import pylab
import cmath
import math

c = -1 + 0j
limit = 250
i = 0
z = 0 + 0j
while i < limit:
    z = z**2 + c
    i += 1
print(z)