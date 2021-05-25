
import numpy as np
from PIL import Image
import time
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import torchvision
from torch.utils.data.sampler import SubsetRandomSampler
from torchvision import datasets, transforms
import random
import os

def getLoader(trainImages, testImages, batch_size=32):
    