import scipy.misc as misc
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
import glob
from scipy.misc import *

# im = misc.imread('/Users/nivedha.sivakumar94/Desktop/tree_counting/Data/Image/frame0035.jpg')
#
# plt.imshow(im)
# plt.show()

i=0
for filename in glob.glob('/Users/nivedha.sivakumar94/Desktop/Tree_counting/Data/inf_im/*.png'): #assuming gif
    i=i+1
    print format(i)
    img = imread(filename)
    index = np.argwhere(img > 0)
    new_img = np.zeros([img.shape[0], img.shape[1]])
    new_img[index[:, 0], index[:, 1]] = 255
    save_im = 'new_' + format(filename[66:])
    imsave(save_im, new_img)

print 'Hi'