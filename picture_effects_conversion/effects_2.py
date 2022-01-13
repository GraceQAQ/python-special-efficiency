#!/usr/bin/env python
# encoding: utf-8
'''
#-------------------------------------------------------------------
#                   CONFIDENTIAL --- CUSTOM STUDIOS
#-------------------------------------------------------------------
#
#                   @Project Name : 图片转换特效之流年
#
#                   @File Name    : effects_2.py
#
#                   @Programmer   : autofelix
#
#                   @Start Date   : 2022/01/13 13:14
#
#                   @Last Update  : 2022/01/13 13:14
#
#-------------------------------------------------------------------
'''
import numpy as np
from PIL import Image

class picture:
    '''
     This is a main Class, the file contains all documents.
     One document contains paragraphs that have several sentences
     It loads the original file and converts the original file to new content
     Then the new content will be saved by this class
    '''
    def __init__(self):
        self.path = 'assets/picture.jpeg'

    def hello(self):
        '''
        This is a welcome speech
        :return: self
        '''
        print('*' * 50)
        print(' ' * 20 + '图片转换特效之流年')
        print(' ' * 5 + '作者: autofelix  Date: 2022-01-13 13:14')
        print(' ' * 5 + '主页: https://autofelix.blog.csdn.net')
        print('*' * 50)
        return self

    def run(self):
        '''
        The program entry
        '''
        im = self.fleeting()
        im.show()
        im.save('assets/fleeting.jpeg')

    def fleeting(self, params=12):
        '''
        Picture to fleeting
        '''
        im = np.asarray(Image.open(self.path).convert('RGB'))
        im1 = np.sqrt(im * [1.0, 0.0, 0.0]) * params
        im2 = im * [0.0, 1.0, 1.0]
        im = im1 + im2
        return Image.fromarray(np.array(im).astype('uint8'))

if __name__ == '__main__':
    picture().hello().run()
