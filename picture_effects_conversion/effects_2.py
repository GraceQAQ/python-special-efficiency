import numpy as np
from PIL import Image

# 流年
def fleeting(imagename,params=12):
    im = np.asarray(Image.open(imagename).convert('RGB'))
    im1 = np.sqrt(im*[1.0,0.0,0.0])*params
    im2 = im*[0.0,1.0,1.0]
    im = im1+im2
    return Image.fromarray(np.array(im).astype('uint8'))