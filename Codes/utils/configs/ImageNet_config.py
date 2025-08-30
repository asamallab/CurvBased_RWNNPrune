from easydict import EasyDict as edict
import os
__C = edict()
cfg = __C

# Data set config

__C.DATASET_NAME = "Covid_XRay"

__C.DOWNLOAD = True

#
# Training parameters
#
__C.BATCH_SIZE = 20
__C.EPOCH = 100

#
# Network parameters
#
__C.NN = edict()
__C.NN.REGIME = "SMALL"

# for image color scale
__C.NN.COLOR = 3
# Resizied to 224x224 in torchvision.transforms.Resize()
__C.NN.IMG_SIZE = 224
# Random graph node
__C.NN.NODES = 32
__C.NN.NUM_CLASSES = 2