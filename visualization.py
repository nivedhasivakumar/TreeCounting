import scipy.misc as misc
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import glob
import numpy as np
import pickle

i = 0
for filename in glob.glob('/Users/nivedha.sivakumar94/Desktop/tree_counting/Data/Image/pr*.png'):
    print 'Saving image: ' + format(i)
    img_name = filename[60:]
    img = misc.imread(filename)
    # mpimg.imsave(filename, img)

    # Indices where mask == 0
    ind = np.where(img == 0)
    img[ind] = 255
    # inp_name = filename[60:]
    # inp_filename = filename[:60] + inp_name[5:14] + '.jpg'
    # inp = misc.imread(inp_filename)
    # inp[ind] = np.array([153, 51, 255])
    # plt.imshow(inp, cmap=cm.Paired, vmin=0, vmax=1)
    # plt.show()
    misc.imsave('color_' + img_name, img)
    # plt.savefig('color_' + img_name)
    i += 1

# pickle_file = pickle.load(open(, 'rb'))
