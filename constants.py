""" 
Define Constants
"""

CAFFE_ROOT              = '/home/huxley/caffe/'                         
# Params
PERCENTAGE_TRAIN = 0.2
NUM_TRAIN_PER_IMAGE = 100
CROP_WIDTH = 480
CROP_HEIGHT = 752 

""" BLOB CONSTANTS """
BLOB_DATA_ROOT               = '/notebooks/tree_counting/Data/'
BLOB_MODEL_ROOT		      = '/notebooks/tree_counting/Data/'
DATA_IMAGE_DIR        = BLOB_DATA_ROOT + 'Image/'
DATA_LABELS_DIR        = BLOB_DATA_ROOT + 'Labels/'
BLOB_TRAIN_IMAGE_DIR         = BLOB_MODEL_ROOT + 'images/training/'              
BLOB_TRAIN_LABELS_DIR        = BLOB_MODEL_ROOT + 'annotations/training/'  
BLOB_TEST_IMAGE_DIR         = BLOB_MODEL_ROOT + 'images/validation/'              
BLOB_TEST_LABELS_DIR        = BLOB_MODEL_ROOT + 'annotations/validation/'  
BLOB_TRAIN_INFO             = BLOB_MODEL_ROOT + 'train_info.p'
BLOB_FILE_WITH_TRAIN_INDICES = BLOB_MODEL_ROOT + 'train.txt'                      
BLOB_FILE_WITH_TEST_INDICES = BLOB_MODEL_ROOT + 'test.txt'     
BLOB_COST_MAP_DIR            = BLOB_MODEL_ROOT + 'cost_map/'
BLOB_WORKDIR                 = '/home/huxley/fcn_model_files/orange/blob_model/'
BLOB_MODEL_NAME              = 'blob_orange.caffemodel'       

# Image Parameters
#BLOB_PICTURE_MEAN            = (197.471060768, 219.051099514, 163.143913032)
BLOB_PICTURE_MEAN            = (101.085444336, 113.0388712566, 82.5194905598)


# Solver Parameters
BLOB_SOLVER_DISPLAY          = "20"
BLOB_SOLVER_AVERAGE_LOSS     = "20"
BLOB_SOLVER_BASE_LR          = "1e-10"
BLOB_SOLVER_MOMENTUM         = "0.99"
BLOB_SOLVER_DEBUG_INFO       = "false"

# Random Initial Model Parameters
BLOB_RANDOM_INITIAL_TRAIN    = BLOB_MODEL_ROOT + 'random_train.prototxt'
BLOB_RANDOM_INITIAL_VAL      = BLOB_MODEL_ROOT + 'random_val.prototxt'
BLOB_RANDOM_INITIAL_SOLVER   = BLOB_MODEL_ROOT + 'random_solve.prototxt'
BLOB_RANDOM_INITIAL_MODEL    = BLOB_MODEL_ROOT + 'random_model.caffemodel'

# Actual Model Parameters
BLOB_ACTUAL_TRAIN            = BLOB_MODEL_ROOT + 'trainnet.prototxt'
BLOB_ACTUAL_VAL              = BLOB_MODEL_ROOT + 'valnet.prototxt'
BLOB_ACTUAL_MODEL            = BLOB_MODEL_ROOT + BLOB_MODEL_NAME
BLOB_ACTUAL_SOLVER           = BLOB_MODEL_ROOT + 'solver.prototxt'
BLOB_SURGERY_MODEL_ORIGIN    = BLOB_MODEL_ROOT + 'surgery_origin/fcn8s-heavy-pascal.caffemodel'

# Train Parameters
BLOB_NUM_ITERATIONS          = 500
BLOB_NUM_STEPS               = 100

# Test Parameters
BLOB_NUMPY_SAVE_FILE_DIR     = BLOB_MODEL_ROOT + 'scores/'      
BLOB_SCORE_IMAGE_DIR         = BLOB_MODEL_ROOT + 'score_images/' 
#BLOB_INFER_MODEL             = BLOB_MODEL_ROOT + BLOB_MODEL_NAME  
BLOB_INFER_MODEL             = '/home/huxley/fcn_segmentation/code/python/blob_code/orange_models/snapshot_iter_50000.caffemodel'
BLOB_MODEL_DEPLOY            = BLOB_MODEL_ROOT + 'deploy.prototxt' 

# Analysis Parameters
BLOB_PICKLE_SAVE_LOCATION    = BLOB_MODEL_ROOT + 'blob_analysis.p' # File to save data
BLOB_OVER_TIME_SAVE_LOCATION = BLOB_MODEL_ROOT + 'blob_over_time.p'

