import numpy as np
from PIL import Image

# 反色
def reverse(imagename):
    im = 255 - np.asarray(Image.open(imagename).convert('RGB'))
    return Image.fromarray(np.array(im).astype('uint8'))