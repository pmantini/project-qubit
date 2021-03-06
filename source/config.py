import os
import inspect
import logging

logging_level = logging.INFO

############################################################
## Directories

# Gets the working directory path

if os.name == 'nt':  # WINDOWS
    ROOT_DIR = os.path.abspath(inspect.getfile(inspect.currentframe()))
    ROOT_DIR = '/'.join(ROOT_DIR.split('\\')[:-2]) + '/'
else:
    ROOT_DIR = os.path.abspath(inspect.getfile(inspect.currentframe()))
    ROOT_DIR = '/'.join(ROOT_DIR.split('/')[:-2]) + '/'

print(ROOT_DIR)

# Directory for images and other data
DATA_PATH = ROOT_DIR + 'source/data/'
UPLOADED_IMAGE_FILE_NAME = 'uploaded_image.jpg'
UPLOADED_IMAGE_FILE_PATH = DATA_PATH + UPLOADED_IMAGE_FILE_NAME
RESULT_IMAGE_FILE_PATH = 'result_image.jpg'
FILE_DELETE_TIME = 1200.0

UPLOADED_NOISE_FILE_PATH = DATA_PATH + 'uploaded_noise.jpg'


print(RESULT_IMAGE_FILE_PATH)
############################################################
## Extensions

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'tif'}
