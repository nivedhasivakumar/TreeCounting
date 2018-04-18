__author__ = 'charlie'
import numpy as np
import os
import random
from six.moves import cPickle as pickle
from tensorflow.python.platform import gfile
import glob
import TensorflowUtils as utils


def read_dataset(data_dir):
    pickle_filename = "InferenceData.pickle"
    pickle_filepath = os.path.join(data_dir, pickle_filename)
    if not os.path.exists(pickle_filepath):
        result = create_image_lists(data_dir)
        print ("Pickling ...")
        with open(pickle_filepath, 'wb') as f:
            pickle.dump(result, f, pickle.HIGHEST_PROTOCOL)
    else:
        print ("Found pickle file!")

    with open(pickle_filepath, 'rb') as f:
        result = pickle.load(f)
        inference_records = result
        del result

    return inference_records


def create_image_lists(image_dir):
    if not gfile.Exists(image_dir):
        print("Image directory '" + image_dir + "' not found.")
        return None
    image_list = []
    file_list = []
    file_glob = os.path.join(image_dir, '*.' + 'jpg')
    file_list.extend(glob.glob(file_glob))

    if not file_list:
        print('No files found')
    else:
        for f in file_list:
            filename = os.path.splitext(f.split("/")[-1])[0]
            record = {'image': f, 'filename': filename}
            image_list.append(record)

    no_of_images = len(image_list)
    print ('No. of files: %d' % no_of_images)

    return image_list
