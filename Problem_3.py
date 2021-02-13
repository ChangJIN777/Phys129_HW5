import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import time

# image size 
X = 512
Y = 512

pvals = np.zeros((X,Y,3), dtype='uint8')

rinc = 255/X
binc = 255/Y

# 
# set the border pixels to white (requirement 1)
# 
borderbottom1 = 0
bordertop1 = int(Y/10)
borderbottom2 = int(Y-Y/10)
bordertop2 = Y
borderbottom3 = 0
bordertop3 = int(X/10)
bordertop4 = X
borderbottom4 = int(X-X/10)

for j in range(Y):
       for i in range(X):
           pvals[i,j,0] = 0x0  # red
           pvals[i,j,1] = 0x0    # green
           pvals[i,j,2] = 0xff  # blue

#
# have a filled blue triangle (requirement 2)
# 
for j in range(Y):
       for i in range(X):
           if j>i*(3/4):
               pvals[i,j,0] = 0xff  # red
               pvals[i,j,1] = 0xff    # green

#
# cut a white triangle inside the filled blue triangle (requirement 3)
#
for j in range(Y):
       for i in range(X):
           if j<=(i*(3/4)-Y//15) and (j>(bordertop1+Y//20)) and (i<(Y-(bordertop3+Y//20))):
               pvals[i,j,0] = 0xff  # red
               pvals[i,j,1] = 0xff  # green

# initialize the image
plotarr = np.flipud(pvals.transpose(1,0,2))
f1, ax1 = plt.subplots()
picture = ax1.imshow(plotarr, interpolation='none')
ax1.axis('off')
f1.show()
f1.canvas.draw()

# update the image based on requirement 1
pvals[:,borderbottom1:bordertop1,:] = (0xff,0xff,0xff)  # white
pvals[:,borderbottom2:bordertop2,:] = (0xff,0xff,0xff)  # white
pvals[borderbottom3:bordertop3,:,:] = (0xff,0xff,0xff)  # white
pvals[borderbottom4:bordertop4,:,:] = (0xff,0xff,0xff)  # white
picture.set_data(plotarr)
ax1.draw_artist(picture)
f1.canvas.blit(ax1.bbox)


#
# save image to TIFF file foo.tif
#
im = Image.fromarray(plotarr, 'RGB')
im.save('Problem3.eps')

input("\nPress <Enter> to exit...\n")

