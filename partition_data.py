import glob
import sys
import os
import random
import pdb
from PIL import Image, ImageOps
import cPickle as pickle
import numpy as np
from scipy import misc

from constants import *

if not os.path.isdir(BLOB_TRAIN_IMAGE_DIR):
    os.makedirs(BLOB_TRAIN_IMAGE_DIR)
if not os.path.isdir(BLOB_TRAIN_LABELS_DIR):
    os.makedirs(BLOB_TRAIN_LABELS_DIR)
if not os.path.isdir(BLOB_TEST_IMAGE_DIR):
    os.makedirs(BLOB_TEST_IMAGE_DIR)
if not os.path.isdir(BLOB_TEST_LABELS_DIR):
    os.makedirs(BLOB_TEST_LABELS_DIR)


files = glob.glob(DATA_LABELS_DIR)
all_files = []
print(DATA_LABELS_DIR)
# read files and add into list
for filename in glob.glob(DATA_LABELS_DIR + '*.png'):
    label_name = filename.replace(DATA_LABELS_DIR, "")
    image_name = label_name[-13:-4]     # frame....jpg
    image_name = image_name + ".jpg"
    print(image_name)
    number = int(image_name[5:9])
    temp = [number, image_name, label_name]
    all_files.append(temp)

# sort
sorted_all_files = sorted(all_files)
num_files = len(all_files)
#num_train = np.ceil(num_files*PERCENTAGE_TRAIN)
num_train = 1
train_info = {}
train_txt = open(BLOB_FILE_WITH_TRAIN_INDICES, 'w')
test_txt = open(BLOB_FILE_WITH_TEST_INDICES, 'w')
# count_source_txt = open(COUNT_SOURCE_FILE_INDICES, 'w')
count = 0
# r_sum = 0
# g_sum = 0
# b_sum = 0

for it in range(num_files):
    temp = sorted_all_files[it]
    # Read image
    im = Image.open('{}{}'.format(DATA_IMAGE_DIR, temp[1]))
    label = misc.imread(glob.glob("{}{}".format(DATA_LABELS_DIR, temp[2]))[0])
    label[label > 0] = 1
    image_label = Image.fromarray(np.uint8(label))

    if np.max(label) == 0:
        continue

    # Save image
    if it < num_train:
        im_array = np.asarray(im)
  	#r_sum += np.mean(im_array[:, :, 0])
        #g_sum += np.mean(im_array[:, :, 1])
        #b_sum += np.mean(im_array[:, :, 2])
        save_str = 'frame' + str(count)
        Image.fromarray(np.uint8(label))
        im.save(BLOB_TRAIN_IMAGE_DIR + save_str + '.png')
        image_label.save(BLOB_TRAIN_LABELS_DIR + save_str + '.png')
        train_txt.write(save_str + '\n')
        count += 1

        # for itt in range(NUM_TRAIN_PER_IMAGE):
        #     save_str = 'frame' + str(count)
        #     nc, nr = im.size
        #     valid = False
        #     while not valid:
        #         start_row = random.randint(0, nr - CROP_HEIGHT)
        #         start_col = random.randint(0, nc - CROP_WIDTH)
        #         new_im = im.crop((start_col, start_row, start_col + CROP_WIDTH, start_row + CROP_HEIGHT))
        #         #new_label = label.crop((start_col, start_row, start_col + CROP_WIDTH, start_row + CROP_HEIGHT))
        #         new_label_array = label[start_row:start_row + CROP_HEIGHT, start_col:start_col + CROP_WIDTH]
        #         if np.max(new_label_array) != 0:
        #             valid = True
        #     new_label = Image.fromarray(np.uint8(new_label_array))
        #     rotate = random.randint(0, 1)
        #     if rotate == 1:
        #         new_im = ImageOps.mirror(new_im)
        #         new_label = ImageOps.mirror(new_label)
        #     train_info[save_str] = [temp[1], temp[2], start_col, start_row, start_col + CROP_WIDTH, start_row + CROP_HEIGHT]
        #     new_im.save(BLOB_TRAIN_IMAGE_DIR + save_str + '.png')
        #     new_label.save(BLOB_TRAIN_LABELS_DIR + save_str + '.png')
        #     train_txt.write(save_str + '\n')
        #     count += 1
    else:
        image_label = Image.fromarray(np.uint8(label))
        im.save(BLOB_TEST_IMAGE_DIR + temp[1])
        image_label.save(BLOB_TEST_LABELS_DIR + temp[2])
        test_txt.write(temp[1] + '\n')

#r_mean = r_sum / num_train
#g_mean = g_sum / num_train
#b_mean = b_sum / num_train

#print("R: " + str(r_mean) + " G: " + str(g_mean) + " B: " + str(b_mean))
pickle.dump(train_info, open(BLOB_TRAIN_INFO, 'w'))
train_txt.close()
test_txt.close() 

