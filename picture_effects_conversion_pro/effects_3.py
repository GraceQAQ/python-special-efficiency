import numpy as np
from PIL import Image

# 旧电影
def oldFilm(imagename):
    im = np.asarray(Image.open(imagename).convert('RGB'))
    # r=r*0.393+g*0.769+b*0.189 g=r*0.349+g*0.686+b*0.168 b=r*0.272+g*0.534b*0.131
    trans = np.array([[0.393,0.769,0.189],[0.349,0.686,0.168],[0.272,0.534,0.131]]).transpose()
    # clip 超过255的颜色置为255
    im = np.dot(im,trans).clip(max=255)
    return Image.fromarray(np.array(im).astype('uint8'))