import numpy as np
from PIL import Image

im = Image.open('./assets/picture.jpeg').convert('RGB')
arr = np.array(im)

# 黑白
def blackWithe(imagename):
    # r,g,b = r*0.299+g*0.587+b*0.114
    im = np.asarray(Image.open(imagename).convert('RGB'))
    trans = np.array([[0.299,0.587,0.114],[0.299,0.587,0.114],[0.299,0.587,0.114]]).transpose()
    im = np.dot(im,trans)
    return Image.fromarray(np.array(im).astype('uint8'))

blackWithe('./assets/picture.jpeg').show()
blackWithe('./assets/picture.jpeg').save('./dog.jpg')